"""REL-59: commutant versus relational redundancy audit.

Question:
Can a non-scalar commutant be identified with pure relational redundancy,
and therefore can scalar commutant/irreducibility be derived from the
relational distinction principle?

Countermodel strategy:
- doubled Clifford sector: Gamma_mu tensor I_2 has a non-scalar commutant;
- an operator in that commutant preserves the full dynamical representation;
- the same mathematical situation can be interpreted either as redundant
  copies or as a genuine internal symmetry/degree of freedom unless an
  additional physical criterion distinguishes the two.

Therefore the audit targets the missing step rather than assuming it.
"""

import numpy as np


def paulis():
    return [
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    ]


def kron(*xs):
    out = xs[0]
    for x in xs[1:]:
        out = np.kron(out, x)
    return out


def gamma_set():
    sx, sy, sz = paulis()
    i2 = np.eye(2, dtype=complex)
    # A 4x4 Euclidean Clifford set is sufficient for the commutant audit.
    return [kron(sx, i2), kron(sy, i2), kron(sz, sx), kron(sz, sy)]


def commutant_residual(gammas, X):
    return max(np.max(np.abs(g @ X - X @ g)) for g in gammas)


def main():
    G = gamma_set()
    I4 = np.eye(4, dtype=complex)
    I2 = np.eye(2, dtype=complex)
    doubled = [kron(g, I2) for g in G]

    # Non-scalar operators acting only on multiplicity space commute with all
    # doubled Clifford generators.
    sx, sy, sz = paulis()
    candidates = [kron(I4, q) for q in (sx, sy, sz)]
    residuals = [commutant_residual(doubled, X) for X in candidates]

    # In a single 4x4 irreducible block, a generic non-scalar Clifford
    # commutant candidate does not commute with the full generating set.
    bad_candidate = G[0]
    single_residual = commutant_residual(G, bad_candidate)

    assert max(residuals) < 1e-12
    assert single_residual > 1e-6

    print("REL-59 commutant versus relational symmetry audit")
    print(f"doubled non-scalar commutant residual max: {max(residuals):.3e}")
    print(f"single-block non-scalar candidate residual: {single_residual:.3e}")
    print("RESULT: a non-scalar commutant is an exact symmetry of the doubled dynamics.")
    print("BOUNDARY: commutation alone does not decide whether that symmetry is gauge redundancy or physical internal structure.")


if __name__ == "__main__":
    main()
