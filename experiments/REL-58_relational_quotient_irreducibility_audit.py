"""REL-58: relational equivalence quotient and irreducibility audit.

Question:
Can quotienting states that are indistinguishable by relations, retained
history, and future admissible transitions force irreducible physical blocks?

This is deliberately a countermodel-seeking audit.  We construct:
1. a duplicated representation with two copies having identical relational
   behavior;
2. a relationally enriched representation where the copies are distinguished
   by an independent retained trace;
3. the quotient by the proposed equivalence relation.

The experiment checks that quotienting removes exact duplicates, but does NOT
silently promote quotienting into a theorem that every quotient block is an
irreducible representation. A separate reducible-but-nonduplicate model is
included as a negative control.
"""

import numpy as np


def canonical_signature(state, history, future):
    return (
        tuple(np.round(state, 12)),
        tuple(np.round(history, 12)),
        tuple(sorted(tuple(np.round(x, 12)) for x in future)),
    )


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
    future = [tuple(np.round((A @ x), 12)), tuple(np.round((-A @ x), 12))]
    sig = canonical_signature(x, history, future)
    return [sig, sig]


def reducible_nonduplicate_model():
    """Direct sum with two distinguishable invariant sectors.

    The two states have different retained traces and future behavior, so the
    relational quotient must not identify them merely because the dynamics
    share the same operator.
    """
    A = np.array([[0.0, 1.0], [-1.0, 0.0]])
    states = [np.array([1.0, 0.0]), np.array([2.0, 0.0])]
    traces = [0.0, 1.0]
    signatures = []
    for x, tr in zip(states, traces):
        history = [x.copy(), (A @ x).copy()]
        future = [tuple(np.round(A @ x, 12)), tuple(np.round((-A) @ x, 12))]
        signatures.append(canonical_signature(x, history + [np.array([tr])], future))
    return signatures


def main():
    dup = duplicated_model()
    dup_classes = quotient_classes(dup)
    assert len(dup_classes) == 1, "Exact relational duplicates were not quotiented."
    assert dup_classes[0] == [0, 1]

    red = reducible_nonduplicate_model()
    red_classes = quotient_classes(red)
    assert len(red_classes) == 2, "Distinct relational sectors were incorrectly identified."

    # Negative-control statement: quotienting alone cannot establish
    # irreducibility. The reducible model is deliberately non-identical at the
    # relational level, so the quotient leaves both sectors present.
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
