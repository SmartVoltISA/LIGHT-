"""REL-22 — invariant causal cone to Lorentz transformation.

Conditional derivation:
linearity + relativity of inertial frames + isotropy/reciprocity + a finite
invariant signal speed c constrain the 1+1 transformation to the Lorentz form.
The value of c is supplied; this experiment does not derive c.
"""

import math


def lorentz_from_cone(v, c=1.0):
    """Construct coefficients from preservation of x=±ct and reciprocity."""
    gamma = 1.0 / math.sqrt(1.0 - (v / c) ** 2)
    a = gamma
    d = -gamma * v / c**2
    b = c**2 * d
    e = a
    return a, b, d, e


def transform(t, x, v, c=1.0):
    a, b, d, e = lorentz_from_cone(v, c)
    return a * x + b * t, d * x + e * t


def run():
    c = 1.0
    max_light_cone_error = 0.0
    max_interval_error = 0.0

    for v in [0.1, 0.3, 0.6, 0.8]:
        for sign in [-1.0, 1.0]:
            t = 1.37
            x = sign * c * t
            xp, tp = transform(t, x, v, c)
            max_light_cone_error = max(max_light_cone_error, abs(xp - sign * c * tp))

        for t, x in [(0.4, 0.1), (1.1, 0.3), (-0.8, 0.9)]:
            xp, tp = transform(t, x, v, c)
            old = c**2 * t**2 - x**2
            new = c**2 * tp**2 - xp**2
            max_interval_error = max(max_interval_error, abs(old - new))

    print({
        "max_light_cone_error": max_light_cone_error,
        "max_interval_error": max_interval_error,
        "status": "conditional support: invariant finite cone + linear inertial transformations -> Lorentz form; c remains input",
    })


if __name__ == "__main__":
    run()
