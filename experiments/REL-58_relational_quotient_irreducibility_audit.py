"""REL-58: relational equivalence quotient and irreducibility audit."""

import numpy as np


def canonical_signature(state, history, future):
    history_sig = tuple(tuple(np.round(h, 12)) for h in history)
    future_sig = tuple(sorted(tuple(np.round(x, 12)) for x in future))
    return (tuple(np.round(state, 12)), history_sig, future_sig)


def quotient_classes(signatures):
    classes = {}
    for i, sig in enumerate(signatures):
        classes.setdefault(sig, []).append(i)
    return list(classes.values())


def duplicated_model():
    """Two exact copies: same state, history and future transitions."""
    A = np.array([[0.0, 1.0], [-1.0, 0.0]])
    x = np.array([1.0, 0.25])
    history = [x.copy()]
    for _ in range(12):
        x = A @ x
        history.append(x.copy())
    future = [A @ x, -A @ x]
    sig = canonical_signature(x, history, future)
    return [sig, sig]


def reducible_nonduplicate_model():
    """Two invariant sectors with independent retained relational traces."""
    A = np.array([[0.0, 1.0], [-1.0, 0.0]])
    states = [np.array([1.0, 0.0]), np.array([2.0, 0.0])]
    traces = [0.0, 1.0]
    signatures = []
    for x, tr in zip(states, traces):
        history = [x.copy(), (A @ x).copy(), np.array([tr])]
        future = [A @ x, -A @ x]
        signatures.append(canonical_signature(x, history, future))
    return signatures


def main():
    dup = duplicated_model()
    dup_classes = quotient_classes(dup)
    assert dup_classes == [[0, 1]], "Exact relational duplicates were not quotiented."

    red = reducible_nonduplicate_model()
    red_classes = quotient_classes(red)
    assert red_classes == [[0], [1]], "Distinct relational sectors were incorrectly identified."

    quotient_removed_exact_redundancy = len(dup_classes) == 1
    quotient_preserved_distinct_relations = len(red_classes) == 2

    print("REL-58 relational quotient audit")
    print(f"duplicate input blocks: 2")
    print(f"duplicate quotient classes: {len(dup_classes)}")
    print(f"nonduplicate reducible input blocks: 2")
    print(f"nonduplicate quotient classes: {len(red_classes)}")
    print(f"exact redundancy removed: {quotient_removed_exact_redundancy}")
    print(f"distinct relational content preserved: {quotient_preserved_distinct_relations}")
    print("RESULT: quotienting removes relationally identical duplicates, but does not by itself prove irreducibility.")


if __name__ == "__main__":
    main()
