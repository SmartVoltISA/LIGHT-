# REL-37 — Frame-invariant causal cone

Date: 2026-09-07
Status: COMPLETED — positive conditional derivation

## Question

What additional structure is required for a finite causal cone to have the same boundary for different inertial observers?

## Test

Use a 1+1D linear kinematic model with a finite cone

`x^2 - C^2 t^2 = 0`.

Compare:

1. Lorentz transformations.
2. Galilean transformations.

The experiment also checks inverse/reciprocity consistency.

## Result

For all tested relative velocities `|v| < C`:

Lorentz transformation preserves

`x'^2 - C^2 t'^2 = x^2 - C^2 t^2`

including both lightlike branches.

The inverse transformation is obtained by replacing `v -> -v` and recovers the original event to numerical precision.

The Galilean transformation does not preserve the same finite cone. A trajectory with `x=Ct` generally transforms to a different slope.

## Conditional conclusion

Within this linear 1+1D model:

`FINITE INVARIANT CAUSAL CONE`

+

`RECIPROCITY / INERTIAL FRAME EQUIVALENCE`

+

`LINEARITY`

constrain the transformation to the Lorentz class rather than the Galilean class.

Thus the missing ingredient identified by REL-36 is precisely **frame-invariant bounded influence**.

## What this does and does not derive

Derived conditionally:

`bounded influence`
→ `finite causal cone`
→ `frame-invariant cone`
→ `Lorentz-type kinematics`.

Not derived:

`C` itself.

The numerical value of `C` remains an input scale. The experiment does not derive:

- the physical speed of light;
- SI units;
- spacetime dimension;
- Minkowski metric from Ω primitives;
- Lorentz invariance from distinction/relation alone;
- electromagnetism;
- Maxwell equations.

## Important boundary

This is deliberately a conditional derivation, not a claim that relativity follows automatically from the earlier Ω chain.

The strongest current chain is:

`DISTINCTION`
→ `RELATION`
→ `LOCALITY`
→ `BOUNDED INFLUENCE`
→ `FINITE CAUSAL CONE`
→ `FRAME-INVARIANT CAUSAL CONE`
→ `LORENTZ-TYPE KINEMATICS`

with the unresolved physical question:

`WHAT FIXES C?`

## Next decisive target

Test whether `C` can be tied to a dynamical invariant of the relational/field sector rather than inserted kinematically. The natural candidate is the electromagnetic sector:

`field equations`
→ `wave equation`
→ `characteristic cone`
→ `C = 1/sqrt(mu0 epsilon0)`.

Then compare that characteristic speed with the invariant causal cone without assuming equality in advance.
