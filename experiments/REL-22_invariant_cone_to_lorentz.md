# REL-22 — Invariant causal cone → Lorentz structure

## Question

Once a finite invariant causal speed is independently supplied, does the combination of linear inertial-frame transformations, relativity, isotropy/reciprocity and preservation of the causal cone constrain the transformation to Lorentz form?

## Result

For `c=1` and boosts `v={0.1,0.3,0.6,0.8}`, the constructed transformation preserves both null lines `x=±ct` and the quadratic interval `c²t²−x²` to floating-point precision.

Maximum tested errors:

- light-cone preservation: approximately `1.8×10^-15`;
- interval preservation: approximately `1.8×10^-15`.

## Interpretation

This closes the **conditional** step:

`finite invariant causal cone + inertial-frame relativity + linearity/reciprocity`

`→ Lorentz transformation`

`→ Minkowski interval preservation`

It does **not** close the deeper step:

`Ω weak relational primitives → finite invariant causal speed c`.

`c` remains an external physical/kinematic input here.

## Status

**CONDITIONAL STRUCTURAL SUPPORT.**

No claim is made that the experiment derives `c`, spacetime dimension, metric signature, or the relativity principle itself.
