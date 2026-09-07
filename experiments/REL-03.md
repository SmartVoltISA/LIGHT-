# REL-03 — Gauge / Connection / Relation

## Purpose

Test whether the relation-first architecture survives the gauge/connection layer instead of stopping at scalar differences or Maxwell propagation.

## Frozen discrete model

Use a periodic 2D lattice.

- site state: charged phase `psi(x)`
- local gauge state: `g(x) = exp(i alpha(x))`
- connection on an oriented link: `U_mu(x) in U(1)`
- gauge transformation:
  `U_mu(x) -> g(x) U_mu(x) g*(x+mu)`
- covariant relation:
  `D_mu psi = U_mu(x) psi(x+mu) - psi(x)`
- curvature / accumulated relation around a plaquette:
  `P = U_x(x) U_y(x+x) U_x*(x+y) U_y*(x)`
- gauge-field energy diagnostic:
  `E = sum_x [1 - Re(P_x)]`

This is the discrete U(1) connection/curvature structure. In the continuum limit it corresponds structurally to a gauge potential and field strength.

## Why this is the correct pressure test

A plain difference between scalar values is insufficient here. The object connecting neighbouring local states must transform with the local phase conventions. The link variable is therefore treated as a connection, while the plaquette is the gauge-invariant accumulated relation.

This is directly consistent with standard QED: local U(1) invariance introduces the gauge field and covariant derivative, while `F_mu nu` is the gauge-invariant field-strength object. CERN's QFT notes explicitly give the local U(1) transformation of `A_mu`, the covariant derivative, and `F_mu nu = d_mu A_nu - d_nu A_mu`.

## Calculated result

For `N = 32`, random fixed seed `7`:

- maximum plaquette invariance error: approximately `6.75e-16`
- maximum covariant-difference error: approximately `4.97e-16`
- gauge-field energy before transformation: approximately `883.4267418564`
- gauge-field energy after transformation: approximately `883.4267418564`
- relative energy error: at floating-point roundoff level

Thus the gauge transformation changes the representation of the local connection but leaves the curvature diagnostic and gauge-invariant energy unchanged.

## Interpretation

REL-03 supports a stronger structural statement than REL-02:

`local state convention -> connection -> accumulated relation/curvature -> invariant observable`

The relation-first architecture therefore survives the introduction of a genuine gauge redundancy in this discrete U(1) test.

But this is still **not** a derivation of QED from Ω. The test starts from the U(1) group and its lattice connection structure. It verifies compatibility of the relation architecture with gauge theory; it does not derive the choice of U(1) from a more primitive Ω principle.

## Falsification pressure

The universal claim becomes weaker if the relation schema cannot retain gauge covariance and gauge-invariant observables without changing its core definitions. Conversely, passing REL-03 does not prove universality: the next question is whether U(1) itself can be selected or derived from the same frozen architecture rather than inserted as domain-specific input.

## Status

`CALCULATED / SUPPORTIVE / NOT PROOF`

Next pressure test: separate what is genuinely universal (`state -> relation -> transformation law -> invariant`) from what has been imported specifically from electromagnetism (`U(1)`).
