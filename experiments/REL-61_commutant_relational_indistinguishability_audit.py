"""REL-61: commutant as relational indistinguishability audit.

Question:
Can the commutant be characterized as transformations that preserve all
currently admitted relational observables, and does scalar commutant follow
when every nontrivial internal transformation creates an independently
observable relation?

This is a countermodel-seeking test. It compares:
1. an irreducible block;
2. duplicated blocks with a non-scalar commutant;
3. duplicated blocks plus an explicitly admitted sector observable.

The experiment tests the proposed implication only inside the finite matrix
model. It does not derive the physical observable algebra, gauge group, or
irreducibility from Omega alone.
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
        out = np.kron(out, xs[1]) if False else out
    # explicit fold avoids accidental axis conventions
    out = xs[0]
    for x in xs[1:]:
        out = np.kron(out, x)
    return out


def gamma_set():
    sx, sy, sz = paulis()
    i2 = np.eye(2, dtype=complex)
    return [kron(sx, i2), kron(sy, i2), kron(sz, sx), kron(sz, sy)]


def residual(A, X):
    return max(np.max(np.abs(a @ X - X @ a)) for a in A)


def span_rank(mats, tol=1e-10):
    if not mats:
        return 0
    M = np.stack([m.reshape(-1) for m in mats], axis=1)
    return int(np.linalg.matrix_rank(M, tol=tol))


def commutant_dimension(generators, basis, tol=1e-10):
    """Dimension of matrices X commuting with every generator."""
    n = generators[0].shape[0]
    cols = []
    for B in basis:
        cols.append(np.concatenate([(G @ B - B @ G).reshape(-1) for G in generators]))
    C = np.stack(cols, axis=1)
    return n * n - int(np.linalg.matrix_rank(C, tol=tol))


def internal_basis(n):
    e = []
    for i in range(n):
        for j in range(n):
            B = np.zeros((n, n), dtype=complex)
            B[i, j] = 1.0
            e.append(B)
    return e


def observable_signature(generators, observables):
    """Vectorized action of generators/observables on matrix units.

    For this audit, an internal transformation X is relationally invisible
    exactly when it commutes with every admitted observable/generator.
    """
    return generators + observables


def main():
    G = gamma_set()
    I4 = np.eye(4, dtype=complex)
    I2 = np.eye(2, dtype=complex)
    sx, sy, sz = paulis()

    # Case A: single irreducible Clifford block.
    basis4 = internal_basis(4)
    dim_single = commutant_dimension(G, basis4)
    assert dim_single == 1, f"Expected scalar commutant, got {dim_single}"

    # Case B: duplicated block. Internal multiplicity transformations are
    # invisible to the doubled Clifford generators.
    G2 = [kron(g, I2) for g in G]
    basis8 = internal_basis(8)
    dim_double = commutant_dimension(G2, basis8)
    assert dim_double == 4, f"Expected 4D commutant, got {dim_double}"

    # Explicit non-scalar commutant elements.
    Xs = [kron(I4, q) for q in (sx, sy, sz)]
    assert max(residual(G2, X) for X in Xs) < 1e-12

    # Case C: admit sector observables I4 tensor sigma_i. These make the
    # multiplicity space relationally accessible. The commutant should shrink
    # back to scalars because the Pauli generators span M_2(C) together with I.
    sector_obs = [kron(I4, q) for q in (sx, sy, sz)]
    enriched = G2 + sector_obs
    dim_enriched = commutant_dimension(enriched, basis8)
    assert dim_enriched == 1, f"Expected scalar enriched commutant, got {dim_enriched}"

    print("REL-61 commutant relational indistinguishability audit")
    print(f"single Clifford commutant dimension: {dim_single}")
    print(f"duplicated Clifford commutant dimension: {dim_double}")
    print(f"duplicated non-scalar commutant residual max: {max(residual(G2, X) for X in Xs):.3e}")
    print(f"enriched observable commutant dimension: {dim_enriched}")
    print("RESULT: a non-scalar commutant is relationally invisible only relative to the admitted algebra; adding independent sector relations removes that indistinguishability.")
    print("BOUNDARY: the criterion requires a prior rule for which relations are physically admissible/observable, so Omega has not yet derived the full observable algebra or irreducibility.")


if __name__ == "__main__":
    main()
