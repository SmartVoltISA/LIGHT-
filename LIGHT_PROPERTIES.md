# LIGHT — Physical Properties Map

## Purpose

Build a complete, testable inventory of physical properties of electromagnetic radiation/light and map each property onto the relation-first architecture without confusing established physics with Ω interpretation.

## Status vocabulary

- `KNOWN` — established physical result/definition.
- `CALCULATED` — follows from established equations/constants.
- `OBSERVED` — experimentally measured phenomenon.
- `HYPOTHESIS` — Ω interpretation requiring independent test.
- `OPEN` — unresolved or requiring a deeper test.

## Property matrix

| Domain | Property | Physical statement | Relation-first target | Status |
|---|---|---|---|---|
| Kinematics | Vacuum speed | `c = 299792458 m/s` exactly | propagation constraint / causal limit | KNOWN |
| Wave | Frequency | `ν` characterizes temporal periodicity | temporal relation/change rate | KNOWN |
| Wave | Wavelength | `λ = c/ν` in vacuum | spatial relation scale | CALCULATED |
| Quantum | Energy | `E = hν = ħω` | excitation/state energy | KNOWN |
| Quantum | Momentum | `p = E/c = h/λ = ħk` for a photon | propagation relation + energy | KNOWN |
| Quantum | Rest mass | photon has zero invariant rest mass | null dispersion / field mode | KNOWN |
| Geometry | Null propagation | light in vacuum follows null spacetime structure | causal relation constraint | KNOWN |
| Field | Electric component | electromagnetic field has `E` | local field state | KNOWN |
| Field | Magnetic component | electromagnetic field has `B` / `H` | coupled field state | KNOWN |
| Field | Transversality | plane-wave vacuum modes have fields transverse to propagation | vector relation / constraint | KNOWN |
| Polarization | Linear/circular/elliptic | polarization encodes transverse state | internal relation between transverse components | KNOWN |
| Spin | Intrinsic angular momentum | photon is spin-1; physical massless modes have helicity ±1 | constrained internal state | KNOWN |
| Energy flow | Poynting flux | energy transport is represented by `S = E × H` | relation-mediated transfer | KNOWN |
| Energy density | Field energy | `u = 1/2(ε₀E² + B²/μ₀)` in vacuum | state/relations carrying stored energy | KNOWN |
| Interaction | Electric charge coupling | photons interact electromagnetically with charged matter | connection/coupling relation | KNOWN |
| Coupling | Fine-structure constant | `α ≈ 1/137` at low energy; EM coupling runs with scale | interaction strength | KNOWN |
| Quantum field | Photon | quantum excitation of electromagnetic field | excitation of constrained relation network | KNOWN / Ω mapping is HYPOTHESIS |
| Statistics | Boson | photon is a boson and can occupy the same quantum state | mode occupancy structure | KNOWN |
| Interference | Superposition | coherent optical amplitudes can interfere | relation between alternatives/phases | KNOWN |
| Diffraction | Spatial spreading | finite apertures/structures produce diffraction | boundary-induced relation evolution | KNOWN |
| Reflection/refraction | Boundary response | fields change according to material/boundary conditions | relation + boundary constraints | KNOWN |
| Dispersion | Medium-dependent phase/group velocity | in material, propagation depends on constitutive response | relation modified by medium state | KNOWN |
| Absorption | Energy transfer to matter | radiation can transfer energy to matter | state transition / transfer | KNOWN |
| Emission | Matter → radiation | excited matter can emit photons | state transition / excitation | KNOWN |
| Scattering | Direction/state change | photons can scatter from matter and, quantum mechanically, through higher-order EM processes | interaction relation | KNOWN |
| Coherence | Phase correlations | coherence determines interference behavior | persistent phase relation | KNOWN |
| Quantum statistics | Single-photon states | nonclassical states require quantized EM field | discrete excitation/state | KNOWN |
| Angular momentum | Total angular momentum | radiation can carry angular momentum; spin/helicity and orbital contributions must be distinguished | internal + spatial relations | KNOWN |
| Causality | No superluminal signal propagation | relativistic EM respects causal structure | global constraint on relations | KNOWN |

## Constant set to freeze

Primary numerical constants for the map:

- `c = 299792458 m/s` (exact)
- `h = 6.62607015×10^-34 J·s` (exact)
- `ħ = 1.054571817...×10^-34 J·s`
- `e = 1.602176634×10^-19 C` (exact)
- `ε₀ = 8.8541878188(14)×10^-12 F/m`
- `μ₀ = 1.25663706127(20)×10^-6 N/A²`
- `Z₀ = 376.730313412(59) Ω`
- `α ≈ 1/137` at low energy

Values follow the NIST 2022 CODATA reference currently used by the project; the next scheduled CODATA adjustment is 2026.

## Architecture map

The current research architecture must not reduce all properties to one scalar relation. The working hierarchy is:

`local state`
`→ relation / comparison`
`→ constraint`
`→ connection (when local conventions exist)`
`→ curvature / field strength`
`→ dynamics`
`→ energy + momentum`
`→ propagation`
`→ boundary interaction`
`→ state transition`
`→ observable`

Quantum layer:

`field configuration`
`→ mode decomposition`
`→ quantization`
`→ photon excitation`
`→ occupation / correlation`
`→ measurement statistics`

## Required Ω tests

1. `REL-04`: determine whether connection/curvature/invariant structure can be motivated without importing U(1) as an unexplained axiom.
2. `REL-05`: derive or fail to derive dispersion `E² = p²c²` / massless propagation from the frozen architecture.
3. `REL-06`: test polarization as an internal relation/constraint, including helicity ±1.
4. `REL-07`: test energy-momentum flow and stress-energy structure, not energy alone.
5. `REL-08`: test boundary interaction: reflection, refraction, diffraction.
6. `REL-09`: test matter coupling and emission/absorption.
7. `REL-10`: test quantum mode/occupation structure and distinguish it from classical wave behavior.
8. `REL-11`: test interference/coherence and information-bearing state distinctions.

## Hard boundary

A successful architectural mapping is not a derivation. Every property must retain an explicit physical source, equation, measurement status, and falsification criterion.
