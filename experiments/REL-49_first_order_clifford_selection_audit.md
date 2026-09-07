# REL-49 — First-order relativistic Clifford selection audit

Date: 2026-09-08
Branch: `rel-41-actual`

## Question

Can a Dirac/Clifford structure be selected without simply postulating gamma matrices, if we require a local first-order relativistic matter equation with finite internal dimension, Hermitian Hamiltonian, isotropy, and the relativistic dispersion relation?

## Conditional setup

Take a first-order Hamiltonian

`H(p) = alpha_i p_i + beta m`.

Demand

`H(p)^2 = (|p|^2 + m^2) I`

for arbitrary momentum `p` and mass `m`.

Expanding the square forces

`{alpha_i, alpha_j} = 2 delta_ij I`

`{alpha_i, beta} = 0`

`beta^2 = I`.

These are precisely a Clifford-algebra relation for the first-order relativistic operator.

## Explicit 4x4 realization

The experiment uses

`alpha_i = sigma_i tensor sigma_1`

`beta = I tensor sigma_3`.

All required anticommutators vanish or equal the required identity to numerical precision.

100 random momentum/mass tests give the relativistic spectrum

`E = +/- sqrt(|p|^2 + m^2)`

with maximum numerical error below `1e-12`.

The private numerical run returned approximately

`max_clifford_residual = 0`

`max_dispersion_error = 2.66e-15`.

## 2x2 obstruction

A massive 2x2 first-order realization would require four nonzero Hermitian matrices `alpha_1, alpha_2, alpha_3, beta` that square to the identity and pairwise anticommute.

In complex dimension two, three such matrices are unitarily equivalent to the Pauli matrices. The only 2x2 matrix that anticommutes with all three Pauli matrices is the zero matrix. Therefore a nonzero fourth matrix `beta` cannot exist.

So the massive first-order construction requires a larger representation. In 3+1 dimensions the standard minimal complex Dirac realization is 4-dimensional.

CERN lecture material independently records the Clifford relation `{gamma_mu,gamma_nu}=2 eta_mu nu` and the 4D Dirac representation; it also notes the 4D Dirac representation decomposes into chiral sectors. See CERN, *Introductory Lectures on Quantum Field Theory*. 

## Interpretation

This is a stronger result than REL-48, but it remains conditional.

Starting assumptions:

`Lorentzian relativistic dispersion`
`+ first-order local evolution`
`+ linearity in momentum`
`+ isotropy`
`+ Hermiticity`
`+ massive nontrivial mode`

force the anticommutator algebra, hence a Clifford structure.

Then:

`Clifford algebra`
`→ spinor representation`
`→ Dirac-type first-order operator`.

CERN material explicitly describes the link from Clifford algebra to the spinor representation of the Lorentz algebra. citeturn0search18

## What was NOT derived

This experiment does not derive:

- Lorentzian metric/signature from Ω alone;
- the finite invariant speed `c`;
- first-order dynamics itself;
- the choice to describe matter by a relativistic linear operator;
- fermionic statistics / anticommutation of quantum field operators;
- Pauli exclusion;
- electron identity;
- numerical mass;
- numerical charge;
- the Standard Model matter spectrum.

Therefore the correct status is:

**CONDITIONAL POSITIVE:** once first-order relativistic massive propagation is required, Clifford/Dirac structure is no longer an arbitrary stylistic choice; it is forced by the dispersion-preserving algebraic constraints.

But this is not yet an Ω derivation of fermions. The missing bridge is now sharply isolated:

`Ω → relativistic first-order carrier`

and, separately,

`first-order carrier → Clifford → spinor`.

The first arrow remains unproven.

## Next test

REL-50 should test whether the quantum-statistical requirement of locality + positivity + multi-particle consistency can independently select Fermi anticommutation rather than Bose commutation, or whether spin-statistics must remain an additional theorem/input once relativistic spinor structure is present.
