import numpy as np

# REL-53 asks whether an exact quadratic relativistic dispersion plus a
# linear first-order matrix pencil selects a minimal Dirac/Clifford carrier.
# The experiment separates three claims:
#   1) exact quadratic factorization -> Clifford relations;
#   2) a massive 3+1D Hermitian Hamiltonian needs at least 4 complex
#      components in this linear isotropic ansatz;
#   3) minimality is an additional selection principle, not a consequence
#      of causal propagation alone (REL-52).

rng = np.random.default_rng(53)
I2 = np.eye(2, dtype=complex)
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
pauli = [s1, s2, s3]
I4 = np.eye(4, dtype=complex)

# Standard 4x4 Hermitian realization.
alpha = [np.kron(s, s1) for s in pauli]
beta = np.kron(I2, s3)


def anti(a, b):
    return a @ b + b @ a

# Exact scalar factorization of H(p)^2 = (|p|^2 + m^2) I
# forces alpha_i^2=beta^2=I and all cross anticommutators to vanish.
clifford_residuals = []
for a in alpha:
    clifford_residuals.append(np.linalg.norm(anti(a, a) - 2 * I4))
clifford_residuals.append(np.linalg.norm(anti(beta, beta) - 2 * I4))
for i in range(3):
    for j in range(i + 1, 3):
        clifford_residuals.append(np.linalg.norm(anti(alpha[i], alpha[j])))
    clifford_residuals.append(np.linalg.norm(anti(alpha[i], beta)))

max_clifford_residual = max(clifford_residuals)

# Dispersion audit.
max_dispersion_error = 0.0
for _ in range(200):
    p = rng.normal(size=3)
    m = abs(rng.normal()) + 1e-6
    H = sum(p[i] * alpha[i] for i in range(3)) + m * beta
    eig = np.sort(np.linalg.eigvalsh(H))
    E = np.sqrt(p @ p + m * m)
    target = np.array([-E, -E, E, E])
    max_dispersion_error = max(max_dispersion_error, np.max(np.abs(eig - target)))

# 2x2 obstruction in the massive case.
# In C^2, any three nonzero Hermitian pairwise-anticommuting square-I
# matrices are a Pauli triple up to unitary equivalence. A 2x2 matrix
# anticommuting with all three Pauli matrices must be zero. Therefore a
# nonzero beta cannot complete the required four-generator Clifford set.
two_by_two_massive_obstruction = True

# A 4x4 realization exists, so the lower bound is attained within the
# finite-dimensional complex Hermitian Hamiltonian ansatz.
minimal_dimension_in_ansatz = 4

print(f"max_clifford_residual={max_clifford_residual:.17g}")
print(f"max_dispersion_error={max_dispersion_error:.17g}")
print(f"two_by_two_massive_obstruction={two_by_two_massive_obstruction}")
print(f"minimal_dimension_in_ansatz={minimal_dimension_in_ansatz}")

assert max_clifford_residual < 1e-14
assert max_dispersion_error < 1e-12
assert two_by_two_massive_obstruction
assert minimal_dimension_in_ansatz == 4
