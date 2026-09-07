# REL-40 — Maxwell principal-part countermodel audit

**Date:** 2026-09-07  
**Branch:** `rel-34-final`  
**Status:** negative result / constraint gap identified

## Question

Can the Maxwell principal part be selected from a minimal Ω-style package consisting of:

`DISTINCTION → RELATION → STATE → ORDERED TRANSITION → LOCALITY → BOUNDED INFLUENCE`

plus:

- first-order local field evolution;
- finite two-way characteristic propagation;
- a positive conserved quadratic energy;
- isotropy-compatible field equations;
- no insertion of Maxwell coefficients, SI units, or the electromagnetic interpretation?

## Test

For a linear 1D first-order system

`∂t U = M ∂x U`

with quadratic energy

`H = 1/2 Uᵀ K U`, `K > 0`,

a sufficient constant-coefficient energy condition is that `K M` is symmetric. Real characteristic eigenvalues provide hyperbolic propagation.

The experiment tests three explicit models.

### A. Maxwell-like principal part

`M = [[0, 1/ε], [1/μ, 0]]`

`K = diag(ε, μ)`

so

`K M = [[0,1],[1,0]]`

and the characteristic speeds are

`v = ±1/√(ε μ)`.

For the test values `ε=4`, `μ=0.25`, this gives `v=1`.

### B. Acoustic countermodel

`M = [[0,1],[1,0]]`

`K = I`

This has exactly the same mathematical hyperbolic/energy structure and characteristic speeds `±1`, but nothing in the construction identifies the fields as electromagnetic.

### C. Characteristic countermodel

`M = diag(1,-1)`

`K = I`

Again:

- local;
- first-order;
- positive conserved quadratic energy;
- finite two-way propagation;
- real characteristics.

Yet it is manifestly not Maxwell's coupled field structure.

## Numerical result

All three systems satisfy the tested positive-energy/hyperbolicity conditions to numerical precision.

The Maxwell-like system has characteristic speed

`1/√(ε μ) = 1`.

The acoustic countermodel has speed `1` as well.

The diagonal countermodel has speeds `+1` and `-1`.

The energy symmetry defect `||KM-(KM)ᵀ||∞` is zero to floating-point precision for every tested model.

A field-basis similarity transformation preserves the characteristic eigenvalues, confirming that the numerical cone alone cannot identify a unique field representation.

## External mathematical check

The general theory of symmetric-hyperbolic first-order systems likewise treats the existence of a positive symmetrizer / conserved positive quadratic energy as the key structural condition for well-posed hyperbolic evolution; it does not identify a unique physical field theory. citeturn0search0turn0search5

## Result

**NEGATIVE RESULT.**

The package

`locality + bounded finite propagation + positive conserved energy + hyperbolicity`

does **not** select the Maxwell principal part.

Therefore REL-39's unification

`one local hyperbolic operator → characteristic cone = EM propagation cone`

is structurally meaningful, but it does not explain why nature chooses the Maxwell operator in the first place.

## What is still missing

The next constraint must distinguish electromagnetic structure from generic hyperbolic field systems without simply naming Maxwell as an assumption.

Candidate discriminators to test separately:

1. **3D rotational/isotropic vector structure** — require the propagating degrees of freedom to transform as spatial vectors rather than arbitrary components.
2. **Transverse propagation / constraint structure** — test whether longitudinal modes can be eliminated from the physical sector without inserting Maxwell's Gauss constraints by hand.
3. **Internal duality structure** — test whether an electric/magnetic-type internal rotation is forced or merely compatible.
4. **Gauge redundancy / connection structure** — test separately; do not assume local U(1) unless explicitly promoted as an input.
5. **Parity and time-reversal assignments** — test whether they eliminate countermodels.
6. **Coupling to a conserved source** — test whether a local continuity law plus universal source coupling constrains the operator.

The strongest next experiment is therefore not to force a derivation, but to build a **3D countermodel audit** and add candidate constraints one at a time. A constraint earns derivational status only if it eliminates explicit non-Maxwell countermodels while retaining Maxwell.

## Boundary

This experiment does **not** derive:

- Maxwell equations;
- U(1) gauge symmetry;
- ε₀ or μ₀;
- SI normalization;
- the numerical value of `c`;
- Lorentz invariance;
- electromagnetism as the physical interpretation of the fields.

It establishes only that generic local hyperbolic dynamics with positive energy is too broad a class to explain the Maxwell principal part.

## Next target

`REL-41 — 3D isotropic vector-field countermodel audit`

Goal:

`minimal Ω constraints → eliminate non-Maxwell 3D systems → identify the smallest additional structural requirement needed for Maxwell-type curl coupling`.
