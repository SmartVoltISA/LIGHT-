"""REL-02E: vector Maxwell relation + energy test.

1D vacuum Maxwell system for a transverse plane wave:
    dE_y/dt = -(1/epsilon) dH_z/dx
    dH_z/dt = -(1/mu)       dE_y/dx

The Yee-like staggered update uses spatial differences as the relation
operator. The same relation structure drives propagation and electromagnetic
energy storage/transport.
"""

import math
import numpy as np


def run(n=400, steps=1200, dx=1.0, eps=1.0, mu=1.0, dt=0.5):
    if dt / dx >= 1.0 / math.sqrt(eps * mu):
        raise ValueError("unstable CFL choice: require dt/dx < 1/sqrt(eps*mu)")

    x = np.arange(n, dtype=float) * dx
    c = 1.0 / math.sqrt(eps * mu)
    z = math.sqrt(mu / eps)

    # Right-moving transverse pulse: H_z = E_y / Z.
    E = np.exp(-((x - 100.0) / 12.0) ** 2)
    H = E / z

    energies = []
    centers = []

    for _ in range(steps):
        # Discrete relation: nearest-neighbour spatial difference.
        H_new = H - dt / (mu * dx) * (E - np.roll(E, 1))
        E_new = E - dt / (eps * dx) * (np.roll(H_new, -1) - H_new)

        # Put E and H on the same effective time level for diagnostics.
        H_mid = 0.5 * (H + H_new)
        u = 0.5 * (eps * E_new**2 + mu * H_mid**2)
        energies.append(float(np.sum(u) * dx))

        phase = np.sum(u * np.exp(2j * np.pi * np.arange(n) / n))
        centers.append(float((np.angle(phase) % (2 * np.pi)) * n / (2 * np.pi)))

        E, H = E_new, H_new

    energies = np.asarray(energies)
    centers = np.unwrap(np.asarray(centers) * 2 * np.pi / n) * n / (2 * np.pi)
    times = np.arange(1, steps + 1, dtype=float) * dt

    lo = max(10, steps // 12)
    hi = max(lo + 2, steps * 2 // 3)
    speed = float(np.polyfit(times[lo:hi], centers[lo:hi], 1)[0])

    return {
        "c_target": c,
        "c_measured": speed,
        "relative_speed_error": (speed - c) / c,
        "E_initial": float(energies[0]),
        "E_final": float(energies[-1]),
        "relative_final_energy_error": float((energies[-1] - energies[0]) / energies[0]),
        "relative_energy_range": float((energies.max() - energies.min()) / energies[0]),
        "transverse_components": "E_y, H_z; propagation along x",
    }


if __name__ == "__main__":
    for key, value in run().items():
        print(f"{key}: {value}")
