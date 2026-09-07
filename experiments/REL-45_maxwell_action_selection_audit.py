import numpy as np

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])


def maxwell_kernel(k):
    """Quadratic Maxwell kernel, up to an overall normalization/sign."""
    k = np.asarray(k, dtype=float)
    k_cov = ETA @ k
    k2 = float(k @ k_cov)
    return k2 * ETA - np.outer(k_cov, k_cov)


def proca_kernel(k, m2=1.0):
    """Maxwell kernel plus a Proca mass term; the mass term breaks gauge invariance."""
    return maxwell_kernel(k) + m2 * ETA


def higher_derivative_kernel(k, lam=1.0):
    """Gauge-invariant higher-derivative deformation: (1+lam*k^2) F^2 kernel."""
    k = np.asarray(k, dtype=float)
    k_cov = ETA @ k
    k2 = float(k @ k_cov)
    return (1.0 + lam * k2) * maxwell_kernel(k)


def gauge_residual(K, k):
    return float(np.max(np.abs(K @ (ETA @ k))))


def run():
    momenta = [
        np.array([2.0, 1.0, 0.5, 0.2]),
        np.array([1.0, 1.0, 0.0, 0.0]),
        np.array([3.0, 0.2, -0.4, 1.1]),
    ]

    maxwell_res = [gauge_residual(maxwell_kernel(k), k) for k in momenta]
    proca_res = [gauge_residual(proca_kernel(k), k) for k in momenta]
    higher_res = [gauge_residual(higher_derivative_kernel(k), k) for k in momenta]

    print("REL-45 Maxwell action selection audit")
    print("Maxwell gauge residual max:", max(maxwell_res))
    print("Proca gauge residual min/max:", min(proca_res), max(proca_res))
    print("Higher-derivative gauge residual max:", max(higher_res))
    print()
    print("Conditional structural result:")
    print("- Lorentz covariance + locality + U(1) gauge invariance")
    print("- quadratic, parity-even action")
    print("- at most two derivatives")
    print("=> unique nontrivial kinetic structure is F_{mu nu} F^{mu nu}, up to normalization")
    print("- F tilde F is a topological/boundary term for constant theta and does not change local vacuum EOM")
    print("- Proca mass term fails gauge invariance")
    print("- higher-derivative F box F is gauge invariant but lies outside the two-derivative/renormalizable class")

    assert max(maxwell_res) < 1e-14
    assert max(higher_res) < 1e-14
    assert min(proca_res) > 1e-12


if __name__ == "__main__":
    run()
