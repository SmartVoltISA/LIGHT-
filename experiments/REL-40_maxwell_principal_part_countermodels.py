"""REL-40: audit whether minimal relational/hyperbolic requirements select Maxwell.

Question:
    Do locality + first-order finite propagation + positive conserved quadratic
    energy + isotropy/parity-like structural requirements uniquely select the
    Maxwell principal part?

This experiment deliberately does NOT assume Maxwell coefficients, c, SI
normalization, gauge invariance, or electromagnetic interpretation.
"""

import numpy as np


def energy_matrix(M, K):
    """Return the symmetry defect K M - (K M)^T."""
    return K @ M - (K @ M).T


def audit_1d(name, M, K):
    defect = np.linalg.norm(energy_matrix(M, K), ord=np.inf)
    eig = np.linalg.eigvals(M)
    speeds = np.sort(np.real_if_close(eig).real)
    return {
        "name": name,
        "energy_symmetry_defect": float(defect),
        "K_positive_eigs": np.linalg.eigvalsh(K).tolist(),
        "characteristic_speeds": speeds.tolist(),
        "two_way_finite": bool(np.all(np.abs(np.imag(eig)) < 1e-12)
                               and np.any(eig.real < -1e-12)
                               and np.any(eig.real > 1e-12)),
    }


def main():
    # Maxwell-like first-order pair after arbitrary field normalization.
    # M = [[0, 1/eps], [1/mu, 0]], K = diag(eps, mu).
    eps, mu = 4.0, 0.25
    M_maxwell = np.array([[0.0, 1.0 / eps], [1.0 / mu, 0.0]])
    K_maxwell = np.diag([eps, mu])

    # Acoustic/telegrapher-like countermodel: same mathematical principal
    # structure, but there is no electromagnetic meaning.
    M_acoustic = np.array([[0.0, 1.0], [1.0, 0.0]])
    K_acoustic = np.eye(2)

    # Characteristic countermodel: already diagonal, still local, hyperbolic,
    # energy-positive and two-way with conserved quadratic energy.
    M_characteristic = np.diag([1.0, -1.0])
    K_characteristic = np.eye(2)

    results = [
        audit_1d("Maxwell-like", M_maxwell, K_maxwell),
        audit_1d("Acoustic countermodel", M_acoustic, K_acoustic),
        audit_1d("Characteristic countermodel", M_characteristic, K_characteristic),
    ]

    # Explicit algebraic equivalence of the first two principal parts:
    # a diagonal field rescaling U'=S U maps M -> S M S^{-1} while preserving
    # the characteristic eigenvalues. This is the same freedom observed in
    # REL-29 and means speed alone cannot identify electromagnetic structure.
    S = np.diag([2.0, 0.5])
    transformed = S @ M_maxwell @ np.linalg.inv(S)
    similarity_error = np.linalg.norm(
        np.sort(np.linalg.eigvals(transformed)) - np.sort(np.linalg.eigvals(M_maxwell))
    )

    print("REL-40 principal-part countermodel audit")
    for r in results:
        print(r)
    print("similarity_eigenvalue_error", similarity_error)
    print("maxwell_characteristic_speed", 1.0 / np.sqrt(eps * mu))
    print("acoustic_characteristic_speed", 1.0)
    print("CONCLUSION: minimal hyperbolicity + positive energy does not select Maxwell.")


if __name__ == "__main__":
    main()
