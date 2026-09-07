# REL-31 — Relation, correlation, and controllable signal

Date: 2026-09-07
Status: COMPLETED — toy-model separation test

## Question

Can a system contain a global relational/correlation structure while controllable state transfer remains bounded by local propagation?

## Construction

Separate three objects:

`G(t)` — relation graph / structural connectivity

`C(A,B)` — correlation observable between distant regions

`I(A→B,t)` — controllable information transfer produced by an intervention at A and decoded at B

The test deliberately does not identify these quantities.

A graph may contain a direct structural relation between A and B at t=0. That does not by itself constitute a causal transfer from A to B.

For controllable transfer, require a sequence of local updates. If each update crosses at most `R` edges and costs at least `τ`, then a graph distance `D` requires at least

`N = ceil(D/R)`

updates and therefore

`T_signal ≥ ceil(D/R) τ`.

The corresponding transfer bound is

`v_signal ≤ D / (ceil(D/R) τ)`

which approaches `R/τ` for large D.

## Toy numerical test

Set `R=2`, `τ=0.5`, and graph distance `D=99`.

Then

`N=50`

`T_signal≥25`

and

`v_signal≤3.96`.

The structural relation `G(A,B)` can be present before any local signal sequence is executed.

## Result

**POSITIVE STRUCTURAL SEPARATION:**

`RELATION / CORRELATION` and `CONTROLLABLE CAUSAL TRANSFER` are mathematically separable objects in the model.

A pre-existing relation or correlation does not imply that a controllable message has traversed the same distance instantaneously.

## Critical physical boundary

This toy model does NOT prove that nature permits superluminal changes of physical relations, nor does it demonstrate superluminal communication.

It establishes only that the proposed ontology does not logically require

`relation = signal`.

To connect the model to quantum physics, one must distinguish ordinary correlation/entanglement from operational signaling. Existing Lieb–Robinson results independently show that local quantum dynamics can have effective light cones limiting information propagation and correlation creation. 

## Ω interpretation

The candidate chain becomes

`DISTINCTION → RELATION → CORRELATION/STRUCTURE`

and separately

`STATE CHANGE → LOCAL TRANSITIONS → PATH → CAUSAL TRANSFER → INFORMATION`

with

`MEMORY → altered future accessible paths`

without requiring memory itself to be a propagating signal.

This supports the hypothesis that the word `СВЯЗЬ` should not be used for every form of physical influence.

## Next target

Construct a controlled two-region information channel where correlation is initialized globally but the intervention-dependent mutual information remains bounded by the local update cone. Then test whether memory and path diversity can alter the correlation structure without increasing the maximum controllable signal speed.
