# REL-01 — Minimal Relation Operator Test

## Objective

Test the narrowest part of H1/H5: whether one unchanged local relation rule can generate the same propagation mathematics in LIGHT and in an independent physical system.

This is deliberately narrower than Maxwell/QED. It does **not** claim to derive electromagnetism from relations.

## Frozen core rule

For a field/state variable `q_i` on a nearest-neighbour lattice:

`L q_i = q_{i+1} - 2 q_i + q_{i-1}`

and dynamics:

`q_tt = c^2 L q`.

No domain-specific change is permitted between the two interpretations.

## Test A — LIGHT propagation layer

Interpret `q` as a scalar field mode. The relation operator produces a discrete wave equation. This tests the propagation layer only; Maxwell's vector structure, gauge constraint, polarization and sources are outside this minimal scalar model.

Numerical parameters:

- `N = 800`
- `dx = 1`
- `c = 1`
- `dt = 0.4`
- 500 time steps
- Gaussian initial displacement

Observed from the numerical run:

- fitted right-moving front speed: **1.00264** lattice units / time unit
- relative energy variation: **1.34 × 10^-3**

The speed is within about 0.26% of the model value `c = 1`.

## Test B — independent system: mass-spring chain

Interpret the same `q_i` as displacement of equal masses coupled by identical nearest-neighbour springs. For unit mass and unit spring constant the linearized equation is exactly the same `q_tt = L q`.

No new parameter or altered relation definition is introduced.

The same numerical implementation gives:

- fitted propagation speed: **1.00264**
- relative energy variation: **1.34 × 10^-3**

## Result

### PASS — propagation-layer universality

The same relation operator and same evolution rule reproduce the same propagation behavior in two different interpretations.

### NOT PROVEN — full LIGHT universality

This experiment does **not** reproduce the full electromagnetic theory. In particular, the minimal scalar relation model does not derive:

- local U(1) gauge symmetry;
- gauge redundancy of `A_mu`;
- electromagnetic field tensor `F_mu nu`;
- two physical transverse photon polarizations;
- coupling to electric charge;
- quantum statistics / photon creation and annihilation;
- Maxwell constraints and relativistic covariance.

Therefore H5 must currently be split:

- **H5a: propagation architecture is transferable — supported by REL-01.**
- **H5b: the same minimal relation architecture reproduces full electromagnetic structure — untested and currently unsupported.**

## Why this result matters

The test removes one possible source of self-deception: the relation operator was not changed to fit the second system. The same mathematical object works in both cases.

But the test also exposes the boundary of the claim. The relation skeleton captures propagation, not the complete identity of electromagnetism.

The next experiment should therefore add the smallest missing structure one layer at a time and test whether the same additions remain domain-independent.

## Next test

REL-02 should test a vector-valued relation model against electromagnetic wave constraints and an independent vector/tensor system, while keeping the core relation operator frozen before measurement.
