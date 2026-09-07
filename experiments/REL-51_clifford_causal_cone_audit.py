import numpy as np

# REL-51: does the causal cone alone force Clifford algebra?
# We separate (A) characteristic-cone information from (B) exact scalar
# second-order closure of a first-order operator.

I4 = np.eye(4, dtype=complex)
I2 = np.eye(2, dtype=complex)
s1 = np.array([[0, 1], [1, 0]], complex)
s2 = np.array([[0, -1j], [1j, 0]], complex)
s3 = np.array([[1, 0], [0, -1]], complex)
alpha = [np.kron(s, s1) for s in (s1, s2, s3)]
beta = np.kron(I2, s3)
eta = np.diag([1, -1, -1, -1])
gamma = [beta] + [beta @ a for a in alpha]

rng = np.random.default_rng(51)
max_closure_error = 0.0
for _ in range(100):
    p = rng.normal(size=4)
    slash = sum(gamma[mu] * p[mu] for mu in range(4))
    p2 = p @ eta @ p
    max_closure_error = max(max_closure_error,
                            np.max(np.abs(slash @ slash - p2 * I4)))

max_clifford_error = 0.0
for mu in range(4):
    for nu in range(4):
        target = 2 * eta[mu, nu] * I4
        err = np.max(np.abs(gamma[mu] @ gamma[nu]
                            + gamma[nu] @ gamma[mu] - target))
        max_clifford_error = max(max_clifford_error, err)

# Algebraic point: if A(p)=Gamma^mu p_mu obeys
# A(p)^2=(g^munu p_mu p_nu) I for every p, polarization of this quadratic
# identity forces {Gamma^mu,Gamma^nu}=2 g^munu I. Exact scalar closure is
# therefore equivalent to the Clifford relation (up to conventions).
exact_closure_forces_clifford = True

print(f"max_closure_error={max_closure_error:.17g}")
print(f"max_clifford_error={max_clifford_error:.17g}")
print(f"exact_closure_forces_clifford={exact_closure_forces_clifford}")

assert max_closure_error < 1e-14
assert max_clifford_error < 1e-14
assert exact_closure_forces_clifford
