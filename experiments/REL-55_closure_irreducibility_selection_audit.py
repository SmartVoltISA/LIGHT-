import numpy as np

# REL-55 — Closure versus irreducibility audit
#
# Question:
# Can "closure" by itself select the irreducible Clifford carrier,
# or does irreducibility remain an additional axiom?
#
# We test the commutant of k identical copies of a 3+1D Clifford module.
# For an irreducible complex module, Schur's lemma predicts a scalar
# commutant. For k copies, the multiplicity space carries Mat_k(C), so
# the commutant has complex dimension k^2.

I2 = np.eye(2, dtype=complex)
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)

pauli = [s1, s2, s3]
alpha = [np.kron(s, s1) for s in pauli]
beta = np.kron(I2, s3)
gamma_generators = [beta] + alpha


def commutant_dimension(generators, tol=1e-10):
    """Dimension over C of {X : XG=GX for every generator G}."""
    n = generators[0].shape[0]
    blocks = []
    eye = np.eye(n, dtype=complex)
    for G in generators:
        # vec(XG-GX) = (G.T kron I - I kron G) vec(X)
        blocks.append(np.kron(G.T, eye) - np.kron(eye, G))
    M = np.vstack(blocks)
    rank = np.linalg.matrix_rank(M, tol=tol)
    return n * n - rank


results = {}
for multiplicity in (1, 2, 3):
    generators = [np.kron(G, np.eye(multiplicity, dtype=complex))
                  for G in gamma_generators]
    d = commutant_dimension(generators)
    results[multiplicity] = d
    print(f"multiplicity={multiplicity}, commutant_dim={d}, expected={multiplicity**2}")
    assert d == multiplicity ** 2

# A scalar commutant is therefore equivalent here to selecting multiplicity 1.
# This is a mathematical closure/irreducibility criterion, not a derivation
# from the upstream Omega primitives. The experiment deliberately records
# that boundary instead of silently promoting the criterion to an Omega axiom.
assert results[1] == 1
assert results[2] > 1
assert results[3] > 1

print("closure_test: multiplicity=1 only")
print("boundary: commutant-scalar criterion is imposed, not derived from Omega")
