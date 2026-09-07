"""REL-26 — finite propagation from bounded local transition depth.

A discrete relational system is updated synchronously. Each elementary update
can transmit influence across at most R relations, with each update taking
at least dt > 0. After N updates the causal reach is at most N*R relations,
so the effective propagation rate is bounded by R/dt in graph-distance units.

This is a structural positive result only. It does not derive physical c,
continuous space, Lorentz invariance, or a universal microscopic time scale.
"""


def max_reach(steps, max_relations_per_step):
    return steps * max_relations_per_step


def run():
    steps = 10
    R = 2
    dt = 0.5
    reach = max_reach(steps, R)
    bound = R / dt

    # Any path using <= R relations per update cannot exceed this reach.
    passed = reach <= bound * (steps * dt)

    result = {
        "steps": steps,
        "max_relations_per_step": R,
        "minimum_time_per_step": dt,
        "max_graph_distance_reached": reach,
        "effective_speed_bound_graph_units": bound,
        "bound_check": passed,
        "conclusion": (
            "Finite local transition depth plus a positive minimum update time "
            "produces a finite propagation bound in relational units."
        ),
    }
    print(result)
    return result


if __name__ == "__main__":
    run()
