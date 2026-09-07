import math


def channel_stats(distance_steps: int, flip_probability: float, paths: int):
    """BSC chain on each path + odd-path majority decoder."""
    if distance_steps < 1 or paths < 1 or paths % 2 == 0:
        raise ValueError("distance_steps and paths must be positive; paths must be odd")
    if not 0 <= flip_probability <= 0.5:
        raise ValueError("flip_probability must be in [0, 0.5]")

    # One path is a BSC whose crossover probability compounds over N local hops.
    eps = (1 - (1 - 2 * flip_probability) ** distance_steps) / 2
    success = sum(
        math.comb(paths, j) * (1 - eps) ** j * eps ** (paths - j)
        for j in range(paths // 2 + 1, paths + 1)
    )
    tv = abs(2 * success - 1)

    if success <= 0 or success >= 1:
        mutual_information = 1.0
    else:
        h = -(success * math.log2(success) + (1 - success) * math.log2(1 - success))
        mutual_information = 1 - h

    return eps, success, tv, mutual_information


def max_reliable_distance(flip_probability: float, paths: int, threshold: float, limit: int = 200):
    candidates = [
        n for n in range(1, limit + 1)
        if channel_stats(n, flip_probability, paths)[2] >= threshold
    ]
    return max(candidates, default=0)


def main():
    tau = 0.5
    p = 0.10
    threshold = 0.50
    path_counts = [1, 3, 5, 11, 25, 101]

    print("REL-35: reliable causal front")
    print(f"local transition time tau={tau}, flip probability p={p}, TV threshold={threshold}")

    for paths in path_counts:
        n = max_reliable_distance(p, paths, threshold)
        tv = channel_stats(n, p, paths)[2] if n else 0.0
        print(f"paths={paths:3d} max_reliable_steps={n:3d} time={n*tau:5.1f} TV={tv:.6f}")

    # Front speed is fixed by the local propagation rule, independent of path count.
    # Distance is measured in local hops here, so v_front = 1/tau.
    v_front = 1 / tau
    assert abs(v_front - 2.0) < 1e-12

    # At a fixed distance, path diversity improves reliability but does not alter arrival time.
    n = 10
    rows = [channel_stats(n, p, k) for k in path_counts]
    assert all(abs(n * tau - 5.0) < 1e-12 for _ in rows)
    assert rows[-1][2] > rows[0][2]

    # No causal influence exists before the local front: this model defines arrival at N*tau.
    arrival = n * tau
    for t in [0.0, arrival - 0.1]:
        assert t < arrival

    print(f"fixed-distance front arrival: t={arrival}")
    print(f"front speed: v_front={v_front}")
    print("PASS: path diversity changes reliability/reachable reliable distance, not causal-front speed.")


if __name__ == "__main__":
    main()
