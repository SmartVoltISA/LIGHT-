"""REL-14 — Group-selection pressure without choosing U(1) in advance.

Question:
    Does representation-invariant local comparison select the electromagnetic
    gauge group, or does it only require a connection/transport rule?

Tested families:
    R+ scalar rescaling, U(1)/SO(2), SO(3), and GL(2,R).

The experiment separates three claims:
    1. raw local comparison is generally representation-dependent;
    2. a compensating transport restores covariance;
    3. the minimal covariance requirement does not select U(1).

This is a structural test, not a derivation of the physical gauge group.
"""

import numpy as np


def inv(a):
    return np.linalg.inv(a)


def rel_err(a, b):
    return np.linalg.norm(a - b) / max(np.linalg.norm(b), 1e-15)


def family_real(n=24):
    x = np.arange(n, dtype=float)
    return np.array([[[np.exp(0.15*np.sin(2*np.pi*xi/n) +
                              0.05*np.cos(4*np.pi*xi/n))]] for xi in x])


def family_u1(n=24):
    out = []
    for xi in np.arange(n, dtype=float):
        a = 0.37*np.sin(2*np.pi*xi/n) + 0.11*np.cos(4*np.pi*xi/n)
        out.append([[np.cos(a), -np.sin(a)],
                    [np.sin(a),  np.cos(a)]])
    return np.asarray(out, dtype=float)


def family_so3(n=24):
    out = []
    for xi in np.arange(n, dtype=float):
        a = 0.25*np.sin(2*np.pi*xi/n)
        b = 0.17*np.cos(2*np.pi*xi/n)
        c = 0.13*np.sin(4*np.pi*xi/n)
        Rx = np.array([[1,0,0],[0,np.cos(a),-np.sin(a)],[0,np.sin(a),np.cos(a)]])
        Ry = np.array([[np.cos(b),0,np.sin(b)],[0,1,0],[-np.sin(b),0,np.cos(b)]])
        Rz = np.array([[np.cos(c),-np.sin(c),0],[np.sin(c),np.cos(c),0],[0,0,1]])
        out.append(Rz @ Ry @ Rx)
    return np.asarray(out)


def family_gl2(n=24):
    out = []
    for xi in np.arange(n, dtype=float):
        a = 0.10*np.sin(2*np.pi*xi/n)
        b = 0.08*np.cos(2*np.pi*xi/n)
        c = 0.06*np.sin(4*np.pi*xi/n)
        d = 0.05*np.cos(4*np.pi*xi/n)
        out.append([[1+a, b], [c, 1+d]])
    return np.asarray(out, dtype=float)


def raw_comparison_error(T, psi):
    """Error of the naive transformed difference Δ' versus T_i Δ."""
    vals = []
    for i in range(len(T)-1):
        D = psi[i+1] - psi[i]
        Dp = T[i+1] @ psi[i+1] - T[i] @ psi[i]
        vals.append(rel_err(Dp, T[i] @ D))
    return max(vals)


def connection_covariance_error(T, psi):
    """Use U_ij = T_i T_j^{-1}; transformed transport is T_i U_ij T_j^{-1}."""
    vals = []
    for i in range(len(T)-1):
        j = i + 1
        U = T[i] @ inv(T[j])
        D = U @ psi[j] - psi[i]

        # Under psi_i -> T_i psi_i, the link transforms as
        # U -> T_i U T_j^{-1}. The covariant difference must transform as T_i D.
        Up = T[i] @ U @ inv(T[j])
        psi_i_p = T[i] @ psi[i]
        psi_j_p = T[j] @ psi[j]
        Dp = Up @ psi_j_p - psi_i_p
        vals.append(rel_err(Dp, T[i] @ D))
    return max(vals)


def composition_error(T):
    """Check U(i,k) U(k,j) = U(i,j) for U(i,j)=T_i T_j^{-1}."""
    errs = []
    for i in range(0, len(T)-2, 3):
        j, k = i+1, i+2
        Uij = T[i] @ inv(T[j])
        Uik = T[i] @ inv(T[k])
        Ukj = T[k] @ inv(T[j])
        errs.append(rel_err(Uik @ Ukj, Uij))
    return max(errs)


def commutator_norm(T):
    """Probe non-Abelianity of two local transformations."""
    A = T[1] @ inv(T[0])
    B = T[2] @ inv(T[0])
    C = A @ B @ inv(A) @ inv(B)
    return np.linalg.norm(C - np.eye(C.shape[0])), np.linalg.det(C)


def run_family(name, T, dim, seed=14):
    rng = np.random.default_rng(seed)
    psi = rng.normal(size=(len(T), dim))
    raw = raw_comparison_error(T, psi)
    conn = connection_covariance_error(T, psi)
    comp = composition_error(T)
    comm, det = commutator_norm(T)
    return {
        "family": name,
        "raw_comparison_error": raw,
        "connection_covariance_error": conn,
        "composition_error": comp,
        "commutator_norm": comm,
        "commutator_determinant": det,
    }


def main():
    cases = [
        ("R+", family_real(), 1),
        ("U(1)/SO(2)", family_u1(), 2),
        ("SO(3)", family_so3(), 3),
        ("GL(2,R)", family_gl2(), 2),
    ]
    results = [run_family(*case) for case in cases]

    print("REL-14 group-selection pressure")
    for result in results:
        print(result)
    print("\nInterpretation:")
    print("- Raw local comparison is representation-dependent in all tested nontrivial cases.")
    print("- A compensating transport restores covariance for all tested families.")
    print("- Composition is satisfied by the transport construction for all families.")
    print("- SO(3) and GL(2,R) expose non-Abelian commutator structure; R+ and U(1)/SO(2) do not.")
    print("- These minimal requirements do not select U(1).")

    assert all(r["connection_covariance_error"] < 1e-12 for r in results)
    assert all(r["composition_error"] < 1e-12 for r in results)
    assert all(r["raw_comparison_error"] > 1e-4 for r in results)
    assert results[0]["commutator_norm"] < 1e-12
    assert results[1]["commutator_norm"] < 1e-12
    assert results[2]["commutator_norm"] > 1e-6
    assert results[3]["commutator_norm"] > 1e-6


if __name__ == "__main__":
    main()
