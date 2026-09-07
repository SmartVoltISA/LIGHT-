"""REL-03: discrete U(1) gauge/connection relation test.

The test uses a 2D periodic lattice. Site phases are local states; U(1)
link variables are the discrete connection. Gauge transformation must leave
plaquette curvature and gauge-invariant energy unchanged, while the matter
covariant difference transforms covariantly.
"""

import numpy as np


def run(n=32, seed=7):
    rng = np.random.default_rng(seed)
    theta = rng.normal(size=(n, n, 2))
    alpha = rng.normal(size=(n, n))
    psi = np.exp(1j * rng.normal(size=(n, n)))

    U = np.exp(1j * theta)
    g = np.exp(1j * alpha)

    # U_mu(x) -> g(x) U_mu(x) g*(x+mu)
    Up = np.empty_like(U)
    for mu in range(2):
        Up[:, :, mu] = g * U[:, :, mu] * np.conj(np.roll(g, -1, axis=mu))

    # Plaquette: discrete curvature/holonomy.
    P = (
        U[:, :, 0]
        * np.roll(U[:, :, 1], -1, axis=0)
        * np.conj(np.roll(U[:, :, 0], -1, axis=1))
        * np.conj(U[:, :, 1])
    )
    Pp = (
        Up[:, :, 0]
        * np.roll(Up[:, :, 1], -1, axis=0)
        * np.conj(np.roll(Up[:, :, 0], -1, axis=1))
        * np.conj(Up[:, :, 1])
    )

    # Covariant forward difference of a charged site field.
    cov_errors = []
    for mu in range(2):
        D = U[:, :, mu] * np.roll(psi, -1, axis=mu) - psi
        Dp = Up[:, :, mu] * np.roll(g * psi, -1, axis=mu) - g * psi
        cov_errors.append(np.max(np.abs(Dp - g * D)))

    energy = float(np.sum(1.0 - np.real(P)))
    energy_gauge = float(np.sum(1.0 - np.real(Pp)))

    return {
        "max_plaquette_invariance_error": float(np.max(np.abs(P - Pp))),
        "max_covariant_difference_error": float(max(cov_errors)),
        "gauge_invariant_energy": energy,
        "gauge_transformed_energy": energy_gauge,
        "relative_energy_error": (energy_gauge - energy) / energy,
    }


if __name__ == "__main__":
    for key, value in run().items():
        print(f"{key}: {value}")
