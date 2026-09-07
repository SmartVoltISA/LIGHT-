"""REL-14 — Group-selection pressure without choosing U(1) in advance.

Question:
    Does representation-invariant local comparison select the electromagnetic
    gauge group, or does it only require a connection/transport rule?

Tested families:
    1. R+ scalar rescaling (GL(1,R)+)
    2. U(1) phase / SO(2) rotation (locally isomorphic)
    3. SO(3) rotations
    4. GL(2,R) general invertible linear transport

For every family we construct a local transport U_i = T_i T_{i+1}^{-1}
that restores covariance of nearest-neighbour comparison. We then measure
transport composition, loop holonomy, and commutator sensitivity.

This experiment is deliberately structural. It does not claim that any one
of these groups is physically realized by electromagnetism.
"""

import numpy as np


def inv(a):
    return np.linalg.inv(a)


def rel_err(a, b):
    den = max(np.linalg.norm(b), 1e-15)
    return np.linalg.norm(a - b) / den


def family_real(n=24):
    x = np.arange(n, dtype=float)
    # positive local rescaling
    return np.array([[[np.exp(0.15 * np.sin(2*np.pi*xi/n) +
                                  0.05*np.cos(4*np.pi*xi/n))]]
                     for xi in x], dtype=float)


def family_u1(n=24):
    x = np.arange(n, dtype=float)
    out = []
    for xi in x:
        a = 0.37*np.sin(2*np.pi*xi/n) + 0.11*np.cos(4*np.pi*xi/n)
        out.append(np.array([[np.cos(a), -np.sin(a)],
                             [np.sin(a),  np.cos(a)]], dtype=float))
    return np.array(out)


def family_so3(n=24):
    x = np.arange(n, dtype=float)
    out = []
    for xi in x:
        a = 0.25*np.sin(2*np.pi*xi/n)
        b = 0.17*np.cos(2*np.pi*xi/n)
        c = 0.13*np.sin(4*np.pi*xi/n)
        Rx = np.array([[1,0,0],[0,np.cos(a),-np.sin(a)],[0,np.sin(a),np.cos(a)]])
        Ry = np.array([[np.cos(b),0,np.sin(b)],[0,1,0],[-np.sin(b),0,np.cos(b)]])
        Rz = np.array([[np.cos(c),-np.sin(c),0],[np.sin(c),np.cos(c),0],[0,0,1]])
        out.append(Rz @ Ry @ Rx)
    return np.array(out)


def family_gl2(n=24):
    x = np.arange(n, dtype=float)
    out = []
    for xi in x:
        a = 0.10*np.sin(2*np.pi*xi/n)
        b = 0.08*np.cos(2*np.pi*xi/n)
        c = 0.06*np.sin(4*np.pi*xi/n)
        d = 0.05*np.cos(4*np.pi*xi/n)
        M = np.array([[1+a, b], [c, 1+d]], dtype=float)
        # Keep matrices safely invertible.
        out.append(M)
    return np.array(out)


def transport_covariance(T, psi):
    """Compare transformed neighbour difference with transported original difference."""
    raw = []
    cov = []
    n = len(T)
    for i in range(n-1):
        D = psi[i+1] - psi[i]
        psi_p_i = T[i] @ psi[i]
        psi_p_j = T[i+1] @ psi[i+1]
        Dp = psi_p_j - psi_p_i
        U = T[i] @ inv(T[i+1])
        transported = inv(T[i]) @ Dp
        # Equivalent convention: U maps transformed neighbour back to site i.
        cov.append(rel_err(Dp, T[i] @ D))
        raw.append(rel_err(Dp, T[i] @ D))
    # The useful invariant statement is checked directly below using U.
    cov2 = []
    for i in range(n-1):
        Dp = T[i+1] @ psi[i+1] - T[i] @ psi[i]
        U = T[i] @ inv(T[i+1])
        lhs = U @ (T[i+1] @ psi[i+1]) - T[i] @ psi[i]
        rhs = T[i] @ (psi[i+1] - psi[i])
        cov2.append(rel_err(lhs, rhs))
    return max(raw), max(cov2)


def connection_covariance(T, psi):
    # Discrete covariant difference D_i psi = U_i psi_{i+1} - psi_i.
    vals = []
    n = len(T)
    for i in range(n-1):
        U = T[i] @ inv(T[i+1])
        D = U @ psi[i+1] - psi[i]
        psi_p_i = T[i] @ psi[i]
        psi_p_j = T[i+1] @ psi[i+1]
        Up = T[i] @ inv(T[i+1])
        Dp = Up @ psi_p_j - psi_p_i
        vals.append(rel_err(Dp, T[i] @ D))
    return max(vals)


def composition_error(T):
    # Transport along i->j must compose: U(i,j) = U(i,k) U(k,j).
    n = len(T)
    errs = []
    for i in range(0, n-2, 3):
        j, k = i+1, i+2
        Uij = T[i] @ inv(T[j])
        Uik = T[i] @ inv(T[k])
        Ukj = T[k] @ inv(T[j])
        errs.append(rel_err(Uik @ Ukj, Uij))
    return max(errs)


def holonomy_and_commutator(T):
    # A generic two-direction local loop requires independent transports.
    # Build matrices A,B from two neighbouring local-frame changes.
    A = T[1] @ inv(T[0])
    B = T[2] @ inv(T[0])
    comm = A @ B @ inv(A) @ inv(B)
    return np.linalg.norm(comm - np.eye(comm.shape[0])), np.linalg.det(comm)


def run_family(name, T, dim):
    rng = np.random.default_rng(14)
    psi = rng.normal(size=(len(T), dim))
    raw, _ = transport_covariance(T, psi)
    conn = connection_covariance(T, psi)
    comp = composition_error(T)
    hol, det = holonomy_and_commutator(T)
    return {
        "family": name,
        "raw_comparison_error": raw,
        "connection_covariance_error": conn,
        "composition_error": comp,
        "commutator_norm": hol,
        "commutator_determinant": det,
    }


def main():
    cases = [
        ("R+", family_real(), 1),
        ("U(1)/SO(2)", family_u1(), 2),
        ("SO(3)", family_so3(), 3),
        ("GL(2,R)", family_gl2(), 2),
    ]
    results = [run_family(*c) for c in cases]

    print("REL-14 group-selection pressure")
    for r in results:
        print(r)
    print("\nInterpretation:")
    print("- Local covariance requires transport/connection across all tested families.")
    print("- Composition follows from the transport construction for all families.")
    print("- Non-commuting families can exhibit non-trivial loop commutators.")
    print("- These structural requirements do not select U(1).")

    # Hard numerical sanity checks.
    assert all(r["connection_covariance_error"] < 1e-12 for r in results)
    assert all(r["composition_error"] < 1e-12 for r in results)
    assert results[0]["commutator_norm"] < 1e-12
    assert results[1]["commutator_norm"] < 1e-12
    assert results[2]["commutator_norm"] > 1e-6
    assert results[3]["commutator_norm"] > 1e-6


if __name__ == "__main__":
    main()
