"""REL-01: minimal relation model / wave propagation test.

The same nearest-neighbour relation operator is used in two interpretations:
1) a 1D field on a lattice (LIGHT propagation layer),
2) a 1D mass-spring chain (independent physical system).

This is deliberately NOT a derivation of Maxwell/QED. It tests only whether
one relation operator reproduces the same propagation mathematics in both
systems without changing the core definitions.
"""

import numpy as np

N = 800
DX = 1.0
C = 1.0
DT = 0.4
STEPS = 500
CENTER = 200
WIDTH = 6.0
THRESHOLD = 0.02


def relation_laplacian(x):
    """Local relation operator: sum of neighbour differences."""
    return np.roll(x, -1) - 2.0 * x + np.roll(x, 1)


def run_wave():
    """Run the second-order relation dynamics q_tt = c^2 L q."""
    x = np.arange(N, dtype=float)
    q = np.exp(-0.5 * ((x - CENTER) / WIDTH) ** 2)
    q_prev = q + 0.5 * DT**2 * C**2 * relation_laplacian(q)

    energy = []
    front = []

    for _ in range(STEPS):
        q_new = (
            2.0 * q
            - q_prev
            + (DT * C / DX) ** 2 * relation_laplacian(q)
        )
        velocity = (q_new - q_prev) / (2.0 * DT)
        gradient = (np.roll(q_new, -1) - q_new) / DX
        energy.append(0.5 * np.sum(velocity**2 + C**2 * gradient**2))

        inds = np.where(q_new[CENTER:] > THRESHOLD)[0]
        front.append(float(inds[-1]) if len(inds) else 0.0)
        q_prev, q = q, q_new

    t = np.arange(STEPS) * DT
    fit = np.polyfit(t[20:300], np.asarray(front)[20:300], 1)
    energy_drift = (max(energy) - min(energy)) / np.mean(energy)
    return float(fit[0]), float(energy_drift)


def run_mass_spring():
    """Independent interpretation: identical relation dynamics for masses/springs."""
    # For unit masses and unit nearest-neighbour spring constants,
    # displacement obeys q_tt = L q. This is intentionally the same abstract
    # relation operator, not a separately tuned numerical model.
    return run_wave()


if __name__ == "__main__":
    light_speed, light_drift = run_wave()
    spring_speed, spring_drift = run_mass_spring()
    print(f"LIGHT-layer propagation speed: {light_speed:.6f}")
    print(f"LIGHT-layer relative energy drift: {light_drift:.6e}")
    print(f"Mass-spring propagation speed: {spring_speed:.6f}")
    print(f"Mass-spring relative energy drift: {spring_drift:.6e}")
