# REL-29 — Electromagnetic sector and invariant speed

Date: 2026-09-07
Status: COMPLETED — structural speed relation isolated; absolute SI value not derived

## Question

Can the propagation speed be obtained from the internal relation between electric and magnetic sectors, without inserting `c` as an input?

## Relational model

Consider the coupled local system

`∂E/∂t = A ∂B/∂x`

`∂B/∂t = C ∂E/∂x`.

Applying one time derivative and substituting the second equation gives

`∂²E/∂t² = AC ∂²E/∂x²`.

The same follows for `B`. Therefore the propagation speed is

`v = sqrt(AC)`.

For vacuum Maxwell theory,

`A = 1/epsilon0`

`C = 1/mu0`

so

`v = 1/sqrt(mu0 epsilon0)`.

## Field-normalization audit

Under independent field rescalings

`E' = lambda E`, `B' = mu B`,

the coefficients transform as

`A' = A mu/lambda`

`C' = C lambda/mu`.

Hence

`A'C' = AC`.

The propagation speed is therefore invariant under separate normalization of the two field variables. Individual coefficients are representation-dependent, while their product is structural for this coupled system.

## Numerical test

Tested coefficient pairs:

`A=1, C=1 -> v=1`

`A=4, C=0.25 -> v=1`

`A=2, C=8 -> v=4`

`A=0.3, C=3 -> v=sqrt(0.9) ≈ 0.9486832981`

The result follows directly from the product `AC`.

For the CODATA 2022 vacuum values

`mu0 = 1.25663706127e-6 N A^-2`

`epsilon0 = 8.8541878188e-12 F m^-1`,

the displayed rounded constants give approximately

`v = 299792457.9998211 m/s`.

The tiny difference from `299792458 m/s` is consistent with rounding of the displayed constants.

## Ω interpretation

The result strengthens the relational chain:

`RELATION → COUPLED SECTORS → SECOND-ORDER PROPAGATION → SPEED SCALE`

The speed is not an arbitrary parameter once the coupling coefficients and their units are fixed.

But the experiment does NOT derive the numerical SI value from Ω primitives. `mu0` and `epsilon0` themselves encode physical calibration/units, and using the exact SI value of `c` to define a coefficient would be circular.

## Critical boundary

Established:

1. A local coupled relational system can generate a finite propagation speed.
2. The speed is `sqrt(AC)`.
3. For Maxwell vacuum, this becomes `1/sqrt(mu0 epsilon0)`.
4. The product `AC` survives independent field normalization.

Not established:

1. Derivation of Maxwell coupling coefficients from Ω alone.
2. Derivation of `mu0` or `epsilon0` from more primitive relational quantities.
3. Derivation of the absolute SI numerical scale.
4. Derivation of Lorentz invariance solely from this coupling.

## Next target

Test whether the electric/magnetic coupling product can itself be fixed by deeper Ω constraints — locality, isotropy, reciprocity, gauge structure, and action — without importing SI constants or `c`.
