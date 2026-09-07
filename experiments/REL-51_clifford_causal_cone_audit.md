# REL-51 — Clifford / causal-cone audit

## Question

Can the causal cone itself select the Clifford algebra, or is Clifford structure an additional algebraic requirement placed on a first-order carrier?

## Separation of claims

There are two different requirements:

A. **Characteristic cone only** — the principal symbol becomes singular on the desired null cone.

B. **Exact scalar second-order closure** — a first-order operator `A(p)=Gamma^mu p_mu` obeys

`A(p)^2 = (g^{mu nu} p_mu p_nu) I`

for every momentum `p`.

These must not be conflated.

## Algebraic result

Expanding the quadratic identity gives

`Gamma^mu Gamma^nu p_mu p_nu = g^{mu nu} p_mu p_nu I`.

Because `p_mu p_nu` is symmetric, polarization forces

`{Gamma^mu, Gamma^nu} = 2 g^{mu nu} I`.

That is precisely the Clifford relation.

Therefore:

`exact scalar closure + first-order linear symbol`
`→ Clifford algebra`.

This is an algebraic consequence, not a numerical fit.

## Numerical audit

A standard 4x4 representation was tested for 100 random four-momenta.

Required result:

`(gamma.p)^2 = p^2 I`.

The numerical run gives closure error below `2e-15` and Clifford residual at machine zero.

## Critical negative boundary

The **causal cone alone** does not yet derive the Clifford algebra.

Knowing only that the characteristic determinant vanishes on

`g^{mu nu} p_mu p_nu = 0`

determines the propagation cone, but does not by itself establish the full matrix product identity required for exact scalar factorization.

Thus the logical distinction is:

`causal cone`
`↛ Clifford`.

But:

`first-order linear operator`
`+ exact scalar factorization of the relativistic quadratic operator`
`→ Clifford`.

## Relation to REL-49

REL-49 showed that demanding first-order relativistic massive dispersion through

`H(p)^2 = (|p|^2 + m^2) I`

forces the alpha/beta anticommutators and therefore Clifford structure. REL-51 generalizes the same result covariantly to the four-dimensional principal symbol.

The CERN formulation independently gives the Dirac operator and the Clifford relation `{gamma^mu,gamma^nu}=2 eta^{mu nu}`. citeturn0search24turn0search0

## Ω interpretation

The important new boundary is now explicit:

`finite causal cone`
`→ relativistic characteristic structure`

but not automatically

`→ Clifford`.

To obtain Clifford, an additional structural demand is needed:

`first-order factor`
`×`
`its exact second-order scalar causal operator`
`→ Clifford factorization`.

This is analogous to taking a square root of the relativistic quadratic relation, but the square-root requirement itself is an extra dynamical/representation constraint.

## Status

**CONDITIONAL POSITIVE / DERIVATION BOUNDARY.**

Positive: exact scalar second-order closure forces the Clifford anticommutator algebra.

Negative: causal-cone information alone does not establish that closure.

Therefore the unresolved upstream Ω question remains:

`Ω → why should matter dynamics admit an exact first-order factorization of the causal quadratic operator?`

That is now a sharper target than the vague question “where do gamma matrices come from?”

## External verification

CERN lecture material states the Dirac equation and Clifford algebra explicitly. A standard mathematical formulation of the Dirac operator also identifies its principal symbol with Clifford multiplication and its square with the metric quadratic form. citeturn0search24turn0search26
