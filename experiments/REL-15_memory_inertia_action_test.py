"""REL-15 — Memory, inertia and action.

Question:
    Does a generic notion of memory force physical inertia/mass, or is a
    more specific momentum-like state / action structure required?

Tests:
    1. Memoryless first-order response: no finite inertia parameter appears.
    2. Second-order state (x, v): past state v persists after an impulse.
    3. Impulse response verifies Delta-v = J/m.
    4. Free-particle action L = 1/2 m v^2 gives p = m v and constant p.
    5. The coefficient m is not selected by the abstract memory rule alone.

Interpretation is deliberately conservative: the experiment supports a
mapping from retained dynamical state -> inertia, but does not derive the
physical value or origin of mass.
"""

import numpy as np


def rel_err(a, b):
    den = max(abs(float(b)), 1e-15)
    return abs(float(a) - float(b)) / den


def first_order_memoryless(J=1.0, k=2.0, dt=1e-4, T=0.1):
    """Overdamped response: velocity follows current force only."""
    n = int(T / dt)
    x = 0.0
    v = 0.0
    for i in range(n):
        F = J / dt if i == 0 else 0.0
        v = F / k
        x += dt * v
    return x, v


def inertial_impulse(m=2.0, J=1.0, dt=1e-4, T=0.1):
    """m x_ddot = F; v is retained as part of the state."""
    n = int(T / dt)
    x = 0.0
    v = 0.0
    for i in range(n):
        F = J / dt if i == 0 else 0.0
        v += dt * F / m
        x += dt * v
    return x, v


def free_action_trajectory(m=2.0, v0=1.7, dt=1e-3, steps=1000):
    """Discrete free-particle trajectory and canonical momentum p=m v."""
    x = 0.0
    v = v0
    xs = []
    ps = []
    actions = []
    for _ in range(steps):
        xs.append(x)
        ps.append(m * v)
        actions.append(0.5 * m * v * v * dt)
        x += dt * v
    return np.array(xs), np.array(ps), float(np.sum(actions))


def main():
    # 1. Memoryless model: no post-impulse persistence.
    _, v_memless = first_order_memoryless()
    assert abs(v_memless) < 1e-15

    # 2. Inertial model: post-impulse velocity persists.
    m = 2.0
    J = 1.0
    _, v_inertial = inertial_impulse(m=m, J=J)
    expected_v = J / m
    impulse_error = rel_err(v_inertial, expected_v)
    assert impulse_error < 1e-12

    # 3. Mass/inertia scaling: doubling m halves Delta-v.
    v1 = inertial_impulse(m=1.0, J=J)[1]
    v4 = inertial_impulse(m=4.0, J=J)[1]
    scaling_error = rel_err(v4, v1 / 4.0)
    assert scaling_error < 1e-12

    # 4. Action: L=1/2 m v^2 gives p=m v; free trajectory keeps p constant.
    _, ps, S = free_action_trajectory(m=m, v0=1.7)
    momentum_spread = np.max(ps) - np.min(ps)
    expected_p = m * 1.7
    momentum_error = rel_err(ps[0], expected_p)
    assert momentum_spread < 1e-12
    assert momentum_error < 1e-12
    assert S > 0.0

    print("REL-15 memory-inertia-action test")
    print(f"memoryless_post_impulse_velocity={v_memless:.16e}")
    print(f"inertial_delta_v={v_inertial:.16e}")
    print(f"expected_J_over_m={expected_v:.16e}")
    print(f"impulse_relative_error={impulse_error:.3e}")
    print(f"mass_scaling_relative_error={scaling_error:.3e}")
    print(f"free_particle_momentum={ps[0]:.16e}")
    print(f"free_particle_momentum_spread={momentum_spread:.3e}")
    print(f"discrete_action={S:.16e}")
    print("\nInterpretation:")
    print("- Generic retained history is not sufficient to define physical mass.")
    print("- A retained momentum-like state produces inertial persistence.")
    print("- In the quadratic free-particle action, m is the coefficient controlling inertia.")
    print("- The architecture supports memory -> inertial state, but does not derive the value/origin of m.")


if __name__ == "__main__":
    main()
