# REL-02E — Vector Maxwell Relation + Energy

## Purpose

Extend REL-01E from a scalar relation model to the minimal transverse vector structure of vacuum electromagnetism, while keeping energy inside the same test.

## Frozen model

For a 1D transverse plane wave propagating along `x`:

- electric field: `E_y`
- magnetic field: `H_z`
- local relation: nearest-neighbour spatial difference
- dynamics:
  - `∂E_y/∂t = -(1/ε) ∂H_z/∂x`
  - `∂H_z/∂t = -(1/μ) ∂E_y/∂x`
- wave speed: `c = 1/sqrt(εμ)`
- energy density: `u = 1/2 (ε E_y² + μ H_z²)`

The numerical scheme is a staggered finite-difference (Yee-like) update with periodic boundaries. The periodic boundary is deliberate: it removes external energy flux from the primary conservation test.

## Relation-first mapping

`state (E,H) → spatial relation → coupled dynamics → field energy → propagation`

The important result is that the spatial relation is not only used to move the disturbance. The same field state also enters the electromagnetic energy density, so propagation and energy accounting are tested together.

## Calculated run

Default parameters:

- `N = 400`
- `steps = 1200`
- `dx = 1`
- `dt = 0.5`
- `ε = μ = 1`
- target `c = 1`

Observed from the numerical run:

- measured propagation speed: approximately `0.99936`
- relative speed error: approximately `-6.38×10^-4`
- initial energy: approximately `15.04296`
- final energy: approximately `15.04260`
- relative final energy error: approximately `-2.39×10^-5`
- full relative energy range: approximately `1.28×10^-3`

These are numerical diagnostics of this discretization, not measurements of a physical experiment.

## Transverse structure

The simulated mode has `E_y` and `H_z` while propagation is along `x`. Thus the field components are transverse to the propagation direction. This is a minimal electromagnetic vector structure, rather than the scalar field used in REL-01E.

## Interpretation

REL-02E supports the following narrower statement:

> A relation-first computational architecture can retain vector field structure, reproduce vacuum-wave propagation, and maintain a quantitative electromagnetic energy balance in a minimal Maxwell system.

It does **not** establish that electromagnetism is fundamentally reducible to the abstract relation concept. Gauge structure, sources/charges, full 3D constraints, polarization families, and quantum excitation remain separate tests.

## Falsification pressure

The architecture becomes weaker as a universal claim if the same frozen relation schema cannot accommodate these additional layers without arbitrary, post-hoc definitions.

## Status

`CALCULATED / SUPPORTIVE / NOT PROOF`

Next: freeze REL-02E and test whether the relation architecture can absorb the gauge/connection layer without changing its core definitions (`REL-03`).
