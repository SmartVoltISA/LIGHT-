"""REL-60: observable-algebra selection audit.

Question:
Can an observable algebra be selected from relational data without
postulating observables in advance?

We test three cases:
1. exact duplicate descriptions: must collapse;
2. physically distinguishable relational sector: must remain distinct;
3. reducible algebra with no duplicates: must remain reducible.

The experiment is deliberately conservative. It tests a selection rule for
candidate observables, not a derivation of quantum operator algebras,
gauge groups, or irreducibility.
"""

from dataclasses import dataclass
from typing import Callable, Iterable, List, Tuple


@dataclass(frozen=True)
class State:
    label: str
    relations: Tuple[Tuple[str, int], ...]
    history: Tuple[int, ...]
    futures: Tuple[int, ...]


def signature(s: State):
    return (tuple(sorted(s.relations)), s.history, tuple(sorted(s.futures)))


def quotient(states: Iterable[State]):
    classes = {}
    for s in states:
        classes.setdefault(signature(s), []).append(s)
    return list(classes.values())


def invariant_observables(states: List[State], candidates: List[Callable[[State], int]]):
    """Keep candidate relations that are constant on every quotient class."""
    classes = quotient(states)
    accepted = []
    for obs in candidates:
        if all(len({obs(s) for s in cls}) == 1 for cls in classes):
            accepted.append(obs)
    return accepted


def duplicate_case():
    base = State("A", (("r", 1),), (0, 1), (2, 3))
    dup = State("B", (("r", 1),), (0, 1), (2, 3))
    return [base, dup]


def distinguishable_case():
    a = State("A", (("r", 1), ("trace", 0)), (0, 1), (2, 3))
    b = State("B", (("r", 1), ("trace", 1)), (0, 1), (2, 3))
    return [a, b]


def reducible_case():
    # Two invariant sectors: same dynamics, different retained relational
    # content. They are not redundant copies and must survive the quotient.
    a = State("sector_1", (("sector", 0),), (0, 1), (1, 0))
    b = State("sector_2", (("sector", 1),), (0, 1), (1, 0))
    return [a, b]


def main():
    dup = duplicate_case()
    dclasses = quotient(dup)
    assert len(dclasses) == 1

    dist = distinguishable_case()
    iclasses = quotient(dist)
    assert len(iclasses) == 2

    red = reducible_case()
    rclasses = quotient(red)
    assert len(rclasses) == 2

    # Candidate observables are relational readouts. The first two are
    # invariant under exact duplication; the trace distinguishes physical
    # relational sectors and therefore is retained rather than quotiented.
    candidates = [
        lambda s: dict(s.relations).get("r", -1),
        lambda s: dict(s.relations).get("trace", -1),
        lambda s: dict(s.relations).get("sector", -1),
    ]

    accepted = invariant_observables(dist, candidates)
    assert len(accepted) == 3

    print("REL-60 observable algebra selection audit")
    print(f"exact duplicate input states: {len(dup)}")
    print(f"duplicate quotient classes: {len(dclasses)}")
    print(f"distinguishable relational input states: {len(dist)}")
    print(f"distinguishable quotient classes: {len(iclasses)}")
    print(f"reducible nonduplicate quotient classes: {len(rclasses)}")
    print(f"candidate relational observables surviving quotient: {len(accepted)}")
    print("RESULT: relationally identical descriptions collapse; independent relational content survives.")
    print("BOUNDARY: this does not derive the full quantum observable algebra or irreducibility.")


if __name__ == "__main__":
    main()
