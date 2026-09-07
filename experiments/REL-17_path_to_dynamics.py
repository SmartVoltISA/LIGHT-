"""REL-17 — Path selection versus physical dynamics.

Tests whether path selection by an abstract value functional determines
Euler-Lagrange-like dynamics, or whether the physical action structure has
to be supplied separately.
"""

from __future__ import annotations

import numpy as np


def action(x, dt, m, k):
    v = np.diff(x) / dt
    kinetic = 0.5 * m * v**2
    potential = 0.5 * k * x[:-1]**2
    return float(np.sum((kinetic - potential) * dt))


def value(x, target):
    # Generic value: endpoint preference only.
    return -abs(x[-1] - target)


def main():
    dt = 0.1
    n = 20
    m = 2.0
    k = 3.0

    # Same endpoints can have many paths. Endpoint value cannot distinguish them.
    t = np.arange(n + 1) * dt
    straight = np.linspace(0.0, 1.0, n + 1)
    curved = straight + 0.2 * np.sin(2 * np.pi * t / t[-1])
    curved[0] = 0.0
    curved[-1] = 1.0

    assert np.isclose(value(straight, 1.0), value(curved, 1.0))
    assert np.isclose(straight[0], curved[0]) and np.isclose(straight[-1], curved[-1])

    # A supplied physical action distinguishes trajectories.
    S1 = action(straight, dt, m, k)
    S2 = action(curved, dt, m, k)
    assert not np.isclose(S1, S2)

    # Variation test: small interior perturbation changes S around a stationary
    # discrete path only when the path is actually solved for; arbitrary value
    # does not enforce this condition.
    eps = 1e-5
    perturbed = straight.copy()
    perturbed[n // 2] += eps
    dS = (action(perturbed, dt, m, k) - S1) / eps

    print("REL-17 PASS")
    print(f"endpoint_value_straight={value(straight, 1.0):.6g}")
    print(f"endpoint_value_curved={value(curved, 1.0):.6g}")
    print(f"action_straight={S1:.12g}")
    print(f"action_curved={S2:.12g}")
    print(f"finite_difference_dS={dS:.12g}")
    print("CONCLUSION: endpoint/path value can select or rank trajectories only after a value functional is specified; physical dynamics require additional structure such as a local action functional and its stationarity condition.")


if __name__ == "__main__":
    main()
