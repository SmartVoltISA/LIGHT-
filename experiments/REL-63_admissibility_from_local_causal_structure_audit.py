"""REL-63: test whether local causal structure can select observables.

Countermodel-seeking audit. Two relational readouts are considered:
- local x, accessible at the current site;
- hidden, accessible only through a nonlocal/global operation.

A locality filter selects local relations, while a purely future-effect filter
can select both. We therefore test whether adding locality reduces the
observable ambiguity exposed by REL-62.

The result is intentionally conditional: locality selects a narrower family
in this construction, but locality itself is an additional physical principle
and does not uniquely imply a complete quantum observable algebra.
"""

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Relation:
    name: str
    support_distance: int
    changes_future: bool


def local_admissible(r: Relation, radius: int = 1) -> bool:
    return r.support_distance <= radius


def future_relevant(r: Relation) -> bool:
    return r.changes_future


def select(relations: Tuple[Relation, ...], *, locality_radius=None):
    out = [r for r in relations if future_relevant(r)]
    if locality_radius is not None:
        out = [r for r in out if local_admissible(r, locality_radius)]
    return tuple(r.name for r in out)


def main():
    relations = (
        Relation("x_local", 0, True),
        Relation("neighbor", 1, True),
        Relation("hidden_global", 10, True),
        Relation("constant", 0, False),
    )

    future_only = select(relations)
    local_only = select(relations, locality_radius=1)

    assert future_only == ("x_local", "neighbor", "hidden_global")
    assert local_only == ("x_local", "neighbor")
    assert "hidden_global" not in local_only

    # Negative control: a local relation that has no future effect must not be
    # admitted by the combined rule.
    assert "constant" not in local_only

    print("REL-63 admissibility from local causal structure audit")
    print(f"future-effect-only relations: {future_only}")
    print(f"local + future-effect relations: {local_only}")
    print("RESULT: locality removes the explicitly nonlocal counterexample in this model.")
    print("BOUNDARY: locality is an added physical admissibility principle; it does not by itself derive the complete observable algebra.")


if __name__ == "__main__":
    main()
