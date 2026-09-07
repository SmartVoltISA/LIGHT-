"""REL-21 — relational requirements and metric countermodels.

Question:
Can DISTINCTION + RELATION + ORDER + BOUNDARY + LOCALITY alone select
Lorentzian spacetime / a finite invariant propagation speed?

Result:
No. A Galilean countermodel satisfies the weak relational requirements while
lacking a nonzero finite invariant speed. Lorentz transformations preserve the
Minkowski interval to numerical precision, but the Lorentzian structure enters
as an additional kinematic/causal constraint rather than being derived from the
weak relational requirements alone.
"""

import math


def lorentz_transform(t, x, v, c=1.0):
    gamma = 1.0 / math.sqrt(1.0 - (v / c) ** 2)
    return gamma * (t - v * x / c**2), gamma * (x - v * t)


def minkowski_interval(t, x, c=1.0):
    return c**2 * t**2 - x**2


def run():
    # Positive control: Lorentz transformations preserve the Minkowski interval.
    lorentz_errors = []
    samples = [(0.3, 0.1), (1.2, 0.4), (-0.7, 0.9)]
    boosts = [0.2, 0.5, 0.8]
    for v in boosts:
        for t, x in samples:
            tp, xp = lorentz_transform(t, x, v)
            lorentz_errors.append(
                abs(minkowski_interval(t, x) - minkowski_interval(tp, xp))
            )

    # Countermodel: Galilean transformations preserve absolute time and admit
    # local ordered propagation, but u' = u - v, so no nonzero finite speed is invariant.
    galilean_speed_changes = []
    speeds = [-2.0, -1.0, 0.5, 1.0, 3.0]
    for v in [0.2, 0.7]:
        for u in speeds:
            u_prime = u - v
            galilean_speed_changes.append(abs(u_prime - u))

    result = {
        "lorentz_max_interval_error": max(lorentz_errors),
        "galilean_max_speed_change": max(galilean_speed_changes),
        "conclusion": (
            "Weak relational requirements do not uniquely select Lorentzian geometry. "
            "A finite invariant speed / causal-cone structure is an additional constraint."
        ),
    }
    print(result)
    return result


if __name__ == "__main__":
    run()
