"""REL-18 — Minimum structure for physical dynamics.

Numerical companion to REL-18. Tests a narrow claim:
local path functional + stationarity gives local equations of motion;
time-translation invariance gives a conserved energy-like quantity;
explicit time dependence breaks that conservation law.
"""
import numpy as np


def rk4(f, y0, t):
    y = np.zeros((len(t), len(y0)), dtype=float)
    y[0] = y0
    dt = t[1] - t[0]
    for i in range(len(t) - 1):
        ti, yi = t[i], y[i]
        k1 = f(ti, yi)
        k2 = f(ti + dt / 2, yi + dt * k1 / 2)
        k3 = f(ti + dt / 2, yi + dt * k2 / 2)
        k4 = f(ti + dt, yi + dt * k3)
        y[i + 1] = yi + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return y


m, k = 2.0, 3.0

def run_time_translation_invariant():
    dt = 1e-3
    t = np.arange(0.0, 5.0 + dt, dt)
    sol = rk4(lambda _t, y: np.array([y[1], -(k / m) * y[0]]), [1.0, 0.0], t)
    x, v = sol[:, 0], sol[:, 1]
    E = 0.5 * m * v**2 + 0.5 * k * x**2
    return float(np.max(np.abs(E - E[0])))


def run_explicit_time_dependence():
    gamma = 0.05
    dt = 1e-3
    t = np.arange(0.0, 5.0 + dt, dt)

    # L = 1/2 m v^2 - 1/2 k x^2 + gamma*t*x^2
    sol = rk4(
        lambda tt, y: np.array([y[1], -(k / m) * y[0] + (2 * gamma * tt / m) * y[0]]),
        [1.0, 0.0],
        t,
    )
    x, v = sol[:, 0], sol[:, 1]
    E = 0.5 * m * v**2 + 0.5 * k * x**2 - gamma * t * x**2

    # Noether balance for explicit time dependence: dE/dt = -dL/dt = -gamma*x^2.
    integral = np.concatenate([[0.0], np.cumsum(-gamma * ((x[:-1] ** 2 + x[1:] ** 2) / 2) * np.diff(t))])
    identity_error = np.max(np.abs((E - E[0]) - integral))
    drift = np.max(np.abs(E - E[0]))
    return float(drift), float(identity_error)


if __name__ == "__main__":
    invariant_drift = run_time_translation_invariant()
    explicit_drift, balance_error = run_explicit_time_dependence()
    print(f"time-translation-invariant max energy drift: {invariant_drift:.16e}")
    print(f"explicit-time max energy drift: {explicit_drift:.16e}")
    print(f"Noether balance identity max error: {balance_error:.16e}")
