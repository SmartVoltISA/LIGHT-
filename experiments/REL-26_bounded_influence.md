# REL-26 — Bounded local influence → finite propagation bound

Date: 2026-09-07
Status: COMPLETED — structural positive result with explicit physical boundary

## Question

Can finite propagation be obtained without inserting a Lorentzian metric, if the relational dynamics itself has bounded local reach and each elementary transition consumes positive time?

## Construction

Let each elementary update transmit influence across at most `R` relations and require at least `Δt > 0` time per update.

After `N` updates:

`D_max(N) ≤ N R`.

Elapsed time satisfies:

`T ≥ N Δt`.

Therefore:

`D_max/T ≤ R/Δt`.

Thus a finite propagation bound exists in graph-distance units:

`v_bound = R/Δt`.

## Numerical check

For `R=2`, `Δt=0.5`, and `N=10`:

`D_max=20`

`T=5`

`v_bound=4`

and the bound is exactly saturated by the maximal-reach construction.

## Result

**POSITIVE STRUCTURAL RESULT:**

`BOUNDED LOCAL TRANSITION DEPTH + POSITIVE MINIMUM TRANSITION TIME`

`→ FINITE PROPAGATION BOUND`

This gives a concrete mechanism for generating bounded influence rather than assuming a causal speed as a primitive.

## Critical boundary

The result still does NOT derive:

- physical spatial length units;
- physical time units;
- a universal value of `c`;
- frame invariance;
- Lorentz symmetry;
- a continuous spacetime manifold.

The ratio `R/Δt` is a bound in relational units. To become physical `c`, a length scale and time scale must be related, and frame invariance must still be established.

## Important implication

REL-23 showed that LOCALITY alone does not imply bounded influence. REL-26 identifies a stronger sufficient condition:

`LOCALITY + FINITE LOCAL REACH + POSITIVE TIME COST`

`→ BOUNDED INFLUENCE`.

The next question is whether the required `FINITE LOCAL REACH` and `POSITIVE TIME COST` themselves follow from the Ω chain, or remain additional dynamical assumptions.

## Candidate expanded chain

`DISTINCTION → RELATION → STATE → ORDERED TRANSITION → LOCALITY → FINITE LOCAL REACH → POSITIVE TRANSITION COST → BOUNDED INFLUENCE → CAUSAL CONE → LORENTZ`

No claim of physical derivation is made beyond the stated relational model.
