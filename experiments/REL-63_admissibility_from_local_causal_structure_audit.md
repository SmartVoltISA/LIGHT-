# REL-63 — Admissibility from Local Causal Structure Audit

## Question

Can locality and future-effect relevance jointly select a physical relation
family and remove the ambiguity exposed by REL-62?

## Construction

Relations are assigned a support distance and a future-effect flag:

`x_local`: distance 0, future-relevant

`neighbor`: distance 1, future-relevant

`hidden_global`: distance 10, future-relevant

`constant`: distance 0, not future-relevant

Two filters are compared.

## Results

Future-effect relevance alone selects:

`x_local + neighbor + hidden_global`

Adding a locality radius of 1 selects:

`x_local + neighbor`

The nonlocal counterexample is removed, while a local relation with no future
effect remains excluded.

## Interpretation

This demonstrates a useful conditional principle:

`locality + independently relevant future effect`
`→ narrower admissible relational family`.

It does not demonstrate:

`Ω → locality`

nor:

`locality → unique complete observable algebra`.

Locality must itself be justified as a physical admissibility requirement.
Moreover, this toy construction does not address gauge invariance, boundary
conditions, quantum completeness, or continuum limits.

## Status

**Conditional positive, with explicit boundary.**

REL-63 reduces the ambiguity of REL-62 by adding a physically meaningful
locality criterion, but the criterion remains an input at this stage.
