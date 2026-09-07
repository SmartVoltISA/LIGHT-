# REL-28 — Speed-number audit

Date: 2026-09-07
Status: COMPLETED — exact physical value identified; Ω derivation boundary preserved

## Question

What numerical value must the relational propagation bound reproduce if the relational length and time scales are calibrated to SI physical units?

## Reference value

The current CODATA 2022 recommended value is

`c = 299792458 m/s`

with exact status in SI. NIST identifies the 2022 CODATA set as the latest available recommended constants database.

## Relational speed law

REL-27 gives the structural form

`v = ell / tau`

for one relation of physical length `ell` traversed in minimum physical time `tau`, or more generally

`v_bound = R ell / (N tau)`

for bounded reach `R` over `N` elementary updates when the time bound is `N tau`.

To reproduce the physical vacuum light speed, the scale relation must satisfy

`ell / tau = 299792458 m/s`.

Therefore, for any chosen relational length scale `ell`,

`tau = ell / 299792458 s`.

Examples:

`ell = 1 m -> tau = 3.3356409519815204e-9 s`

`ell = 1 mm -> tau = 3.3356409519815204e-12 s`

`ell = 1 um -> tau = 3.3356409519815204e-15 s`

## Independent electromagnetic cross-check

For vacuum Maxwell propagation,

`c = 1 / sqrt(mu0 epsilon0)`.

Using the CODATA 2022 values,

`mu0 = 1.25663706127e-6 N A^-2`

`epsilon0 = 8.8541878188e-12 F m^-1`

and the resulting value agrees with the exact SI value within the rounding of the displayed constants.

## Result

**NUMERICAL RESULT:**

`c = 299792458 m/s`.

**STRUCTURAL RESULT:**

The Ω relational model can represent this value as a propagation-scale ratio `ell/tau`, but the absolute SI length/time calibration is not derived by REL-28.

## Critical boundary

The experiment does NOT claim to predict the digits `299792458` from Ω primitives alone.

It establishes the exact numerical target that a future derivation must reproduce and separates:

1. emergence of a finite speed ratio;
2. universality/frame invariance of that ratio;
3. calibration to SI meters and seconds;
4. the numerical value `299792458`.

Only (1) is structurally supported by REL-26/27. (2)-(4) require additional physical structure/calibration at this stage.

## Next target

Attempt to derive the scale ratio from electromagnetic relational constants already present in LIGHT, rather than inserting `c` directly. In particular test whether the relation between electric and magnetic sectors constrains a universal propagation ratio and whether that ratio can be connected to `mu0 epsilon0` without circularly using `c`.