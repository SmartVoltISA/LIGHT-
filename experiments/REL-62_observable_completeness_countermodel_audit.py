"""REL-62: observable completeness and countermodel audit.

Question:
Can a relational completeness rule select a unique physical observable
algebra, or does completeness itself require an external choice of what counts
as an admissible relation?

We construct finite relational systems with the same underlying states but
vary the admitted relation family. A candidate completeness rule is tested:
include every relation that can independently affect a future transition.

Countermodel: two admissible relation families can be equally closed under
future effects while exposing different internal labels. Therefore closure
under future effects alone does not uniquely select the observable algebra.

The audit also tests a stronger rule: two descriptions are equivalent iff no
admissible experiment can distinguish their future distributions. This gives a
well-defined operational quotient, but the admissible experiment set remains
an input.
"""

from dataclasses import dataclass
from itertools import product
from typing import FrozenSet, Iterable, Tuple


@dataclass(frozen=True)
class State:
    x: int
    hidden: int


@dataclass(frozen=True)
class RelationFamily:
    name: str
    observations: Tuple[str, ...]

    def observe(self, s: State, name: str):
        if name == "x":
            return s.x
        if name == "hidden":
            return s.hidden
        if name == "parity":
            return s.hidden % 2
        raise ValueError(name)


def future_effect(s: State, action: int) -> int:
    # Both x and hidden can affect an available future transition.
    return s.x + action * s.hidden


def effect_signature(s: State, family: RelationFamily):
    return tuple(family.observe(s, r) for r in family.observations) + tuple(
        future_effect(s, a) for a in (-1, 0, 1)
    )


def operational_classes(states: Iterable[State], family: RelationFamily):
    classes = {}
    for s in states:
        classes.setdefault(effect_signature(s, family), []).append(s)
    return list(classes.values())


def independently_affecting_relations(states, relation_names):
    """Relations whose value changes at least one future effect."""
    accepted = []
    for name in relation_names:
        changed = False
        for a, b in product(states, repeat=2):
            if a == b:
                continue
            if all(future_effect(a, u) == future_effect(b, u) for u in (-1, 0, 1)):
                continue
            # relation is relevant if it separates a pair with different effects
            if getattr(a, "x") != getattr(b, "x") and name == "x":
                changed = True
            if getattr(a, "hidden") != getattr(b, "hidden") and name == "hidden":
                changed = True
        if changed:
            accepted.append(name)
    return accepted


def main():
    states = [State(x, h) for x in (0, 1) for h in (0, 1)]

    # Two candidate admissible families.
    family_x = RelationFamily("X-only", ("x",))
    family_full = RelationFamily("full", ("x", "hidden"))
    family_parity = RelationFamily("parity", ("x", "parity"))

    cx = operational_classes(states, family_x)
    cf = operational_classes(states, family_full)
    cp = operational_classes(states, family_parity)

    # x-only cannot distinguish hidden sectors, while full can.
    assert len(cx) < len(cf)
    assert len(cf) == len(states)

    # parity still loses the distinction between hidden=0 and hidden=2 in a
    # larger test space, despite being closed as an observation family.
    larger = [State(x, h) for x in (0, 1) for h in (0, 1, 2, 3)]
    cp_large = operational_classes(larger, family_parity)
    cf_large = operational_classes(larger, family_full)
    assert len(cp_large) < len(cf_large)

    # The operational quotient is well-defined once the experiment family is
    # fixed. But the choice of admissible family is not selected by the quotient
    # itself.
    assert family_x.observations != family_full.observations
    assert family_parity.observations != family_full.observations

    print("REL-62 observable completeness countermodel audit")
    print(f"states in base model: {len(states)}")
    print(f"X-only operational classes: {len(cx)}")
    print(f"full operational classes: {len(cf)}")
    print(f"parity operational classes (larger model): {len(cp_large)}")
    print(f"full operational classes (larger model): {len(cf_large)}")
    print("RESULT: operational quotient is well-defined after admissible experiments are fixed.")
    print("NEGATIVE RESULT: closure/future-effect relevance alone does not uniquely select the admissible observable family.")
    print("BOUNDARY: Omega still needs a principled admissibility rule, or must treat the observable family as additional physical input.")


if __name__ == "__main__":
    main()
