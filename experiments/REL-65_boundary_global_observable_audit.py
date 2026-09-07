"""REL-65: boundary/history/global structure -> observable content.

Countermodel-seeking audit. A finite ring has a local state on each site and a
single global holonomy-like label H. Local observations cannot recover H, while
a closed-loop operation can. History may retain H as a persistent invariant.

The test asks whether boundary/global observability follows from relation,
history and local causal structure, or whether admissible global operations /
boundary structure are an additional input.
"""

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class State:
    local: Tuple[int, ...]
    global_label: int


def local_observation(s: State) -> Tuple[int, ...]:
    return s.local


def loop_observation(s: State) -> int:
    return s.global_label


def evolve_local(s: State, site: int, delta: int) -> State:
    x = list(s.local)
    x[site] += delta
    return State(tuple(x), s.global_label)


def main():
    a = State((0, 0, 0, 0), 0)
    b = State((0, 0, 0, 0), 1)

    # Local algebra cannot distinguish the two global sectors.
    assert local_observation(a) == local_observation(b)

    # A closed-loop/global operation does distinguish them.
    assert loop_observation(a) != loop_observation(b)

    # Local evolution preserves the global label: history retains a constraint.
    a2 = evolve_local(a, 1, 1)
    b2 = evolve_local(b, 1, 1)
    assert a2.global_label == a.global_label
    assert b2.global_label == b.global_label

    # Same local history, different global history => global sector remains
    # physically distinguishable once the admissible loop operation is allowed.
    assert local_observation(a2) == local_observation(b2)
    assert loop_observation(a2) != loop_observation(b2)

    print("REL-65 boundary/global observable audit")
    print("local observations: global sectors indistinguishable")
    print("loop/global operation: global sectors distinguishable")
    print("local evolution: global label retained as history/constraint")
    print("RESULT: global observable content cannot be reconstructed from local observations alone.")
    print("CONDITIONAL POSITIVE: if closed-loop/global operations are admitted, retained global structure becomes observable.")
    print("BOUNDARY: admissibility of global operations and boundary/global structure is an additional physical input; it is not derived from local causality alone.")


if __name__ == "__main__":
    main()
