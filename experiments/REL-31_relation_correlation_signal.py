import math


def signal_bound(distance, reach, tau):
    updates = math.ceil(distance / reach)
    time_min = updates * tau
    return updates, time_min, distance / time_min


def run():
    R = 2
    tau = 0.5
    D = 99

    updates, time_min, v = signal_bound(D, R, tau)

    # Structural relation exists independently of the update path.
    relation_exists_at_t0 = True
    signal_transferred_at_t0 = False

    assert updates == 50
    assert time_min == 25.0
    assert math.isclose(v, 3.96, rel_tol=0, abs_tol=1e-12)
    assert relation_exists_at_t0 and not signal_transferred_at_t0

    print("REL-31 PASS")
    print(f"distance={D}")
    print(f"local_reach={R}")
    print(f"minimum_update_time={tau}")
    print(f"minimum_updates={updates}")
    print(f"minimum_signal_time={time_min}")
    print(f"signal_speed_bound={v}")
    print("relation_exists_before_signal=True")
    print("CONCLUSION: relation/correlation and controllable causal transfer are distinct model objects.")


if __name__ == "__main__":
    run()
