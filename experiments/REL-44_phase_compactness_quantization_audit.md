# REL-44 — Phase compactness / quantization audit

**Date:** 2026-09-07  
**Status:** boundary identified / conditional positive result

## Question

Can the quantum phase structure exclude the non-compact additive group R and select compact U(1) after REL-43?

## Local equivalence

At the infinitesimal level, R and U(1) have the same one-dimensional abelian Lie algebra. The local transformation of a connection has the same form,

`A -> A + dλ`,

and the Abelian curvature is

`F = dA`.

Therefore local connection/curvature data cannot distinguish R from U(1).

## Global quantum test

For a charged state,

`ψ -> exp(i q λ) ψ`.

For compact U(1), the group parameter is periodic:

`λ ~ λ + 2π`.

Single-valuedness requires

`exp(i q (λ + 2π)) = exp(i q λ)`

and hence

`exp(i 2π q) = 1`.

Therefore, in minimal-charge units,

`q ∈ Z`.

For the non-compact group R there is no identification `λ ~ λ + 2π`, so arbitrary real q remains locally consistent.

## Numerical audit

Tested q values:

`0, 1, -1, 2, 1/2, sqrt(2)`.

Integer values satisfy the U(1) periodicity test; non-integer values do not under the chosen minimal-charge normalization. All real q remain admissible for the non-compact R transformation because no periodic identification is imposed.

## Result

**CONDITIONAL POSITIVE RESULT.**

Quantum single-valuedness **plus a periodic internal phase** excludes the non-compact R realization and yields the compact U(1) charge lattice.

But the crucial logical point is:

`periodicity / compactness`

is a **global quantum input**. It is not derived from the preceding local Ω chain.

Thus the strongest justified chain is:

`Ω local structure`
`→ connection`
`→ curvature`
`→ 1D abelian Lie algebra`

then, with the additional quantum-global condition

`periodic phase`
`→ single-valued quantum state`
`→ charge quantization`
`→ compact U(1)`.

## External check

The relation between charge quantization and compactness of the gauge group is a standard result discussed by Yang. Geometric-quantization treatments likewise connect charge quantization with the U(1) gauge structure of electromagnetism. citeturn0search0turn0search5

## Boundary

REL-44 does **not** claim to derive compactness from classical locality alone. It identifies the precise additional global quantum condition required to select U(1) over R.
