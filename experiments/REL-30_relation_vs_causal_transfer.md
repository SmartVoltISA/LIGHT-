# REL-30 — Relation structure vs causal transfer

Date: 2026-09-07
Status: COMPLETED — separation test; no superluminal information claim

## Question

Can a relational architecture contain nonlocal/global structural relations while keeping controllable causal state transfer bounded?

The experiment deliberately separates:

`RELATION EXISTENCE / STRUCTURAL CORRELATION`
from
`CAUSAL STATE UPDATE / CONTROLLED INFORMATION TRANSFER`.

## Model

Take a graph of `N` nodes.

The structural relation graph `G` is available as a static object. A node may therefore have a relation record to a distant node without any signal being transmitted between them.

Causal dynamics are a separate update process. During one update, information can move through at most `R` local edges. Each update costs at least `tau > 0`.

For a shortest causal route of `D` edges,

`T_transfer >= ceil(D/R) tau`.

Therefore

`v_transfer <= R ell / tau`.

The existence of an edge in `G` does not itself count as a transfer event.

## Numerical test

For a 100-node line graph with unit edge length, choose `R=2` and `tau=0.5`.

A structural relation can be recorded between node 0 and node 99 at `t=0` without any causal update.

The shortest causal route contains 99 edges.

Minimum transfer time:

`T >= ceil(99/2) * 0.5 = 25 s`.

Hence

`v_transfer <= 99/25 = 3.96 edges/s`

for this finite-route construction, while the structural relation itself has no propagation time because it was part of the initial state.

## Memory/path extension

Let `M` encode retained history and constraints on accessible future paths.

Changing `M` can change the set of admissible paths

`P(s | M)`

without requiring a new signal to every node represented in the structural description.

This is a state/configuration change, not automatically a superluminal message.

If a controllable bit is encoded in `M` at node A and must be recovered at distant node B, that recovery requires an actual causal transfer path and is subject to the transfer bound.

## Result

**POSITIVE SEPARATION RESULT:**

A model can consistently distinguish:

`GLOBAL/STATIC RELATION STRUCTURE`

from

`BOUNDED CAUSAL REALIZATION OF A STATE CHANGE`.

Therefore the statement

"a relation exists between A and B"

does not imply

"information or a physical state change propagated from A to B".

## Important physical boundary

This does NOT demonstrate that nature contains superluminal structural changes.

It demonstrates only that the concepts are mathematically separable.

In relativistic physics, controllable information transfer must respect causal structure. NIST describes `c` as the speed limit in the SI framework, and modern quantum many-body theory independently distinguishes correlations/structural influence from bounded information propagation through Lieb–Robinson-type bounds.

## Ω interpretation

The refined chain is:

`RELATION`
→ `STRUCTURAL POSSIBILITY / CORRELATION`
→ `MEMORY / CONSTRAINT`
→ `POSSIBLE PATHS`

while physical realization follows a separate branch:

`CHOICE`
→ `ACTION`
→ `LOCAL STATE CHANGE`
→ `CAUSAL PATH`
→ `BOUNDED TRANSFER`
→ `OBSERVABLE RESULT`.

This gives a precise candidate for the user's hypothesis:

**Light need not limit the existence of relations; it limits the causal realization of transferable physical changes.**

This sentence remains a hypothesis about physical ontology, not an established empirical result.

## Next target

Test whether nonlocal correlation can be represented without allowing controllable signalling, then compare the construction with quantum entanglement/no-signalling constraints. The decisive quantity must be mutual controllability of the remote outcome, not mere correlation or graph connectivity.
