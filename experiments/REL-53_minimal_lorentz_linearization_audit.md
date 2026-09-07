# REL-53 — Minimal Lorentz-linearization audit

## Question

Can the missing `?` between a causal quadratic relativistic operator and an exact first-order square root be sharpened into a minimality requirement, rather than simply postulating Dirac/Clifford structure?

## Starting point

REL-52 showed:

`finite causal cone + local first-order evolution + positive quadratic norm`
`↛ unique Dirac/Clifford structure`.

REL-51 showed the conditional positive result:

`first-order linear symbol + exact scalar second-order factorization`
`→ Clifford algebra`.

REL-53 isolates the extra ingredient needed to turn that conditional statement into a concrete selection rule: **minimal finite-dimensional linearization of the massive relativistic dispersion relation**, within a Hermitian isotropic Hamiltonian ansatz.

## Model

Take

`H(p) = α₁ p₁ + α₂ p₂ + α₃ p₃ + β m`.

Require exact relativistic dispersion for every momentum and mass:

`H(p)^2 = (|p|² + m²) I`.

Expanding the square and comparing independent monomials forces

`αᵢ² = I`

`β² = I`

`{αᵢ, αⱼ} = 0` for `i ≠ j`

`{αᵢ, β} = 0`.

Therefore the first-order carrier is a representation of the 3+1D Clifford algebra. This is the same structural factorization used in the standard Dirac construction. citeturn0search36turn0search6

## Minimality audit

A massive 3+1D realization in this ansatz requires four nonzero Hermitian generators that square to identity and pairwise anticommute.

For complex 2×2 matrices, three such generators are, up to unitary equivalence, a Pauli triple. No nonzero 2×2 matrix can anticommute with all three Pauli matrices. Therefore a nonzero mass matrix `β` cannot be added in dimension 2.

A 4×4 realization exists explicitly:

`αᵢ = σᵢ ⊗ σ₁`

`β = I₂ ⊗ σ₃`.

Thus dimension 4 is minimal **within the stated finite-dimensional complex Hermitian isotropic Hamiltonian ansatz**. The numerical audit over 200 random `(p,m)` samples gives machine-precision agreement with `±sqrt(|p|²+m²)`.

## Numerical result

`max_clifford_residual = 0`

`max_dispersion_error ≈ 3.55 × 10⁻¹⁵`

The algebraic 2×2 obstruction is exact, not a numerical claim.

## Important boundary

This does **not** derive the Dirac equation from Ω alone.

The result is conditional on adding:

`relativistic quadratic dispersion`
`+ local linear first-order matrix carrier`
`+ Hermitian Hamiltonian`
`+ isotropy`
`+ exact scalar factorization`
`+ finite-dimensionality`
`+ minimal internal dimension`.

Minimality is therefore exposed as a genuine additional selection principle, not something supplied by causal propagation itself.

## Why this matters

The chain can now be sharpened:

`Ω → causal quadratic operator`
`→ relativistic mass-shell constraint`
`→ demand a local linear carrier`
`→ exact scalar factorization`
`→ Clifford algebra`
`→ minimal finite-dimensional representation`
`→ 4-component Dirac carrier in 3+1D`.

But there is still a logical gap before calling this an Ω derivation: neither the relativistic quadratic form nor the demand for a linear carrier nor the minimality principle has yet been derived from the deeper Ω foundation.

## Non-uniqueness warning

“First-order relativistic root” by itself is not enough. Higher-order polynomial Clifford constructions can also produce first-order relativistic equations, including cubic roots of Klein–Gordon-type operators. Their representations can have different spin/covariance properties. citeturn0search0turn0academia34

So the correct discriminator is not simply **first order**, but the combination of **quadratic mass-shell factorization + exact Clifford relation + minimal representation**.

## Relation to previous experiments

`REL-49:` first-order relativistic Hamiltonian + exact dispersion ⇒ Clifford; 4×4 massive realization.

`REL-51:` exact scalar first-order factorization ⇒ Clifford; causal cone alone does not.

`REL-52:` finite causal propagation + first-order locality + positive norm does not select Dirac.

`REL-53:` minimality makes the missing selection principle explicit, and shows that 4 components are the minimum in the tested 3+1D massive ansatz.

## External verification

Mathematical treatments of Dirac-type operators identify the principal symbol with Clifford multiplication, while the Dirac operator is a first-order hyperbolic system on Lorentzian spin manifolds. citeturn0search2turn0search35

## Status

**CONDITIONAL POSITIVE.**

The minimal-linearization mechanism is internally consistent and numerically verified, but the upstream Ω derivation of the relativistic quadratic operator, linear-carrier requirement, and minimality principle remains open.
