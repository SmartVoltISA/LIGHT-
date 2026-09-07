# REL-55 — Closure versus irreducibility selection audit

## Question

Can a closure requirement select the irreducible Clifford carrier, rather than irreducibility being inserted as an independent axiom?

## Construction

Use a concrete 4-component complex Clifford carrier in 3+1 dimensions and form k identical copies:

`S_k = S_4 ⊗ C^k`

with generators

`Γ^μ_k = Γ^μ ⊗ I_k`.

The multiplicity space is invisible to the Clifford action. Its operators therefore commute with every `Γ^μ_k`.

The relevant diagnostic is the commutant:

`Comm(Γ_k) = {X : XΓ^μ_k = Γ^μ_kX for all μ}`.

For one irreducible copy the commutant is scalar. For k identical copies its complex dimension is `k²`, corresponding to arbitrary operators on the multiplicity space.

## Numerical result

For multiplicities `k = 1, 2, 3` the computed commutant dimensions are:

`k=1 -> 1`

`k=2 -> 4`

`k=3 -> 9`

matching `dim Comm = k²` exactly at numerical rank tolerance.

Thus the doubled and tripled systems contain genuine internal operators that are invisible to the Clifford generators.

## Interpretation

A scalar-commutant criterion selects one copy:

`Comm = C·I`

`=> k=1`

and excludes independent multiplicity sectors.

This gives a precise mathematical formulation of “no unused internal structure”. It is closely related to Schur's lemma: for an irreducible complex representation, the commutant is scalar. Standard representation theory also identifies the commutant as the object encoding decomposition/multiplicity structure. citeturn0search25turn0search24

## Critical boundary

The experiment does **not** derive the scalar-commutant criterion from the upstream Ω primitives.

Therefore we must not claim:

`Ω -> closure -> irreducibility`

as established.

What is established is the conditional statement:

`exact Clifford carrier + scalar-commutant closure criterion`
`-> irreducibility`
`-> no independent multiplicity sector`
`-> minimal Clifford carrier`.

The missing upstream principle is now explicit:

`DISTINCTION -> RELATION -> STATE -> TRANSITION -> CONSTRAINT -> CLOSURE`

`?`

`-> scalar commutant / irreducibility`

The `?` remains unresolved.

## Relation to previous experiments

REL-52 showed that finite causal propagation and generic first-order evolution do not uniquely select Dirac/Clifford.

REL-53 showed that exact first-order factorization plus the relativistic quadratic dispersion selects the Clifford relations, with the 4-component massive realization minimal in the tested class.

REL-55 now shows that even after Clifford selection, irreducibility/minimal multiplicity is a distinct structural condition. It cannot be silently identified with “closure” without defining and deriving that closure principle.

## Status

**CONDITIONAL POSITIVE:** a scalar-commutant closure criterion selects the irreducible carrier.

**NEGATIVE / UNRESOLVED:** the scalar-commutant criterion has not been derived from Ω itself.

This boundary is intentional and is part of the result.
