# REL-38 — Electromagnetic characteristic cone vs generic causal cone

Date: 2026-09-07
Status: COMPLETED — structural matching audit

## Question

Does the finite causal cone constructed from local reach/time coincide with the vacuum electromagnetic characteristic cone without inserting `c` into the electromagnetic calculation?

## Generic causal sector

For a local rule with reach `ell` per minimum transition time `tau`:

`v_cone = ell/tau`.

Test values:

`ell = 2`

`tau = 0.5`

so

`v_cone = 4`.

This is deliberately independent of electromagnetism.

## Electromagnetic sector

For vacuum Maxwell equations, the characteristic wave speed is

`v_EM = 1/sqrt(mu0*epsilon0)`.

Using the CODATA/NIST values used in the LIGHT- audit:

`mu0 = 1.25663706127e-6 H/m`

`epsilon0 = 8.8541878188e-12 F/m`

we obtain

`v_EM = 299792457.9998211 m/s`.

The SI comparison value is

`c = 299792458 m/s`.

Relative difference from coefficient rounding:

`~ -5.97e-13`.

NIST independently states the vacuum Maxwell relation `c = (epsilon0*mu0)^(-1/2)` and gives the exact SI value of `c`. See the external source record.

## Result

There are two logically separate characteristic speeds:

`v_cone = ell/tau`

and

`v_EM = 1/sqrt(mu0*epsilon0)`.

The electromagnetic value agrees with the SI `c` to the expected coefficient-rounding level.

The generic causal speed does **not** automatically equal it. In the toy choice above:

`v_cone = 4`

while

`v_EM ~= 2.99792458e8 m/s`.

Therefore:

**FINITE CAUSAL CONE + LOCALITY DOES NOT BY ITSELF DERIVE THE ELECTROMAGNETIC SPEED SCALE.**

## What would be required for equality?

An additional physical identification/constraint is needed:

`ell/tau = 1/sqrt(mu0*epsilon0)`.

Equivalently, once `ell` is selected, the causal time scale would have to satisfy

`tau = ell*sqrt(mu0*epsilon0)`.

This is a matching condition, not a derivation.

## Strong conclusion

The investigation now cleanly separates three levels:

1. **Structural level**

`DISTINCTION -> RELATION -> LOCALITY -> BOUNDED INFLUENCE -> CAUSAL CONE`

This can establish a finite characteristic propagation bound in a model.

2. **Kinematic level**

Adding invariant-cone structure plus inertial-frame assumptions constrains Lorentz-type transformations.

3. **Electromagnetic dynamical level**

Maxwell coefficients determine

`v_EM = 1/sqrt(mu0*epsilon0)`.

The equality of the causal-cone speed with the EM speed is therefore an additional cross-sector constraint that must be explained, not assumed.

## Ω boundary

Not derived:

- `mu0`
- `epsilon0`
- the SI scale
- the numerical value of `c`
- Maxwell's field equations from the Ω foundation
- the identification of the generic causal cone with the electromagnetic cone

Established:

- a generic causal cone can be defined independently;
- Maxwell vacuum has an independently determined characteristic speed;
- their equality is a falsifiable matching condition rather than a tautology.

## Next target

REL-39 should remove arbitrary `ell/tau` parameters as far as possible and ask whether a single local field structure can simultaneously produce:

`causal cone`

and

`Maxwell characteristic cone`

from the same underlying quadratic/hyperbolic operator.

That is the first point where the Ω causal construction can genuinely meet the LIGHT electromagnetic sector rather than merely coexist with it.
