"""REL-39: one first-order hyperbolic operator carries the causal and EM cones.

For a 1D transverse vacuum Maxwell sector:
    d/dt [E, H]^T = M d/dx [E, H]^T
with
    M = [[0, 1/eps], [1/mu, 0]]
(up to an orientation/sign convention).

The characteristic speeds are the eigenvalues of M:
    lambda = +/- 1/sqrt(eps*mu).

Thus the causal cone and EM wave cone are properties of the SAME operator.
The test does not derive eps, mu, their SI scale, or the numerical value of c.
"""

import math
import numpy as np


def audit(eps, mu):
    M = np.array([[0.0, 1.0 / eps], [1.0 / mu, 0.0]])
    eig = np.sort(np.linalg.eigvals(M).real)
    v = 1.0 / math.sqrt(eps * mu)
    expected = np.array([-v, v])
    err = float(np.max(np.abs(eig - expected)))
    return eig, v, err


def main():
    cases = [(1.0, 1.0), (4.0, 0.25), (2.0, 8.0), (0.3, 3.0)]
    for eps, mu in cases:
        eig, v, err = audit(eps, mu)
        print(f"eps={eps:g}, mu={mu:g}")
        print(f"eigen_speeds={eig}")
        print(f"characteristic_speed={v:.15g}")
        print(f"max_eigenvalue_error={err:.3e}")
        assert err < 1e-12
        assert np.isclose(abs(eig[0]), eig[1], rtol=0, atol=1e-12)

    print("RESULT: SAME OPERATOR -> SAME CHARACTERISTIC CONE")
    print("BOUNDARY: coefficients eps, mu and absolute SI scale are inputs")


if __name__ == "__main__":
    main()
