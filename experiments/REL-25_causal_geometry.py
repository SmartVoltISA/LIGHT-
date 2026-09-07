"""REL-25 — causal cone selection of Lorentzian structure.

Tests whether a finite invariant causal cone is compatible with, and strongly
restricts, the geometry relative to Euclidean and Galilean countermodels.
The finite invariant speed c is explicitly supplied; it is NOT derived here.
"""
import math


def lorentz(t, x, v, c=1.0):
    g = 1.0 / math.sqrt(1.0 - (v / c) ** 2)
    return g * (t - v * x / c**2), g * (x - v * t)


def minkowski(t, x, c=1.0):
    return c**2 * t**2 - x**2


def euclidean(t, x):
    return t * t + x * x


def galilean(t, x, v):
    return t, x - v * t


def run():
    c = 1.0
    v = 0.6
    samples = [(1.2, 0.4), (0.3, 0.1), (-0.7, 0.9)]

    # Positive control: Lorentz transformations preserve the causal cone and interval.
    null = [(1.0, 1.0), (1.0, -1.0)]
    cone_errors = []
    interval_errors = []
    for t, x in null:
        tp, xp = lorentz(t, x, v, c)
        cone_errors.append(abs(abs(xp / tp) - c))
    for t, x in samples:
        tp, xp = lorentz(t, x, v, c)
        interval_errors.append(abs(minkowski(t, x, c) - minkowski(tp, xp, c)))

    # Negative control 1: Euclidean quadratic form is not preserved by Lorentz boosts.
    euclidean_errors = []
    for t, x in samples:
        tp, xp = lorentz(t, x, v, c)
        euclidean_errors.append(abs(euclidean(tp, xp) - euclidean(t, x)))

    # Negative control 2: Galilean transformation does not preserve a finite nonzero cone.
    galilean_speed_changes = []
    for u in [-2.0, -1.0, 0.5, 1.0, 3.0]:
        up = u - v
        galilean_speed_changes.append(abs(up - u))

    result = {
        "lorentz_max_cone_error": max(cone_errors),
        "lorentz_max_interval_error": max(interval_errors),
        "euclidean_max_error_under_lorentz": max(euclidean_errors),
        "galilean_max_speed_change": max(galilean_speed_changes),
        "conclusion": (
            "Given a finite invariant causal cone, Lorentzian interval structure is "
            "compatible and the tested Euclidean/Galilean alternatives fail the same "
            "invariance requirement. The cone scale c remains an external input."
        ),
    }
    print(result)
    return result


if __name__ == "__main__":
    run()
