"""REL-24 — relation/path construction of discrete metric."""


def shortest_path_metric(n, edges):
    inf = 10**9
    d = [[inf] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for a, b in edges:
        d[a][b] = d[b][a] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


def run():
    # Connected relational graph: 0--1--2, with a direct 0--2 relation as well.
    edges = [(0, 1), (1, 2), (0, 2), (2, 3)]
    d = shortest_path_metric(4, edges)

    identity = all(d[i][i] == 0 for i in range(4))
    symmetry = all(d[i][j] == d[j][i] for i in range(4) for j in range(4))
    triangle = all(
        d[i][k] <= d[i][j] + d[j][k]
        for i in range(4)
        for j in range(4)
        for k in range(4)
    )

    result = {
        "distance": d,
        "identity": identity,
        "symmetry": symmetry,
        "triangle_inequality": triangle,
        "metric_pass": identity and symmetry and triangle,
        "conclusion": (
            "Relations + paths + positive shortest-path cost construct a discrete metric; "
            "continuous or Lorentzian physical geometry requires additional structure."
        ),
    }
    print(result)
    return result


if __name__ == "__main__":
    run()
