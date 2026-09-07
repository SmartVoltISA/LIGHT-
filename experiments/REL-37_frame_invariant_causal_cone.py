import math

# REL-37: 1+1D causal-cone audit.
# We compare Galilean and Lorentz transformations against the same finite cone.
# A finite invariant speed is imposed as a structural constraint for the Lorentz test;
# this experiment checks what follows from that constraint, not its physical origin.

C = 1.0


def lorentz(x, t, v):
    g = 1.0 / math.sqrt(1.0 - v * v / (C * C))
    return g * (x - v * t), g * (t - v * x / (C * C))


def galilean(x, t, v):
    return x - v * t, t


def cone_residual(x, t):
    return x * x - C * C * t * t


def run():
    speeds = [-0.8, -0.3, 0.2, 0.7]
    for v in speeds:
        assert abs(v) < C
        for s in (-1.0, 1.0):
            x, t = s * C, 1.0
            xp, tp = lorentz(x, t, v)
            assert abs(cone_residual(xp, tp)) < 1e-12

    # Galilean control: a lightlike trajectory is generally not invariant.
    galilean_residuals = []
    for v in speeds:
        x, t = C, 1.0
        xp, tp = galilean(x, t, v)
        galilean_residuals.append(abs(cone_residual(xp, tp)))
    assert max(galilean_residuals) > 1e-6

    # Reciprocity/inverse check for Lorentz transformations.
    for v in speeds:
        x, t = 1.7, 2.3
        xp, tp = lorentz(x, t, v)
        xr, tr = lorentz(xp, tp, -v)
        assert abs(xr - x) < 1e-12
        assert abs(tr - t) < 1e-12

    print("REL-37 RESULT")
    print("Lorentz: finite cone invariant and inverse-consistent.")
    print("Galilean: same finite cone is not frame invariant.")
    print("CONCLUSION: finite invariant causal cone + reciprocity selects Lorentz-type kinematics in this 1+1D linear model.")
    print("BOUNDARY: invariant speed C is an input; its physical value and origin are not derived.")


if __name__ == "__main__":
    run()
