# CHANGELOG

## 2026-09-07 — LIGHT v1.0

- Added `experiments/REL-15_memory_inertia_action_test.py`.
- Added `experiments/REL-15_memory_inertia_action_test.md`.
- REL-15 tests the proposed chain from retained history/memory to inertia and action.
- A memoryless first-order response has no post-impulse persistence.
- A second-order retained dynamical state produces inertial persistence with `Δv=J/m`.
- The free-particle action `L=1/2 m v²` gives `p=mv` and constant momentum.
- Result: retained dynamical state supports an inertia mapping, but generic memory does not derive mass.
- Important boundary: the coefficient `m` remains an input of the tested mechanical action; physical mass generation is not derived.
- Updated `LIGHT_HYPOTHESES.md` with H5k.

## 2026-09-07 — LIGHT v0.9

- Added `experiments/REL-14_group_selection_pressure.py`.
- Added `experiments/REL-14_group_selection_pressure.md`.
- REL-14 compares representation/transport structures for R+, U(1)/SO(2), SO(3), and GL(2,R) without selecting U(1) as the target.
- Raw local comparison is representation-dependent across all tested families.
- Compensating transport restores covariance to machine precision for all tested families.
- Transport composition also closes to machine precision.
- SO(3) and GL(2,R) expose non-trivial commutator structure, while R+ and U(1)/SO(2) commute in the tested construction.
- Result: minimal local covariance + transport requirements do not select U(1). This is recorded as an explicit negative selection result.

## 2026-09-07 — LIGHT v0.8

- Added `experiments/REL-13_representation_agnostic_connection_test.py`.
- Added `experiments/REL-13_representation_agnostic_connection_test.md`.
- REL-13 tests local positive-real rescaling, complex phase, and SO(2) rotation without selecting one physical gauge group as the target.
- Raw nearest-neighbour comparison fails covariance for all three representation families.
- A local transport/connection constructed from neighboring representation maps restores covariance to machine precision.
- Result: connection pressure is representation-agnostic across the tested families; this does not select U(1), SO(2), or any physical gauge group.

## 2026-09-07 — LIGHT v0.7

- Added `experiments/REL-12_external_input_audit.md`.
- Added executable `experiments/REL-12_external_input_audit.py`.
- REL-12 audited which parts of the light/QED stack are produced by relation-first structure and which remain external inputs.
- Controlled local-representation test: raw finite differences fail covariance under spatially varying local phase (`~2.36e-2`), while the compensating connection restores covariance to `~2.29e-16`.
- Independent lattice-curvature cross-check remains invariant to `~1.11e-15`.
- Conclusion: connection-like structure is strongly motivated by representation-independent local comparison, but the experiment does not derive U(1).
- Explicit external-input boundary: U(1), spacetime geometry, Maxwell/QED kinetic dynamics, hbar/quantization, bosonic commutators, alpha and matter charge spectrum remain un-derived.

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

- Added `LIGHT_PROPERTIES.md` and `FULL_LIGHT_RUN.md`.
- Completed the physical-property inventory and relation-first mapping.
- Added the planned REL-05–REL-11 analysis layer.
- Fixed the scientific boundary: architectural compatibility is not derivation.

## 2026-09-07 — LIGHT v0.4

- Added the discrete U(1) gauge/connection test and recorded H5d.
- Fixed the boundary: U(1) remains an input from established QED, not an Ω derivation.

## 2026-09-07 — LIGHT v0.3

- Added energy relation tests and recorded H5c.

## 2026-09-07 — LIGHT v0.2

- Added QFT_CORE, GAUGE_STRUCTURE, LAGRANGIAN, MINIMAL_STRUCTURE, DERIVATION_CHAIN and LIGHT_HYPOTHESES.

## 2026-09-07 — LIGHT v0.1

- Created the fundamental LIGHT research framework.
