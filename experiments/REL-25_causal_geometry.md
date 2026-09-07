# REL-25 — Causal cone → Lorentzian geometry

Date: 2026-09-07
Status: COMPLETED — conditional structural result with negative controls

## Question

Does a finite invariant causal cone distinguish Lorentzian structure from Euclidean and Galilean countermodels?

## Fixed input

A finite invariant propagation speed `c` is supplied. This experiment does **not** derive the numerical value of `c` or the existence of the cone.

## Positive control

For a 1+1-dimensional Lorentz boost

`x' = γ(x-vt)`

`t' = γ(t-vx/c²)`

with `γ = 1/sqrt(1-v²/c²)`, the null lines `x=±ct` remain null and the interval

`s² = c²t²-x²`

is preserved.

## Negative controls

### Euclidean

The positive-definite form

`r²=t²+x²`

is not preserved by the Lorentz boost. Therefore Euclidean geometry cannot represent the same invariant finite causal cone.

### Galilean

Under `x'=x-vt`, a signal velocity transforms as

`u'=u-v`.

Therefore no nonzero finite speed is invariant under arbitrary Galilean boosts.

## Numerical result

The implementation gives Lorentz cone/interval errors at floating-point precision, while the Euclidean and Galilean controls show nonzero violations.

## Structural result

`FINITE INVARIANT CAUSAL CONE + RELATIVITY + LINEARITY/RECIPROCITY`

`→ LORENTZ TRANSFORMATIONS`

`→ LORENTZIAN INTERVAL`

The causal cone determines the conformal/causal class of the Lorentzian structure, but an overall metric scale remains undetermined.

## Critical boundary

This does **not** derive:

- finite bounded influence from Ω primitives;
- the existence of an invariant cone;
- the numerical value of `c`;
- spacetime dimension;
- the Lorentzian signature independently of the causal-cone assumption;
- the physical metric scale.

Thus REL-25 strengthens the conditional chain but does not close the fundamental origin of `c`.

## Ω interpretation

The geometry problem separates into two distinct questions:

1. `RELATION → PATH → DISTANCE → GEOMETRY`
2. `BOUNDED INFLUENCE → CAUSAL CONE → LORENTZIAN GEOMETRY`

REL-24 addresses the first at the discrete metric level. REL-25 addresses the second conditionally.

The unresolved arrow remains:

`Ω primitives → BOUNDED INFLUENCE`.

That is the next fundamental target.
