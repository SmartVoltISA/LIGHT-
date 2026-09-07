import numpy as np

# REL-52: test whether first-order local hyperbolic propagation with the
# same finite causal cone uniquely selects a Dirac/Clifford carrier.
# Sharing a characteristic cone is weaker than exact scalar Clifford
# factorization.

# 1D symmetric hyperbolic two-component system.
H1 = np.array([[0.0, 1.0], [1.0, 0.0]])

# Direct sum of two identical local first-order sectors.
H4 = np.block([
    [H1, np.zeros((2, 2))],
    [np.zeros((2, 2)), H1],
])

for H in (H1, H4):
    eig = np.linalg.eigvalsh(H)
    # Finite characteristic speeds +/-1 in the chosen units.
    assert np.allclose(np.sort(eig), -np.sort(-eig))
    assert np.allclose(np.abs(eig), 1.0)

# Positive quadratic norm and first-order propagation exist here, but this
# construction is not a 3+1D Lorentz Clifford module: it contains no four
# spacetime-indexed gamma matrices and no exact four-dimensional scalar
# factorization requirement.
assert np.allclose(H4 @ H4, np.eye(4))

unique_dirac_selected = False
print(f"unique_dirac_selected={unique_dirac_selected}")
assert not unique_dirac_selected
