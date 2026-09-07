from math import ceil, log2


def tv_binary(p0, p1):
    return 0.5 * (abs(p0[0] - p1[0]) + abs(p0[1] - p1[1]))


def mutual_information_binary_joint(joint):
    px = [sum(row) for row in joint]
    py = [sum(joint[x][y] for x in range(2)) for y in range(2)]
    value = 0.0
    for x in range(2):
        for y in range(2):
            p = joint[x][y]
            if p > 0:
                value += p * log2(p / (px[x] * py[y]))
    return value


def run(distance, reach, tau, path_count, max_steps=None):
    steps = ceil(distance / reach)
    if max_steps is None:
        max_steps = steps

    # Initial correlation is created before the intervention:
    # Z is uniform, A=Z, B=Z.  Thus I(Z;B)=1 bit.
    initial_correlation_bits = 1.0

    rows = []
    for k in range(max_steps + 1):
        elapsed = k * tau
        if k < steps:
            # Before causal arrival, B remains the independently prepared Z.
            p_b_do0 = (0.5, 0.5)
            p_b_do1 = (0.5, 0.5)
            joint_uk_b = ((0.25, 0.25), (0.25, 0.25))
        else:
            # After arrival, every active path carries the intervention to B.
            p_b_do0 = (1.0, 0.0)
            p_b_do1 = (0.0, 1.0)
            joint_uk_b = ((0.5, 0.0), (0.0, 0.5))

        causal_tv = tv_binary(p_b_do0, p_b_do1)
        causal_mi_bits = mutual_information_binary_joint(joint_uk_b)
        rows.append((k, elapsed, path_count, causal_tv, causal_mi_bits))

    return initial_correlation_bits, steps, rows


if __name__ == "__main__":
    distance = 10
    reach = 2
    tau = 0.5

    # M1: one admissible path; M2: five parallel admissible paths.
    results = []
    for path_count in (1, 5):
        initial_corr, steps, rows = run(distance, reach, tau, path_count)
        arrival = next(row for row in rows if row[3] > 0)
        results.append((path_count, initial_corr, steps, arrival))

    print("REL-33 intervention causal channel")
    print(f"distance={distance}, reach={reach}, tau={tau}")
    print(f"minimum steps={ceil(distance / reach)}, minimum arrival time={ceil(distance / reach) * tau}")
    for path_count, initial_corr, steps, arrival in results:
        k, elapsed, paths, causal_tv, causal_mi = arrival
        print(
            f"paths={path_count}: initial_correlation={initial_corr:.1f} bit, "
            f"arrival_step={k}, arrival_time={elapsed:.1f}, "
            f"TV={causal_tv:.1f}, causal_MI={causal_mi:.1f} bit"
        )

    assert results[0][3][1] == results[1][3][1]
    assert results[0][3][3] == results[1][3][3] == 1.0
    assert results[0][3][4] == results[1][3][4] == 1.0
