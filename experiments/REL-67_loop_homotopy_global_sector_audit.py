"""REL-67 — loop homotopy / global-sector audit.

Countermodel-seeking finite graph experiment. Build two graph geometries:
A) a tree, where every closed walk is reducible by backtracking;
B) a ring, where one noncontractible cycle remains after local backtracking
reduction.

The test asks whether global loop sectors can be generated from relation
composition plus an equivalence rule that cancels immediate backtracking.
It does not assume a continuum manifold or invoke formal homotopy theory.
"""

from collections import deque


def reduce_walk(walk):
    stack = []
    for edge in walk:
        if stack and stack[-1] == -edge:
            stack.pop()
        else:
            stack.append(edge)
    return tuple(stack)


def ring_walk(n, winding):
    step = 1 if winding >= 0 else -1
    return (step,) * (n * abs(winding))


def tree_closed_walk():
    # 0 -> 1 -> 2 -> 1 -> 0: entirely reducible by local backtracking.
    return (1, 1, -1, -1)


def main():
    tree = tree_closed_walk()
    assert reduce_walk(tree) == ()

    # On a ring, local backtracking reduction cannot remove a full winding.
    ring_once = ring_walk(6, 1)
    ring_twice = ring_walk(6, 2)
    ring_reverse = ring_walk(6, -1)

    assert reduce_walk(ring_once) == ring_once
    assert reduce_walk(ring_twice) == ring_twice
    assert reduce_walk(ring_reverse) == ring_reverse

    # Distinct winding sectors survive the local equivalence.
    assert reduce_walk(ring_once) != reduce_walk(ring_twice)
    assert reduce_walk(ring_once) != reduce_walk(ring_reverse)

    # A path followed by its inverse is contractible under the same rule.
    inverse_pair = ring_once + tuple(-x for x in reversed(ring_once))
    assert reduce_walk(inverse_pair) == ()

    print("REL-67 loop homotopy global sector audit")
    print(f"tree closed walk reduced form: {reduce_walk(tree)}")
    print(f"ring winding +1 reduced form length: {len(reduce_walk(ring_once))}")
    print(f"ring winding +2 reduced form length: {len(reduce_walk(ring_twice))}")
    print(f"ring winding -1 reduced form length: {len(reduce_walk(ring_reverse))}")
    print("RESULT: relation composition + local backtracking equivalence distinguishes noncontractible winding sectors in the ring model.")
    print("NEGATIVE CONTROL: all tree closed walks generated here reduce to the trivial sector.")
    print("BOUNDARY: the existence of a noncontractible cycle is a global connectivity/topology property; local cancellation does not derive it.")


if __name__ == "__main__":
    main()
