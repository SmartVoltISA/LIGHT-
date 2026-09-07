# REL-61 — Commutant as Relational Indistinguishability Audit

## Question

Can the commutant be interpreted as transformations that remain invisible to the currently admitted relational observables?

## Test

Three cases are compared.

### A. Single Clifford block

A 4x4 generating set is used. The commutant is computed by solving

`[X, Gamma_mu] = 0`

for all generators.

Expected result: only scalar matrices remain.

### B. Duplicated block

Use

`Gamma'_mu = Gamma_mu tensor I_2`.

The multiplicity-space operators

`I_4 tensor sigma_x`,
`I_4 tensor sigma_y`,
`I_4 tensor sigma_z`

commute with every doubled generator.

Expected result: a 4-dimensional commutant, corresponding to the full
`M_2(C)` multiplicity algebra.

### C. Relationally enriched doubled block

Admit the multiplicity operators themselves as independent relational
observables. Then an operator invisible to both the Clifford dynamics and all
three sector observables must commute with the full matrix algebra on the
multiplicity space.

Expected result: only scalar matrices remain.

## Result

The finite-matrix audit passes:

`single block → commutant dimension 1`

`duplicated block → commutant dimension 4`

`duplicated + independent sector relations → commutant dimension 1`

The explicit non-scalar multiplicity operators commute with the doubled
Clifford generators to numerical precision below `1e-12`.

## Interpretation

Within this model, the commutant has a useful relational interpretation:

`non-scalar commutant`
`→ transformation invisible to the admitted relational algebra`

Adding an independently admitted relation that distinguishes the multiplicity
space removes that internal indistinguishability and reduces the commutant to
scalars.

This gives a conditional Ω rule:

`all physically admissible independent relations included`
`+`
`no nontrivial transformation preserves all of them`
`→`
`scalar commutant`
`→`
`irreducible relational block`

## Critical boundary

The first premise is not yet derived by Ω. We still need a principled rule
that determines the complete set of physically admissible relations/observables.
Without that rule, the result is conditional and cannot be promoted to

`Ω → observable algebra → irreducibility`.

Likewise, a non-scalar commutant does not by itself prove gauge redundancy.
It only establishes indistinguishability relative to the algebra that was
actually admitted.

## Status

**Conditional positive.**

REL-61 closes the mathematical gap between relational observability and the
commutant inside the tested finite-dimensional model, while preserving the
important negative boundary that the physical observable algebra itself has
not been derived.
