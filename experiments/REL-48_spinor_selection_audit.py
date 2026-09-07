import numpy as np


def scalar_countermodel(phi, q, A, grad_lambda, lam):
    """Local U(1)-covariant scalar: D'phi' = exp(i q lam) D phi."""
    phase = np.exp(1j * q * lam)
    phi_p = phase * phi
    A_p = A - grad_lambda
    Dphi = 1j * q * A * phi
    Dphi_p = 1j * q * A_p * phi_p
    return Dphi_p - phase * (Dphi + 1j * q * grad_lambda * phi)


def run():
    rng = np.random.default_rng(48)
    max_res = 0.0
    for _ in range(100):
        phi = rng.normal() + 1j * rng.normal()
        q = rng.normal()
        A = rng.normal(size=4)
        grad = rng.normal(size=4)
        lam = rng.normal()
        # D = partial + i q A; include an independent derivative of phi.
        dphi = rng.normal(size=4) + 1j * rng.normal(size=4)
        phase = np.exp(1j * q * lam)
        phi_p = phase * phi
        A_p = A - grad
        dphi_p = phase * (dphi + 1j * q * grad * phi)
        Dp = dphi_p + 1j * q * A_p * phi_p
        D = dphi + 1j * q * A * phi
        res = np.max(np.abs(Dp - phase * D))
        max_res = max(max_res, float(res))
    print("REL-48 scalar countermodel U(1) covariance max residual:", max_res)
    assert max_res < 1e-12
    print("Conclusion: local U(1) covariance does not select spin-1/2 or Dirac structure.")
    print("A charged scalar is already a countermodel; a charged Weyl field is another.")


if __name__ == "__main__":
    run()
