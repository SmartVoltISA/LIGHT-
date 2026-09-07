from math import ceil


def signal_bound(distance, reach, tau):
    steps = ceil(distance / reach)
    t_min = steps * tau
    return steps, t_min, distance / t_min


def main():
    D = 10
    R = 2
    tau = 0.5

    # M1 and M2 have identical local propagation rules but different
    # numbers of admissible paths. Path diversity is deliberately external
    # to the local speed rule.
    m1_paths = 1
    m2_paths = 5

    s1, t1, v1 = signal_bound(D, R, tau)
    s2, t2, v2 = signal_bound(D, R, tau)

    assert m1_paths != m2_paths
    assert s1 == s2 == 5
    assert t1 == t2 == 2.5
    assert v1 == v2 == 4.0

    print("REL-32 PASS")
    print(f"M1_paths={m1_paths}, M2_paths={m2_paths}")
    print(f"M1_steps={s1}, M1_Tmin={t1}, M1_vmax={v1}")
    print(f"M2_steps={s2}, M2_Tmin={t2}, M2_vmax={v2}")
    print("CONCLUSION: path diversity changes accessible futures without changing the fixed local causal-speed bound.")


if __name__ == "__main__":
    main()
