# CHANGELOG

## 2026-09-07 — LIGHT v0.6

- Added `experiments/REL-05_dispersion_kinematics_test.py`.
- Added `experiments/REL-06_polarization_helicity_test.py`.
- Added `experiments/REL-07_energy_momentum_test.py`.
- Added `experiments/REL-08_boundary_fresnel_test.py`.
- Extended `FULL_LIGHT_RUN.md` with quantitative REL-05 to REL-08 results.
- Updated `LIGHT_HYPOTHESES.md` with H5e–H5h.
- REL-05: long-wavelength phase speed approaches `c`; high-k lattice dispersion is explicitly separated from physical photon dispersion.
- REL-06: tested transverse polarization states produce normalized circular handedness `+1/-1`.
- REL-07: plane-wave energy flux and momentum density agree with `S=uc` and `g=u/c` to approximately `6e-13` relative error using frozen CODATA constants.
- REL-08: ideal lossless Fresnel cases preserve `R+T=1`.
- Strict boundary preserved: these tests do not derive U(1), `hbar`, quantization, `alpha`, or spacetime geometry.

## 2026-09-07 — LIGHT v0.5

- Added `LIGHT_PROPERTIES.md`: full physical-property inventory and relation-first mapping.
- Added `FULL_LIGHT_RUN.md`: complete pass over kinematics, fields, energy, momentum, polarization, causality, interaction, boundaries, quantum structure, interference and information.
- Added the planned REL-05–REL-11 analysis layer.
- Fixed the scientific boundary: architectural compatibility is not derivation.

## 2026-09-07 — LIGHT v0.4

- Added `experiments/REL-03_gauge_relation_test.py`: discrete U(1) gauge/connection test.
- Added `experiments/REL-03.md`: connection, covariant relation, curvature and gauge-invariant energy.
- Recorded H5d: relation-first architecture is compatible with a discrete U(1) gauge/connection layer at the tested numerical level.
- Fixed the boundary: U(1) remains an input from established QED, not an Ω derivation.

## 2026-09-07 — LIGHT v0.3

- Added `ENERGY_RELATION.md` and the REL-01E / REL-02E energy tests.
- Recorded H5c: vector structure, propagation and energy balance survive at the tested numerical layer.
- Kept gauge/connection, sources, full 3D structure and quantum layer as separate tests.

## 2026-09-07 — LIGHT v0.2

- Added QFT_CORE, GAUGE_STRUCTURE, LAGRANGIAN, MINIMAL_STRUCTURE, DERIVATION_CHAIN and LIGHT_HYPOTHESES.
- Fixed distinction between mathematical relation/analogy and physical fact.

## 2026-09-07 — LIGHT v0.1

- Created the fundamental LIGHT research framework.
- Fixed FIELD, PHOTON, PROPAGATION, INTERACTION, GEOMETRY and Ω_MAPPING.
- Added experimental plan and fact/model/hypothesis separation.
