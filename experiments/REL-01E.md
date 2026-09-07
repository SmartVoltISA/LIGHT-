# REL-01E — Energy-Constrained Relation Test

## Purpose

Extend REL-01. The relation model must reproduce propagation **and** carry a well-defined energy balance.

## Frozen model

For a 1D chain:

`q̈_i = c² (q_{i+1} - 2q_i + q_{i-1}) / dx²`

The relation is the local difference between neighboring states. No additional force law is introduced.

For `m = 1` and `k = c²`, the tracked energy is:

`E = 1/2 Σ v_i² + 1/2 c² Σ (q_{i+1} - q_i)²`

The first term is kinetic energy. The second is energy stored in the relations between neighboring states.

## Numerical run

Parameters:

- `N = 201`
- `dt = 0.2`
- `dx = 1`
- `c = 1`
- 2000 Velocity-Verlet steps
- fixed endpoints
- initial Gaussian displacement
- zero initial velocity

Observed run:

- `E_initial ≈ 0.07802683`
- `E_final ≈ 0.07802019`
- relative final error `≈ -7.86×10^-5`
- full energy range / initial energy `≈ 4.05×10^-4`

## Interpretation

The same relation that generates propagation also defines the stored interaction energy through the squared local difference.

This is stronger than REL-01, because the model now has both:

`relation → dynamics`

and

`relation → energy storage`

The result does **not** establish a universal theory. It shows that a minimal relation model can simultaneously support propagation and a numerically stable energy accounting under the stated closed-system conditions.

## Next test

The next comparison should replace the scalar chain with the electromagnetic field. There the corresponding energy density is established by Maxwell electrodynamics:

`u = 1/2 (ε₀ E² + B²/μ₀)`

and energy transport is described by the Poynting vector and theorem.

The critical question is whether the same abstract relation architecture can represent:

`local relation → field dynamics → stored energy → energy flux → conservation`

without adding arbitrary domain-specific structure.

## Status

`CALCULATED / SUPPORTIVE`

Not a proof of H5. The test is a controlled computational result for the minimal relation model.
