import numpy as np

rng = np.random.default_rng(49)
I2 = np.eye(2, dtype=complex)
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
pauli = [s1, s2, s3]

# A concrete 4x4 first-order relativistic Hamiltonian representation.
# H(p) = alpha_i p_i + beta m, with the Clifford relations required
# for H(p)^2 = (|p|^2 + m^2) I.
alpha = [np.kron(s, s1) for s in pauli]
beta = np.kron(I2, s3)
I4 = np.eye(4, dtype=complex)

def anti(a, b):
    return a @ b + b @ a

relations = []
for a in alpha:
    relations.append(np.linalg.norm(anti(a, a) - 2 * I4))
relations.append(np.linalg.norm(anti(beta, beta) - 2 * I4))
for i in range(3):
    for j in range(i + 1, 3):
        relations.append(np.linalg.norm(anti(alpha[i], alpha[j])))
    relations.append(np.linalg.norm(anti(alpha[i], beta)))

max_clifford_residual = max(relations)

# Dispersion audit over random momenta and masses.
max_dispersion_error = 0.0
for _ in range(100):
    p = rng.normal(size=3)
    m = abs(rng.normal())
    H = sum(p[i] * alpha[i] for i in range(3)) + m * beta
    eig = np.sort(np.linalg.eigvalsh(H))
    E = np.sqrt(p @ p + m * m)
    target = np.array([-E, -E, E, E])
    max_dispersion_error = max(max_dispersion_error, np.max(np.abs(eig - target)))

# A 2x2 massive first-order realization would require four Hermitian
# matrices alpha_1, alpha_2, alpha_3, beta, each squaring to I and
# pairwise anticommuting. In C^2, three such matrices are unitarily
# equivalent to the Pauli matrices; the only 2x2 matrix anticommuting
# with all three is zero, so no fourth nonzero beta exists.
# We record this as an algebraic obstruction rather than pretending a
# finite numerical search proves it.
two_by_two_massive_obstruction = True

print(f"max_clifford_residual={max_clifford_residual:.17g}")
print(f"max_dispersion_error={max_dispersion_error:.17g}")
print(f"two_by_two_massive_obstruction={two_by_two_massive_obstruction}")

assert max_clifford_residual < 1e-14
assert max_dispersion_error < 1e-12
assert two_by_two_massive_obstruction
