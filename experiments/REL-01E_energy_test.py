"""REL-01E: energy-constrained relation test.

Minimal 1D relation model:
    q_ddot[i] = c^2 (q[i+1] - 2 q[i] + q[i-1]) / dx^2

The experiment tracks kinetic + relation/potential energy while the wave
propagates in a closed chain with fixed endpoints.
"""

import numpy as np


def acceleration(q, c=1.0, dx=1.0):
    a = np.zeros_like(q)
    a[1:-1] = c**2 * (q[2:] - 2.0*q[1:-1] + q[:-2]) / dx**2
    return a


def energy(q, v, c=1.0, dx=1.0):
    kinetic = 0.5 * np.sum(v**2)
    relation = 0.5 * c**2 * np.sum((q[1:] - q[:-1])**2)
    return kinetic + relation


def run(n=201, steps=2000, dt=0.2, c=1.0, dx=1.0):
    x = np.arange(n, dtype=float)
    q = np.exp(-((x - 50.0) / 8.0)**2)
    v = np.zeros_like(q)

    energies = [energy(q, v, c, dx)]

    # Velocity-Verlet integration.
    for _ in range(steps):
        a = acceleration(q, c, dx)
        v += 0.5 * dt * a
        q += dt * v
        a = acceleration(q, c, dx)
        v += 0.5 * dt * a
        energies.append(energy(q, v, c, dx))

    energies = np.asarray(energies)
    return {
        "E_initial": float(energies[0]),
        "E_final": float(energies[-1]),
        "E_min": float(energies.min()),
        "E_max": float(energies.max()),
        "relative_range": float((energies.max() - energies.min()) / energies[0]),
        "relative_final_error": float((energies[-1] - energies[0]) / energies[0]),
    }


if __name__ == "__main__":
    print(run())
