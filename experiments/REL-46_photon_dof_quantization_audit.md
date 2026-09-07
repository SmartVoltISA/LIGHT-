# REL-46 — Photon degrees of freedom and quantization audit

## Question

Given the Maxwell/U(1) structure selected conditionally in REL-45, what follows for the free propagating quantum mode?

## Input package

Assume:

- 3+1-dimensional Lorentzian spacetime.
- Maxwell kinetic action.
- U(1) gauge redundancy.
- Free vacuum propagation.
- Standard quantum relations `E = hbar omega` and `p = hbar k` when translating classical modes to quantum excitations.

The first four items are field-theory inputs; `hbar` is an additional quantum normalization constant.

## Mode condition

For a plane-wave mode, the vacuum Maxwell equations give the null dispersion relation

`k^2 = 0`.

A four-component vector polarization `epsilon^mu` is constrained by transversality/Lorenz gauge

`k_mu epsilon^mu = 0`.

The gauge equivalence

`epsilon^mu ~ epsilon^mu + alpha k^mu`

removes one further direction.

Therefore:

`4 components - 1 constraint - 1 gauge direction = 2 physical polarizations`.

For propagation along `z`, representatives can be chosen as the two transverse `x` and `y` modes. Circular combinations give the two helicity sectors `+1` and `-1`.

## Numerical audit

The accompanying script checks several null four-momenta and confirms:

- `k^2 = 0` to numerical precision.
- the transversality constraint has rank one.
- the physical quotient dimension is exactly two.
- explicit transverse representatives satisfy the constraint.

## Quantum interpretation

With

`E = hbar omega`,

`p = hbar k`,

and `k^2 = 0`, one obtains

`E^2 - p^2 c^2 = 0`.

Thus the excitation is massless in the relativistic sense.

The numerical value of `hbar`, the SI value of `c`, and the quantum field normalization are not derived by this experiment.

## Result

**CONDITIONAL POSITIVE.**

The Maxwell/U(1) gauge structure has exactly two propagating physical polarization degrees of freedom in 3+1 dimensions, and its free modes are massless. Quantization maps these modes to photon excitations; `hbar` remains an external quantum constant.

## Boundary

This does not derive:

- quantum mechanics from Ω,
- Planck's constant,
- Lorentz symmetry,
- spacetime metric/signature,
- the existence of U(1),
- the numerical value of the electromagnetic coupling,
- the SI scale.

## Current chain

`Ω relational package`
`→ locality`
`→ bounded influence`
`→ causal cone`
`→ 3D transverse selection`
`→ connection/curvature`
`→ Abelian local algebra`
`→ compact U(1) only after global periodicity/quantum input`
`→ Maxwell kinetic term under Lorentz + locality + gauge + quadratic + <=2 derivatives`
`→ exactly 2 propagating photon polarizations`
`→ massless quantum excitation`.

The remaining major gate is the matter sector: whether local U(1) phase coupling forces the covariant derivative/current interaction and what, if anything, Ω can say about charge, coupling normalization, and the electron sector.
