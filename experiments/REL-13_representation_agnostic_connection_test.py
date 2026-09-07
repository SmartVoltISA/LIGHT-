"""REL-13: representation-agnostic connection pressure.

Purpose:
    Test the structural statement without selecting U(1) as the only allowed
    local representation. Three local representation families are tested:
    positive scalar rescaling, complex phase, and SO(2) rotation.

For each family, a raw nearest-neighbour difference is compared with the
transformed reference difference. A compensating local connection is then
constructed directly from neighboring representation maps.

This does NOT derive a physical gauge group. It tests whether the need for a
comparison/transport rule survives when the representation class changes.
"""
import numpy as np

N = 64
x = np.arange(N)

results = {}

# 1) Positive real local rescaling: T(x) in R_{>0}.
q = np.sin(0.37 * x) + 0.2 * np.cos(0.11 * x)
a = 0.17 * np.sin(2 * np.pi * x / N) + 0.03 * np.cos(6 * np.pi * x / N)
T = np.exp(a)
qp = T * q
raw = np.roll(qp, -1) - qp
expected = T * (np.roll(q, -1) - q)
raw_err = np.max(np.abs(raw - expected))
U = T / np.roll(T, -1)
cov = U * np.roll(qp, -1) - qp
cov_err = np.max(np.abs(cov - expected))
results["positive_scale"] = (raw_err, cov_err)

# 2) Complex phase: the familiar U(1) case, retained only as one member
#    of the comparison family.
q = np.exp(1j * 0.37 * x)
qp = np.exp(1j * a) * q
raw = np.roll(qp, -1) - qp
expected = np.exp(1j * a) * (np.roll(q, -1) - q)
raw_err = np.max(np.abs(raw - expected))
U = np.exp(1j * a) / np.exp(1j * np.roll(a, -1))
cov = U * np.roll(qp, -1) - qp
cov_err = np.max(np.abs(cov - expected))
results["complex_phase"] = (raw_err, cov_err)

# 3) SO(2) local rotations on a two-component state.
theta = 0.21 * np.sin(2 * np.pi * x / N) + 0.05 * np.cos(4 * np.pi * x / N)
T = np.stack([
    np.stack([np.cos(theta), -np.sin(theta)], axis=1),
    np.stack([np.sin(theta),  np.cos(theta)], axis=1),
], axis=1)
q = np.stack([np.sin(0.37 * x), np.cos(0.23 * x)], axis=1)
qp = np.einsum("nij,nj->ni", T, q)
raw = np.roll(qp, -1, axis=0) - qp
expected = np.einsum("nij,nj->ni", T, np.roll(q, -1, axis=0) - q)
raw_err = np.max(np.linalg.norm(raw - expected, axis=1))
Tnext = np.roll(T, -1, axis=0)
U = np.matmul(T, np.transpose(Tnext, (0, 2, 1)))
cov = np.einsum("nij,nj->ni", U, np.roll(qp, -1, axis=0)) - qp
cov_err = np.max(np.linalg.norm(cov - expected, axis=1))
results["SO2_rotation"] = (raw_err, cov_err)

for name, (raw_err, cov_err) in results.items():
    print(f"{name}: raw_error={raw_err:.16e}, covariant_error={cov_err:.16e}")
    assert raw_err > 1e-4
    assert cov_err < 1e-12

print("STATUS: REPRESENTATION_AGNOSTIC_CONNECTION_PRESSURE")
print("STATUS: DOES_NOT_SELECT_OR_DERIVE_A_PHYSICAL_GAUGE_GROUP")
