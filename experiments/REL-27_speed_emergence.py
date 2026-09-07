"""REL-27 — numerical scale test for emergent relational speed."""


def bound(R, ell, tau):
    return R * ell / tau


def run():
    R = 2
    baseline = bound(R, 1.0, 0.5)
    length_scaled = bound(R, 3.0, 0.5)
    time_scaled = bound(R, 1.0, 1.0)
    both_scaled = bound(R, 5.0, 2.5)

    result = {
        "baseline": baseline,
        "length_scaled": length_scaled,
        "time_scaled": time_scaled,
        "both_scaled": both_scaled,
        "scale_invariance_when_a_equals_b": both_scaled == baseline,
        "conclusion": (
            "Relational reach fixes a finite bound only in relational units; "
            "the numerical speed requires a relation between length and time scales."
        ),
    }
    print(result)
    return result


if __name__ == "__main__":
    run()
