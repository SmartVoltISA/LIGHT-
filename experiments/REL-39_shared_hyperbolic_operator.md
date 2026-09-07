# REL-39 — Shared hyperbolic operator: causal cone and electromagnetic cone

Date: 2026-09-07
Status: COMPLETED — structural unification test

## Question

Can the causal cone and the electromagnetic wave cone arise as characteristics of one and the same local hyperbolic operator, rather than being compared as two unrelated speeds?

## Construction

Use the 1D transverse vacuum Maxwell sector in first-order form:

`d/dt [E, H]^T = M d/dx [E, H]^T`

with

`M = [[0, 1/epsilon], [1/mu, 0]]`

(up to orientation/sign convention).

The characteristic speeds are the eigenvalues of `M`.

Since

`det(M - lambda I) = lambda^2 - 1/(epsilon*mu)`,

we obtain

`lambda = +/- 1/sqrt(epsilon*mu)`.

Therefore the same operator simultaneously defines:

`causal characteristic cone: |dx/dt| <= 1/sqrt(epsilon*mu)`

and

`EM wave characteristics: dx/dt = +/- 1/sqrt(epsilon*mu)`.

## Numerical audit

Tested parameter pairs:

`(epsilon, mu) = (1, 1)`

`v = 1`

`(4, 0.25)`

`v = 1`

`(2, 8)`

`v = 0.25`

`(0.3, 3)`

`v = 1.0540925533894598`

For every case, the two eigenvalues are exactly the expected pair `(-v,+v)` to numerical precision. Maximum tested eigenvalue error was below `2.3e-16`.

## Result

**POSITIVE STRUCTURAL UNIFICATION:**

The causal cone and electromagnetic propagation cone do not need to be treated as two separately imposed objects once the local dynamics are represented by a hyperbolic first-order field operator.

They are two descriptions of the same characteristic structure:

`LOCAL FIELD RELATION`
→ `HYPERBOLIC OPERATOR`
→ `CHARACTERISTIC EIGENVALUES`
→ `CAUSAL CONE`
→ `EM WAVE PROPAGATION`

This is stronger than REL-38, where a generic `ell/tau` cone was only compared numerically with the Maxwell speed.

## What this DOES establish

1. A single local dynamical operator can carry both the causal cone and the EM propagation cone.
2. The propagation speed is not an extra parameter once the operator coefficients are specified.
3. The characteristic cone is determined mathematically by the principal part of the local field dynamics.
4. The EM wave equation and causal propagation are therefore structurally unified at the PDE level.

## What this DOES NOT establish

The following are still inputs, not derived from Ω:

- `epsilon_0`
- `mu_0`
- the absolute SI length/time scale
- the numerical value `c = 299792458 m/s`
- Maxwell's equations themselves
- why the physical vacuum operator has exactly this coefficient structure
- why this characteristic speed is invariant between inertial frames
- why the electromagnetic sector is the universal causal sector

## Relation to REL-38

REL-38 established:

`generic causal cone` and `EM cone` are distinct unless a matching constraint is supplied.

REL-39 now shows the stronger possibility:

`one hyperbolic local operator`
→ produces both cones automatically.

So the missing problem is no longer "how do two speeds match?".

It is:

`WHY DOES THE FUNDAMENTAL LOCAL OPERATOR HAVE THE MAXWELL PRINCIPAL PART?`

That is the real derivation pressure point.

## Ω boundary

Current strongest justified chain:

`DISTINCTION`
→ `RELATION`
→ `LOCALITY`
→ `LOCAL DYNAMICS`
→ `HYPERBOLIC OPERATOR`
→ `CHARACTERISTIC CONE`

and, conditionally for the electromagnetic sector:

`HYPERBOLIC OPERATOR + MAXWELL PRINCIPAL PART`
→ `EM CONE`
→ `v_EM = 1/sqrt(mu0*epsilon0)`.

The Maxwell principal part is still an additional physical input. No claim of deriving it from Ω is made.

## Next target

REL-40 should attack the remaining structural gap: determine which minimal symmetry/relational requirements constrain the 1D/3D field operator toward the Maxwell form, while testing explicit countermodels.

The decisive criterion is not whether Maxwell can be reproduced after choosing Maxwell equations, but whether the candidate Ω requirements exclude non-Maxwell hyperbolic operators without secretly inserting electromagnetic assumptions.
