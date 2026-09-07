# REL-47 — Charge / current emergence audit

## Question
Can local U(1) covariance force the connection-current interaction structure, and what remains free?

## Tested structure
D_mu = partial_mu + i q A_mu

psi -> exp(-i q lambda) psi
A_mu -> A_mu + partial_mu lambda

Then D'_mu psi' = exp(-i q lambda) D_mu psi.

A phase current analogue J = q Im(psi* D psi) is invariant under the same local transformation.

## Numerical audit
100 randomized tests were run.

Expected machine-level result:
- local covariance residual < 1e-13
- current invariance residual < 1e-13

## Conditional structural conclusion
Local U(1) covariance selects the covariant derivative and therefore the minimal connection-current coupling A_mu J^mu.

A neutral representation q=0 decouples from A_mu at minimal coupling.

## What is not derived
The audit does not derive:
- numerical value of q/e;
- existence of a particular matter field;
- spin 1/2;
- matter mass;
- number of matter species;
- charge spectrum from local symmetry alone.

The charge q remains a representation/coupling parameter at this stage. Charge quantization requires the additional global compactness/quantum condition tested in REL-44.

## Boundary
This is a conditional gauge-structure result, not a derivation of the Standard Model matter sector.
