from math import ceil


def signal_bound(distance, reach, tau):
    updates = ceil(distance / reach)
    return updates * tau


def main():
    D = 10
    R = 2
    tau = 0.5

    # Same local causal architecture, different memory-conditioned path spaces.
    memory_states = {
        "M1": ["shortest"],
        "M2": ["shortest", "detour_left", "detour_right", "loop_a", "loop_b"],
    }

    Tmin = signal_bound(D, R, tau)
    vmax = D / Tmin

    assert Tmin == 2.5
    assert vmax == 4.0
    assert len(memory_states["M2"]) > len(memory_states["M1"])

    # Path diversity changes without changing the causal cone.
    print("REL-32 PASS")
    print(f"distance={D}")
    print(f"reach={R}")
    print(f"tau={tau}")
    print(f"minimum_signal_time={Tmin}")
    print(f"maximum_signal_speed={vmax}")
    print(f"M1_path_count={len(memory_states['M1'])}")
    print(f"M2_path_count={len(memory_states['M2'])}")
    print("CONCLUSION: memory/path diversity can change accessible path space without changing the local causal speed bound.")


if __name__ == "__main__":
    main()
