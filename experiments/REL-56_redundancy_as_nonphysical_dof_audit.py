import numpy as np

# REL-56: test whether duplicated identical sectors introduce
# distinguishable physical dynamics or only an internal multiplicity.
# We deliberately separate:
#   (A) equality of the dynamical operator,
#   (B) existence of a nontrivial commutant,
#   (C) whether a chosen observable algebra can distinguish sectors.
# This does NOT assume that mathematical redundancy is automatically gauge.

rng = np.random.default_rng(56)
I2 = np.eye(2, dtype=complex)
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
pauli = [s1, s2, s3]
alpha = [np.kron(s, s1) for s in pauli]
beta = np.kron(I2, s3)
I4 = np.eye(4, dtype=complex)

# Base Dirac Hamiltonian.
def H4(p, m):
    return sum(p[i] * alpha[i] for i in range(3)) + m * beta

# Two identical copies: H8 = H4 \otimes I2.
I_mult = I2

def H8(p, m):
    return np.kron(H4(p, m), I_mult)

# A sector-mixing operator acting only on multiplicity space.
Xmix = np.kron(I4, s1)
Zmix = np.kron(I4, s3)

max_comm_X = 0.0
max_comm_Z = 0.0
max_spectrum_split = 0.0

for _ in range(100):
    p = rng.normal(size=3)
    m = abs(rng.normal())
    H = H8(p, m)
    max_comm_X = max(max_comm_X, np.linalg.norm(Xmix @ H - H @ Xmix))
    max_comm_Z = max(max_comm_Z, np.linalg.norm(Zmix @ H - H @ Zmix))

    eig = np.sort(np.linalg.eigvalsh(H))
    E = np.sqrt(p @ p + m * m)
    target = np.sort(np.array([-E, -E, -E, -E, E, E, E, E]))
    max_spectrum_split = max(max_spectrum_split, np.max(np.abs(eig - target)))

# Compare with a sector-distinguishing perturbation. This is intentionally
# outside the identical-copy hypothesis: it demonstrates what extra input
# would be needed to make multiplicity physically distinguishable.
sector_break = np.kron(I4, s3)
p = np.array([0.3, -0.7, 0.4])
m = 0.8
H = H8(p, m)
for eps in [0.0, 0.1, 0.5]:
    Hb = H + eps * sector_break
    vals = np.sort(np.linalg.eigvalsh(Hb))
    if eps == 0.0:
        base = vals
    else:
        max_spectrum_split = max(max_spectrum_split, np.max(np.abs(vals - base)))

print(f"max_comm_X={max_comm_X:.17g}")
print(f"max_comm_Z={max_comm_Z:.17g}")
print(f"max_identical_copy_spectrum_error={max_spectrum_split:.17g}")

assert max_comm_X < 1e-14
assert max_comm_Z < 1e-14

# The two-copy system is dynamically identical sector-by-sector. Therefore
# the test cannot justify calling multiplicity 'gauge redundancy' by itself.
# A physical distinction requires an observable/interactor that couples to
# multiplicity; without such extra structure, the multiplicity is not fixed
# by the original Clifford dynamics.
print("RESULT: identical multiplicity is dynamically invisible to the base operator, but not automatically gauge.")
print("RESULT: irreducibility requires an additional physical criterion, e.g. no unaccounted observable algebra or no independent relational content.")
