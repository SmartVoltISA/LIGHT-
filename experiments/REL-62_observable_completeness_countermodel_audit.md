# REL-62 — Observable Completeness Countermodel Audit

## Question

Can Omega derive a unique physical observable algebra from relational structure
by requiring that every independently relevant relation be represented?

## Construction

Finite states carry two relational attributes:

`x`

and

`hidden`.

Future effects are

`future(s,a) = x + a*hidden`

for `a ∈ {-1,0,1}`.

Three candidate observation families are compared:

`X-only = {x}`

`full = {x, hidden}`

`parity = {x, hidden mod 2}`.

The operational quotient identifies states that have identical admitted
observations and identical future effects for all tested actions.

## Results

For the base state set:

`X-only` gives fewer operational classes than the full relational description.

`full` gives one class per state.

For a larger hidden-state set, `parity` still produces fewer classes than the
full relation family.

Thus an operational quotient is perfectly well-defined once the admissible
experiment/observable family is fixed.

## Critical countermodel

The quotient itself does not determine which relation family is admissible.
Different families can be internally consistent and closed under the same
operational construction while retaining different amounts of relational
information.

Therefore the attempted implication

`future-effect relevance → unique observable algebra`

fails in this toy model.

## Consequence for Ω

We have now isolated the missing premise precisely:

`RELATION → PHYSICAL OBSERVABLE`

cannot be obtained from future-effect relevance alone.

A further physical admissibility principle is required, for example a rule
based on locality, operational accessibility, invariance, conservation,
causal influence, or another independently justified criterion.

This is a useful negative result rather than a failure of the program: it
prevents us from smuggling the observable algebra into Ω through a vague word
such as "relevant".

## Current strongest chain

`DISTINCTION`
`→ RELATION`
`→ STATE`
`→ HISTORY`
`→ FUTURE EFFECT`
`→ OPERATIONAL EQUIVALENCE`
`→ QUOTIENT`
`→ PHYSICAL RELATIONAL CONTENT`
`→ COMMUTANT`
`→ CONDITIONAL IRREDUCIBILITY`

The arrow

`RELATION → COMPLETE OBSERVABLE ALGEBRA`

remains unresolved.

## Status

**Negative / boundary result.**

Operational quotienting is well-defined after the admissible experiment set
is supplied, but relational future-effect closure does not uniquely determine
that set.
