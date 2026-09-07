# REL-22 — Causal-cone constraint to Lorentz structure

Date: 2026-09-07
Status: COMPLETED — conditional derivation

## Question

What follows once a finite invariant causal speed is supplied together with inertial-frame relativity, linearity and reciprocity?

## Assumptions

`finite invariant causal speed c`
`+ relativity of inertial frames`
`+ linear transformations`
`+ reciprocity / isotropy`

No Minkowski interval is assumed as the result.

## Construction

In 1+1 dimensions, let

`x' = A(v)x + B(v)t`
`t' = C(v)x + D(v)t`.

Impose:

- homogeneity and linearity;
- isotropy/reciprocity;
- composition of boosts;
- preservation of the distinguished finite speed `c`.

The null trajectories `x = ±ct` must map to null trajectories. Together with reciprocity and continuity this constrains the boost family to the Lorentz form

`x' = γ(x-vt)`
`t' = γ(t-vx/c²)`

with

`γ = 1/sqrt(1-v²/c²)`.

The preserved quadratic form is

`c²t²-x²`.

## Numerical control

For boosts `v = 0.2, 0.5, 0.8` and several spacetime samples, direct evaluation of the Lorentz transformation gives maximum interval error approximately `1.61e-15`.

## Result

**CONDITIONAL SUPPORT.**

A finite invariant causal cone plus inertial-frame relativity and the stated regularity/symmetry assumptions is sufficient to recover Lorentz transformations and an invariant quadratic interval in the tested 1+1 construction.

## Boundary

REL-22 does NOT derive:

- existence of the finite invariant speed `c`;
- why nature has a causal cone;
- spacetime dimension;
- the metric signature from deeper Ω primitives;
- the numerical value of `c`.

Therefore the safe chain is:

`RELATIONAL STRUCTURE → [UNRESOLVED CAUSAL-CONE PRINCIPLE] → LORENTZ STRUCTURE → INVARIANT INTERVAL`.

This closes a conditional step but not the origin of relativity itself.
