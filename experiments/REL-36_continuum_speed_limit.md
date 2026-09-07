# REL-36 — Continuum refinement and characteristic speed

Date: 2026-09-07
Status: COMPLETED — scale audit

## Question

Can a finite characteristic speed remain stable under continuum refinement without changing the local propagation rule?

## Construction

Let a local transition advance a disturbance by spatial scale `ell` in minimum time `tau`.

Then the characteristic front speed is

`v = ell / tau`.

The continuum audit refines both scales while preserving their ratio.

## Matched refinement

Starting from `(ell,tau)=(1,1)`:

`(1,1) -> v=1`

`(0.5,0.5) -> v=1`

`(0.25,0.25) -> v=1`

`(0.125,0.125) -> v=1`

`(0.0625,0.0625) -> v=1`

The characteristic speed is invariant under refinement when

`ell -> a ell`

and

`tau -> a tau`.

## Independent scaling control

If spatial and temporal scales are not locked:

`(1,1) -> v=1`

`(0.5,0.25) -> v=2`

`(0.25,0.0625) -> v=4`.

Therefore refinement alone does not generate a universal numerical speed. The ratio `ell/tau` is an independent scale input unless an additional principle locks spatial and temporal scales.

## Result

**POSITIVE CONTINUUM-SCALING RESULT:**

A finite characteristic speed is stable under simultaneous refinement of local spatial and temporal scales.

**NEGATIVE DERIVATION RESULT:**

The finite numerical value of that speed is not derived by locality alone. It remains encoded in the scale ratio

`v = ell/tau`.

## Strong conclusion

The previous causal-chain results survive continuum refinement:

`LOCALITY + MINIMUM TRANSITION TIME`

can produce a finite characteristic speed,

but

`LOCALITY`

alone does not determine its numerical value.

To obtain a universal invariant speed rather than an arbitrary unit-dependent ratio, the theory still needs a scale-locking principle and frame-invariance/relativity structure.

## Relation to known physics

This distinction is important because finite propagation bounds are well established for broad classes of local quantum dynamics, including Lieb–Robinson bounds. Such bounds constrain propagation without by themselves identifying the bound with the relativistic speed of light. The existence and form of a light cone can depend on interaction range and dynamical assumptions.

## Critical boundary

Not established:

1. `v = c`.
2. Derivation of SI units or the numerical value `299792458 m/s`.
3. Lorentz invariance.
4. Minkowski metric/signature.
5. That the continuum limit uniquely selects electromagnetism.

## Ω status

The strongest defensible chain is now:

`DISTINCTION`
→ `RELATION`
→ `LOCALITY`
→ `BOUNDED INFLUENCE`
→ `CAUSAL CONE`
→ `FINITE CHARACTERISTIC SPEED`

with a hard boundary:

`FINITE SPEED ≠ DERIVED c`.

The missing step is no longer "can locality produce a finite speed?" It can in the model. The missing step is "what principle fixes the same invariant speed for all inertial observers?"

That points directly to the next test: derive or countermodel the required frame-invariant causal cone.
