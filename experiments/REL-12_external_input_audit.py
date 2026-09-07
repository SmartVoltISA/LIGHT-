"""REL-12: controlled audit of relation-first local comparison.

The test intentionally uses a complex phase representation to check a known
U(1) case. It does NOT claim to derive U(1); it measures whether a compensating
connection is required for representation-independent local comparison.
"""
import numpy as np

N = 64
x = np.arange(N)
q = np.exp(1j * 0.37 * x)
alpha = 0.17 * np.sin(2 * np.pi * x / N) + 0.03 * np.cos(6 * np.pi * x / N)
T = np.exp(1j * alpha)
qp = T * q

raw = np.roll(qp, -1) - qp
expected_raw = T * (np.roll(q, -1) - q)
raw_error = np.max(np.abs(raw - expected_raw))

# Compensating link for the chosen complex-phase representation.
U = np.exp(1j * (alpha - np.roll(alpha, -1)))
covariant = U * np.roll(qp, -1) - qp
covariant_error = np.max(np.abs(covariant - T * (np.roll(q, -1) - q)))

# 2D additive connection: curvature is the oriented plaquette sum.
nx = ny = 32
rng = np.random.default_rng(7)
A = rng.normal(0, 0.2, (ny, nx, 2))
g = rng.normal(0, 1, (ny, nx))
At = A.copy()
At[:, :, 0] += g - np.roll(g, -1, axis=1)
At[:, :, 1] += g - np.roll(g, -1, axis=0)

F = (
    A[:, :, 0]
    + np.roll(A[:, :, 1], -1, axis=1)
    - np.roll(A[:, :, 0], -1, axis=0)
    - A[:, :, 1]
)
Ft = (
    At[:, :, 0]
    + np.roll(At[:, :, 1], -1, axis=1)
    - np.roll(At[:, :, 0], -1, axis=0)
    - At[:, :, 1]
)
curvature_error = np.max(np.abs(Ft - F))

print(f"raw_difference_covariance_error = {raw_error:.16e}")
print(f"covariant_difference_error = {covariant_error:.16e}")
print(f"curvature_invariance_error = {curvature_error:.16e}")
print("STATUS: SUPPORTS_CONNECTION_PRESSURE; DOES_NOT_DERIVE_U1")

assert raw_error > 1e-4
assert covariant_error < 1e-12
assert curvature_error < 1e-12
