# REL-23 — Origin of bounded causal influence

Date: 2026-09-07
Status: COMPLETED — negative derivation / candidate boundary

## Question

Can a finite causal cone or invariant propagation limit be derived from the weaker Ω requirements

`DISTINCTION + RELATION + ORDER + BOUNDARY + LOCALITY`

without inserting a finite bound by hand?

## Countermodel construction

The same abstract relational requirements admit at least three propagation classes:

1. **Unbounded influence:** a transition at one node may affect arbitrarily distant nodes in one update.
2. **Finite but non-invariant influence:** influence is restricted to a finite neighborhood, but the maximum propagation rate depends on the chosen frame/update rule.
3. **Invariant finite cone:** influence is restricted by a frame-independent finite bound `c`, producing a causal cone.

All three can be described using distinction, relations, ordered transitions, boundaries and local update rules at an abstract level.

## Result

**NEGATIVE DERIVATION RESULT.**

Locality alone is not enough to derive a finite invariant causal speed. Even strengthening locality to bounded graph-neighborhood influence does not, by itself, establish frame invariance or select a unique propagation bound.

The missing concept is therefore more precise than generic LOCALITY:

`BOUNDED INFLUENCE`

and, for Lorentz physics,

`FRAME-INVARIANT BOUNDED INFLUENCE`.

The numerical value of the bound remains a separate physical constant.

## What this closes

The previous gap is now decomposed:

`LOCALITY` → constrains which relations may act directly.

`BOUNDED INFLUENCE` → constrains the maximum causal reach per ordered transition.

`FRAME-INVARIANT BOUNDED INFLUENCE` → supplies the structural ingredient needed by REL-22 to obtain Lorentz kinematics.

But:

`Ω primitives → BOUNDED INFLUENCE`

is **not yet derived**.

## Ω status

This is a useful foundation candidate and a hard physical boundary, not a failed experiment. It identifies the exact class of missing structure rather than hiding it inside the word "locality".

Candidate chain:

`DISTINCTION → RELATION → STATE → ORDERED TRANSITION → LOCALITY → BOUNDED INFLUENCE → CAUSAL CONE → RELATIVITY → LORENTZ`

The arrow `LOCALITY → BOUNDED INFLUENCE` remains an open derivation target.
