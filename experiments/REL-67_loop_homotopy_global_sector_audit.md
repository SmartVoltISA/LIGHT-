# REL-67 — Loop composition → homotopy-like global sectors

## Question

Can nontrivial global loop sectors arise from relation composition plus a local
path-equivalence rule, or must topology be inserted independently?

## Construction

A walk is represented by oriented edges. The local equivalence rule cancels
immediate inverse traversals:

`e · e^-1 -> identity`.

Two cases are tested.

### Tree

A closed walk can be reduced completely by repeated local backtracking
cancellation.

`closed walk -> identity`.

### Ring

A full winding around the ring has no adjacent inverse pair and therefore
survives the same local reduction.

`winding +1`, `winding +2`, `winding -1`

remain distinct reduced sectors.

A winding followed by its exact inverse reduces to the identity.

## Result

Conditional structural chain:

`RELATION`
→ `COMPOSABLE PATH`
→ `LOOP`
→ `LOCAL PATH EQUIVALENCE`
→ `REDUCED LOOP CLASS`
→ `GLOBAL SECTOR`.

Thus a homotopy-like distinction can emerge from path composition and an
explicitly local cancellation rule.

## Critical boundary

The ring and tree differ in a global property: the ring contains a
noncontractible cycle while the tree does not.

Therefore the experiment does **not** derive topology from local relation
algebra alone.

What is derived conditionally is narrower:

`given a path space + composition + local equivalence`
→ `global loop classes`.

The existence of noncontractible cycles remains encoded in global connectivity
/topology.

## Relation to REL-66

REL-66 showed that closed-path composition can produce a gauge-invariant global
holonomy candidate.

REL-67 now shows how distinct loop sectors can arise before assigning any
numerical phase to the loop:

`path class`
→ `sector`
→ `possible global memory`.

The numerical holonomy/phase is an additional structure on those sectors.

## Status

**CONDITIONAL POSITIVE + TOPOLOGICAL BOUNDARY.**

Positive: local composition/equivalence can classify surviving global loop
sectors.

Boundary: the existence and global connectivity of noncontractible cycles are
not derived from local cancellation alone.
