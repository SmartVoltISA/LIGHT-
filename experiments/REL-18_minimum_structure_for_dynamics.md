# REL-18 — Minimum Structure for Physical Dynamics

Date: 2026-09-07
Status: COMPLETED — sufficiency test, not a derivation

## Question

What additional structure is sufficient to turn PATH/VALUE into a physical dynamical law, and which part is responsible for conservation?

## Minimal test class

Use a one-dimensional local path functional

`S[x] = ∫ L(x, xdot, t) dt`

and impose the stationary condition

`δS = 0`.

Two cases are compared:

1. time-translation-invariant `L = 1/2 m xdot² − 1/2 kx²`;
2. explicitly time-dependent `L = 1/2 m xdot² − 1/2 kx² + γ t x²`.

The first case is local in the path parameter and has no explicit time dependence. The second keeps locality and stationarity but removes time-translation invariance.

## Numerical result

For `m=2`, `k=3`, RK4 integration gives:

`time-translation-invariant max energy drift ≈ 9.77×10⁻¹⁵`

For the explicitly time-dependent case with `γ=0.05`:

`max energy drift ≈ 1.215446×10⁻¹`

The balance identity

`dE/dt = −∂L/∂t = −γ x²`

is satisfied numerically with maximum integrated error `≈ 5.15×10⁻⁹`.

## Structural result

The test separates three layers that were previously mixed:

`PATH` alone → not enough.

`VALUE(PATH)` alone → can rank paths, but does not specify physical local dynamics.

`LOCAL PATH FUNCTIONAL + δS=0` → supplies a dynamical selection rule in this tested class.

Then:

`TIME-TRANSLATION SYMMETRY → CONSERVED ENERGY`

while explicit time dependence removes that conservation, with the precise balance law above.

This is consistent with the standard Noether framework: continuous symmetries of a Lagrangian are associated with conserved quantities/currents. citeturn0search2turn0search3

## Important negative boundary

REL-18 does **not** derive the physical form

`L = 1/2 m v² − V(x)`

from Ω primitives.

It also does not derive `m`, the spacetime metric, the time parameter, or the stationary-action principle itself from abstract VALUE.

It establishes a narrower result:

**If** a system admits a local path functional and a stationary-selection rule, then local equations of motion can arise; **if additionally** the functional is time-translation invariant, an energy-like conserved quantity follows.

Therefore the missing structure after REL-17 is not merely “more value”. It is a physical path functional plus a selection/stationarity law, followed by symmetry constraints.

## Updated Ω interpretation

`WILL → MEMORY → VALUE → CHOICE → PATH → [LOCAL PHYSICAL FUNCTIONAL] → ACTION/SELECTION → CHANGE → MEMORY`

and, where time-translation symmetry exists:

`SYMMETRY → CONSERVATION`

The bracketed layer remains an open derivation target.

## Next target

Test whether locality + stationarity + symmetry can constrain the **form** of the physical functional without importing the known mechanical Lagrangian. Compare candidate functionals under:

- locality;
- composition of adjacent path segments;
- time-translation symmetry;
- spatial translation/rotation symmetry;
- dimensional consistency;
- conservation laws.

Any parameter that remains free must be recorded as an external input rather than silently derived.
