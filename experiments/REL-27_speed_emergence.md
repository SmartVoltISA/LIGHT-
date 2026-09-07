# REL-27 — Can the propagation speed emerge as a relational ratio?

Date: 2026-09-07
Status: COMPLETED — scale-analysis result with explicit boundary

## Question

REL-26 gives a finite bound `v_bound = R/Δt` in graph-distance units. Can the numerical speed be determined by relational structure alone, rather than inserted as an independent constant?

## Construction

Let one relation carry an effective length `ℓ` and one elementary transition consume a time `τ`.

For a maximal local reach of `R` relations per transition,

`v_bound = R ℓ / τ`.

The dimensionless relational architecture determines the ratio `R`, but it does not by itself determine `ℓ`, `τ`, or their ratio.

We therefore tested the scale transformation

`ℓ → aℓ`

`τ → bτ`

which leaves the abstract relation/path structure unchanged while transforming

`v_bound → (a/b) v_bound`.

## Numerical check

Baseline: `R=2`, `ℓ=1`, `τ=0.5` gives `v_bound=4`.

Rescaling length by `a=3` and keeping time fixed gives `v_bound=12`.

Rescaling time by `b=2` and keeping length fixed gives `v_bound=2`.

Rescaling both with `a=b=5` leaves `v_bound=4`.

Thus identical abstract relational structure admits different numerical propagation speeds under independent unit scales.

## Result

**NEGATIVE DERIVATION RESULT:**

`RELATIONAL STRUCTURE → finite speed bound`

is supported structurally only up to

`v_bound = Rℓ/τ`.

The numerical value cannot be fixed without an additional mechanism that relates the emergent length and time scales.

## Stronger target

To derive a universal physical speed, Ω would need to generate or constrain a scale-locking relation such as

`ℓ/τ = constant`

and explain why the same ratio is invariant between admissible inertial descriptions.

## Boundary

This experiment does NOT derive the physical value of `c`, SI units, Lorentz invariance, or the existence of a universal invariant speed.

It closes a common hidden assumption: `R/Δt` is not a physical speed until spatial and temporal scales have been established and linked.

## Candidate chain

`RELATION → PATH → FINITE LOCAL REACH + POSITIVE TIME COST → BOUNDED INFLUENCE → v_bound = Rℓ/τ`

then the still-open step is

`SCALE LOCKING + FRAME INVARIANCE → UNIVERSAL SPEED`.
