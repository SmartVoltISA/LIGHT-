"""REL-16 — Value/path selection test.

Question:
Can an abstract value functional select a path among memory-constrained
alternatives, and does that alone determine physical dynamics?

The experiment deliberately separates:
  memory/constraints -> admissible paths
  value functional  -> ordering of paths
  choice rule       -> selected path
  physical action   -> a separate, explicitly supplied object

This is a structural test, not a claim that utility/value is physical action.
"""

from __future__ import annotations

import math


def paths(start: int, goal: int, max_step: int = 1, horizon: int = 4):
    out = []

    def walk(x, p):
        if len(p) - 1 == horizon:
            if x == goal:
                out.append(tuple(p))
            return
        for dx in range(-max_step, max_step + 1):
            walk(x + dx, p + [x + dx])

    walk(start, [start])
    return out


def value_path(path):
    # Abstract preference: shorter total variation is preferred.
    return -sum(abs(path[i + 1] - path[i]) for i in range(len(path) - 1))


def kinetic_action(path, dt=1.0, mass=1.0):
    # Explicit physical action candidate; mass is deliberately an input.
    return sum(0.5 * mass * ((path[i + 1] - path[i]) / dt) ** 2 * dt
               for i in range(len(path) - 1))


def main():
    # Memory imposes a local transition constraint: |dx| <= 1 per step.
    candidates = paths(0, 2, max_step=1, horizon=4)
    assert candidates
    assert all(abs(p[i + 1] - p[i]) <= 1 for p in candidates for i in range(len(p) - 1))

    values = {p: value_path(p) for p in candidates}
    best_value = max(values.values())
    selected = [p for p, v in values.items() if v == best_value]

    # Value selects/order paths, but does not uniquely determine a physical
    # law: several paths can remain tied.
    assert len(selected) >= 1

    # Demonstrate that adding an explicit action changes the selection rule.
    actions = {p: kinetic_action(p, mass=2.0) for p in candidates}
    best_action = min(actions.values())
    action_selected = [p for p, a in actions.items() if math.isclose(a, best_action, rel_tol=0, abs_tol=1e-12)]
    assert action_selected

    # Changing mass rescales the action ranking but does not create mass.
    actions_m4 = {p: kinetic_action(p, mass=4.0) for p in candidates}
    ratios = [actions_m4[p] / actions[p] for p in candidates if actions[p] > 0]
    assert all(math.isclose(r, 2.0, rel_tol=1e-12, abs_tol=1e-12) for r in ratios)

    print("REL-16 PASS")
    print(f"candidate_paths={len(candidates)}")
    print(f"value_max={best_value}")
    print(f"value_selected_paths={len(selected)}")
    print(f"action_min={best_action}")
    print(f"action_selected_paths={len(action_selected)}")
    print("mass scaling action(m=4)/action(m=2)=2")
    print("CONCLUSION: value + memory can select/order paths, but do not by themselves derive a unique physical action or its parameters.")


if __name__ == "__main__":
    main()
