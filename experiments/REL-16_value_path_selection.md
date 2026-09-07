# REL-16 — Value / Path Selection

Date: 2026-09-07
Status: COMPLETED — structural negative-boundary result

## Question

Can an abstract value rule, together with memory-imposed admissibility constraints, select a path, and does that selection alone determine a physical action/dynamics?

## Minimal architecture

`WILL → MEMORY → VALUE → CHOICE → PATH`

Memory is represented by a local transition constraint `|Δx| ≤ 1` per step. This produces a finite set of admissible paths from an initial state to a target.

Value is represented independently as:

`V(P) = − Σ |Δx|`

Choice selects paths with maximal value.

A separate physical action candidate is then supplied:

`S(P) = Σ 1/2 m v² Δt`

The coefficient `m` is deliberately an external input.

## Numerical result

For the test from `x=0` to `x=2` in four steps with `|Δx|≤1`:

- admissible paths: `10`;
- maximal abstract value: `−2`;
- paths tied for maximal value: `6`;
- minimum supplied kinetic action for `m=2`: `2`;
- paths tied for minimum kinetic action: `6`;
- changing `m` from `2` to `4` scales every nonzero kinetic-action value by exactly `2`.

The implementation is deterministic and the analytical checks pass.

## Interpretation

The test supports three separate statements:

1. MEMORY/constraints can reduce the space of possible paths.
2. VALUE can order admissible paths and therefore participate in CHOICE.
3. VALUE alone does not determine a unique physical law, a physical action functional, or the numerical parameter `m`.

This is an important negative boundary. A generic value rule can select among already-defined possibilities, but it does not automatically generate the metric, time dependence, kinetic structure, mass parameter, locality, symmetry or conservation laws required by physical dynamics.

## Relation to physical action

The structural analogy is:

`VALUE(P)` → evaluates/orders paths

`S(P)` → physical action functional over paths

But:

`VALUE ≠ S`

and

`CHOICE ≠ δS = 0`

without additional assumptions.

The correct physical statement is the principle of stationary action. It must not be redefined as generic maximization of value.

## Result

`WILL + MEMORY + VALUE → PATH SELECTION` is structurally viable.

`WILL + MEMORY + VALUE → UNIQUE PHYSICAL DYNAMICS` is **not demonstrated**.

The next research target is therefore not to equate value with action, but to determine the minimum additional structure required for a path-selection rule to become a physical variational principle while preserving locality, symmetry and conservation constraints.
