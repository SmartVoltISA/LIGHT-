import math

# REL-36: continuum refinement audit.
# Local hop: spatial scale ell, temporal scale tau.
# Characteristic front speed is v = ell/tau.
# Refinement should preserve v only when ell and tau are scaled together.

CASES = [
    (1.0, 1.0),
    (0.5, 0.5),
    (0.25, 0.25),
    (0.125, 0.125),
    (0.0625, 0.0625),
]

DRIFT = [
    (1.0, 1.0),
    (0.5, 0.25),
    (0.25, 0.0625),
]


def speed(ell, tau):
    return ell / tau


def run():
    print("REL-36 continuum refinement")
    print("matched refinement: ell/tau constant")
    base = speed(*CASES[0])
    for ell, tau in CASES:
        v = speed(ell, tau)
        print(f"ell={ell:g}, tau={tau:g}, v={v:.12g}, drift={v-base:.3g}")
        assert abs(v - base) < 1e-12

    print("\nindependent scaling: ell/tau changes")
    values = []
    for ell, tau in DRIFT:
        v = speed(ell, tau)
        values.append(v)
        print(f"ell={ell:g}, tau={tau:g}, v={v:.12g}")
    assert values == [1.0, 2.0, 4.0]

    # No physical c is inserted. The experiment only tests scale covariance.
    print("\nRESULT: finite characteristic speed survives refinement only when spatial and temporal scales are locked.")
    print("BOUNDARY: numerical speed remains an input scale ratio; no derivation of physical c.")


if __name__ == "__main__":
    run()
