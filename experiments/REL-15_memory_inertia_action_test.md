# REL-15 — Memory, inertia and action

## Question

Does a generic notion of memory force physical inertia/mass, or is a more specific retained dynamical state required?

## Frozen distinction

- **Memory**: information from prior states remains relevant to future transitions.
- **Inertia**: a state of motion/change persists after the external cause is removed.
- **Mass**: in Newtonian mechanics, the coefficient relating impulse to velocity change and force to acceleration.
- **Action**: the integral of a Lagrangian over a trajectory; in the free-particle model `L = 1/2 m v^2`.

The test must not identify these concepts by definition.

## Models

### A. Memoryless / overdamped response

`v(t) = F(t)/k`

After the impulse disappears, `v` immediately returns to zero. There is no retained momentum-like state.

### B. Inertial response

`m d²x/dt² = F(t)`

The velocity `v` is part of the state and remains after the impulse.

For impulse `J = ∫F dt`:

`Δv = J/m`.

### C. Action layer

For a free particle:

`L = 1/2 m v²`

`p = ∂L/∂v = m v`.

The Euler–Lagrange equation gives `dp/dt = 0`, so the retained momentum is the inertial state.

## Numerical result

Using `J = 1`, `m = 2`, and a finite-step impulse:

- memoryless post-impulse velocity: `0`;
- inertial `Δv`: `0.5`;
- expected `J/m`: `0.5`;
- relative impulse error: below `1e-12`;
- mass-scaling test (`m=1` vs `m=4`): relative error below `1e-12`;
- free-particle momentum spread: below `1e-12`.

The numerical checks therefore reproduce the expected inertial persistence and the action-to-momentum relation.

## Interpretation

The result is **supportive but deliberately limited**:

`retained dynamical state -> inertial persistence`

is a valid structural mapping.

However:

`generic memory -> mass`

is **not established**.

Memory can exist without inertia. What matters is that the retained state has the correct dynamical role (momentum/velocity-like state) and that the transition rule is second-order or equivalently first-order in an enlarged state space.

Likewise, the action formulation organizes the dynamics and produces momentum, but the coefficient `m` remains an input parameter in the free-particle action. The experiment does **not** derive the numerical value or microscopic origin of physical mass.

## Ω interpretation

A safer chain is:

`Will / possibility space`

`→ Memory / retained constraints`

`→ allowed transition rule`

`→ Action / trajectory rule`

`→ retained dynamical state`

`→ Inertia`

`→ measurable energy and momentum`

The current test supports the middle link between retained dynamical state and inertia. It does not yet establish that Will + Memory uniquely generate the physical action.

## Boundary

Established physics must remain separate from Ω interpretation. In the Standard Model, mass generation is not reduced to generic memory; CERN describes the Higgs mechanism as giving mass to W/Z and many matter particles through interaction with the Higgs field, while the photon remains massless because it does not acquire mass through that mechanism. The Ω mapping therefore remains a hypothesis, not a replacement for the Standard Model account.

## Status

**STRUCTURAL SUPPORT / IMPORTANT NEGATIVE RESULT**

The experiment strengthens the idea that inertia can be represented as retained dynamical state, while simultaneously falsifying the stronger shortcut that arbitrary memory by itself is sufficient to produce mass.
