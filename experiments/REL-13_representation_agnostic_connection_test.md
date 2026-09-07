# REL-13 — Representation-agnostic connection pressure

## Question

Does the need for a local comparison/transport rule survive when the local representation is changed without selecting U(1) in advance?

## Frozen setup

A local state is transformed by a position-dependent representation map `T(x)`. The physical comparison should transform consistently with the state at the starting point.

Tested representation families:

1. positive real local rescaling `T(x) ∈ R_{>0}`;
2. complex phase `T(x) = exp(i α(x))`;
3. two-component `SO(2)` local rotation.

No claim is made that any one of these is the physical electromagnetic group.

## Test

Raw comparison:

`Δ_raw q = q(x+dx) - q(x)`.

Target covariance:

`Δ_target = T(x)[q(x+dx)-q(x)]`.

A local transport map is constructed from neighboring representation maps:

`U(x,x+dx) = T(x) T(x+dx)^(-1)`.

Then:

`Δ_cov q = U(x,x+dx) q'(x+dx) - q'(x)`.

## Numerical results

| Representation | Raw comparison error | Covariant comparison error |
|---|---:|---:|
| positive real scaling | `2.825116e-02` | `2.706169e-16` |
| complex phase | `2.362070e-02` | `3.236829e-16` |
| SO(2) rotation | `3.528319e-02` | `3.608225e-16` |

All three raw comparisons fail covariance at a macroscopic numerical level. The compensating transport rule restores covariance to machine precision.

## Interpretation

This is stronger than REL-12 in one specific sense: the connection pressure does not depend on choosing complex phase/U(1) as the representation family. The same structural problem appears for real rescaling and SO(2) rotation.

The result supports the abstract pattern:

`local representation freedom → neighbor comparison problem → transport/connection rule`.

It does **not** determine:

- U(1);
- SO(2) versus another group;
- compactness;
- the physical electromagnetic coupling;
- Maxwell dynamics;
- quantum mechanics.

Indeed, the complex U(1) and real SO(2) cases are locally isomorphic, so this test cannot distinguish them.

## Falsification pressure

The structural claim would weaken if a nontrivial position-dependent representation class admitted a local, representation-independent comparison rule without an equivalent transport/connection object, while preserving locality and nontrivial transformations.

## Status

**STRUCTURAL SUPPORT — REPRESENTATION-AGNOSTIC CONNECTION PRESSURE**

Not a derivation of electromagnetism.
