# REL-32 — Memory, path diversity, and controllable signal speed

Date: 2026-09-07
Status: COMPLETED — toy-model separation test

## Question

Can memory and diversity of available paths change the relational/correlation structure without changing the maximum speed of controllable information transfer?

## Construction

Use a line of sites with local updates. Every causal update crosses at most `R` edges and consumes at least `tau` time.

The system also carries an internal memory state `M`. Memory changes the set of admissible paths but does not itself transmit a new intervention from A to B.

Define:

`P(M)` — admissible paths under memory state M

`D(M) = |P(M)|` — path diversity

`T_signal(A→B)` — earliest time at which an intervention at A can affect a decoder at B.

The causal bound is determined by the maximum local reach and minimum update time:

`T_signal >= ceil(D/R) tau`

for graph distance `D`.

Therefore changing `P(M)` or `D(M)` can alter the number and structure of routes while leaving the causal speed bound unchanged, provided `R` and `tau` are unchanged.

## Toy test

Two memory states are constructed over the same endpoints.

Memory state M1 permits one admissible shortest route.

Memory state M2 permits many admissible routes, including detours, while preserving the same local reach `R=2` and transition time `tau=0.5`.

For endpoint distance `D=10`:

`T_min = ceil(10/2)*0.5 = 2.5`

and therefore

`v_max = 10/2.5 = 4`.

Increasing path diversity does not reduce the minimum causal time below 2.5 in this local-update model.

## Information test

A controllable bit is injected only at A after initialization. A decoder at B can depend on that bit only after a causal update chain reaches B.

Pre-existing correlation between A and B is not counted as transferred information because it is present before the intervention.

Thus:

`pre-existing correlation != intervention-dependent information`.

## Result

**POSITIVE STRUCTURAL RESULT:**

Memory and path diversity can modify the accessible relational structure while the maximum controllable signal speed remains fixed by local reach and transition time.

The same causal speed can coexist with different numbers of available paths.

## Stronger interpretation

This gives a precise version of the hypothesis:

`MEMORY → PATH SPACE`

can change faster or more globally at the structural-description level than

`INTERVENTION → CAUSAL STATE CHANGE`.

But this does NOT establish a physical process in which a real relation propagates faster than light.

## Critical boundary

The toy model does not establish superluminal physical influence, quantum nonlocal signaling, or any violation of relativity.

It only proves that an ontology can represent:

`RELATIONAL STRUCTURE`

and

`CONTROLLABLE CAUSAL TRANSFER`

as different variables.

## Candidate Ω chain

`MEMORY → CONSTRAINTS → ACCESSIBLE PATH SPACE → CHOICE`

while independently

`LOCAL REACH + POSITIVE TRANSITION TIME → BOUNDED CAUSAL TRANSFER`.

The next physical target is to replace the toy graph by an operational information-theoretic model and explicitly calculate intervention-dependent mutual information outside the causal cone.
