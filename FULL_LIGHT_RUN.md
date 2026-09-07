# LIGHT — Full Physical Run

## Purpose

This document is the current complete research pass over the physical properties of light/electromagnetic radiation and their mapping onto the Ω relation-first architecture.

The central rule is strict separation:

`physical fact → standard model/equation → experiment/calculation → Ω mapping → falsification pressure`

An architectural match is not a derivation.

## 1. What light is in established physics

At the classical level, light is electromagnetic radiation described by Maxwell's equations.

At the quantum-field level, light is the electromagnetic field; a photon is a quantized excitation/mode of that field.

The photon is electrically neutral and has no invariant rest mass in the Standard Model. Its physical propagating modes have two helicity states, `+1` and `-1`.

## 2. Kinematics

Vacuum speed:

`c = 299792458 m/s` exactly.

For a monochromatic vacuum wave:

`omega = c |k|`
`nu = c/lambda`

For a photon:

`E = h nu = hbar omega`
`p = h/lambda = hbar |k|`
`E = pc`

and therefore

`E^2 = p^2 c^2`.

The invariant mass relation gives `m^2 c^4 = E^2 - p^2 c^2 = 0`.

## 3. Field structure

The vacuum electromagnetic field has electric and magnetic components. For a plane wave:

`k·E = 0`
`k·B = 0`
`E·B = 0`.

Thus the propagating vacuum mode is transverse. The field has two independent physical polarization degrees of freedom after gauge redundancy and constraints are accounted for.

## 4. Polarization

The transverse state can be linearly, circularly, or elliptically polarized.

Polarization is not an extra scalar property. It is a relation between the allowed transverse field components and their relative phase.

For circular polarization, the handedness corresponds to photon helicity `±1`.

## 5. Energy

Vacuum electromagnetic energy density:

`u = 1/2 (epsilon0 E^2 + B^2/mu0)`.

Energy flux is represented by the Poynting vector:

`S = E x H`.

With sources, the Poynting theorem includes work exchange with matter. In source-free vacuum, changes of stored field energy are balanced by boundary flux.

## 6. Momentum and stress

Electromagnetic radiation carries momentum. For vacuum fields the momentum density is related to energy flux by

`g = S/c^2`.

The Maxwell stress tensor describes momentum transport/stress and is required for a complete local energy-momentum accounting.

Therefore light does not only transport energy; it also transports momentum and can exert radiation pressure.

## 7. Causality and geometry

Vacuum light propagation follows null spacetime structure. Light cones separate events that can be causally connected from those that cannot be connected by subluminal or luminal signals.

The causal statement is stronger than the numerical value of `c`: the propagation structure constrains possible influence.

## 8. Interaction with matter

Charged matter couples to the electromagnetic field. In QED this is represented by the covariant derivative and gauge connection.

The interaction permits:

- emission;
- absorption;
- elastic and inelastic scattering;
- momentum transfer;
- energy transfer;
- phase/coherence changes.

At higher order QED also permits photon-photon scattering. Direct high-energy light-by-light scattering has been observed by ATLAS and agrees with the QED expectation.

## 9. Boundary behavior

At material interfaces, Maxwell boundary conditions and constitutive response determine reflection, transmission and refraction.

For normal incidence between simple lossless nonmagnetic media:

`r = (n1-n2)/(n1+n2)`
`R = |r|^2`.

Diffraction is wave evolution constrained by apertures/obstacles and does not require a separate classical force.

## 10. Dispersion

In vacuum the exact continuum relation is linear:

`omega = c|k|`.

In material media, constitutive response can make phase and group velocity frequency-dependent. Therefore the statement "light always travels at c" is only correct for vacuum propagation of the relevant signal/phase context; material propagation is different.

## 11. Quantum structure

Classical field modes become quantum harmonic oscillators. A mode has occupation number `n` and energy

`E_n = (n + 1/2) hbar omega`.

A photon is a one-quantum excitation above the vacuum contribution. Single-photon and other nonclassical states require quantized field operators; a classical wave amplitude is not sufficient.

## 12. Superposition, interference and coherence

Light obeys superposition in the linear regime. Interference depends on relative phase and coherence. Observable intensity contains cross terms between coherent amplitudes.

This makes phase relation physically meaningful even when an overall common phase is not directly observable.

## 13. Spectrum

The same electromagnetic field framework covers radio, microwave, infrared, visible, ultraviolet, X-ray and gamma radiation. Frequency/wavelength changes the photon energy through `E=h nu`; the underlying electromagnetic field framework remains the same.

Example photon energies using exact `c`, `h`, and `e`:

- `1 m`: `1.23984e-6 eV`
- `1 cm`: `1.23984e-4 eV`
- `1 um`: `1.23984 eV`
- `500 nm`: `2.47968 eV`
- `100 nm`: `12.3984 eV`
- `0.1 nm`: `12.3984 keV`
- `1 pm`: `1.23984 MeV`

## 14. Coupling strength

The fine-structure constant is the dimensionless low-energy electromagnetic coupling parameter. Its effective value depends on energy scale through quantum corrections (running coupling).

The dimensionless character is important for Ω analysis because it cannot be explained by merely choosing a unit system.

## 15. Completed Ω / computational tests

### REL-01
Scalar nearest-neighbour relation reproduces wave-like propagation.

### REL-01E
The same local relation also appears in the stored-energy term. Calculated energy balance is stable within the tested numerical error.

### REL-02E
A minimal transverse Maxwell discretization reproduces vacuum propagation and electromagnetic energy balance together. Measured speed was approximately `0.99936 c` in normalized units; final relative energy error was approximately `-2.39e-5`, with total energy range about `1.28e-3`.

### REL-03
Discrete U(1) link variables, plaquette curvature, covariant matter difference and gauge-invariant energy remain invariant under local gauge transformations to approximately machine precision. This establishes compatibility, not derivation of U(1).

### REL-04
Without assuming U(1), local representation freedom plus locality and representation-independent predictions create structural pressure for a connection and curvature/holonomy. The group itself is not selected.

### REL-05
The frozen continuum target is `omega=c|k|`, together with `E=hbar omega` and `p=hbar k`. The finite-difference test reproduces the continuum dispersion at long wavelengths but necessarily develops lattice dispersion near the Nyquist scale. This is a discretization effect, not a physical photon mass.

For the tested scheme with `dt/dx=0.5`, phase speed approaches `c` at small `k`; at `k=0.1 pi`, the numerical phase-speed error is about `-0.309%`, while at `k=0.01 pi` it is about `-0.00308%`.

### REL-06
The transverse field structure and two physical polarization/helicity states are compatible with the relation architecture. A full 3D numerical helicity test remains a next refinement.

### REL-07
Energy/momentum/stress structure is established physically. Energy was numerically tested; momentum/stress is documented but requires a dedicated 3D numerical conservation test for a full computational pass.

### REL-08
Reflection/refraction/diffraction fit the boundary-constraint layer. A simple normal-incidence Fresnel check gives, for `n1=1`, `n2=1.5`, `R=0.04`, `T=0.96`, with `R+T=1` in the ideal lossless case. Full FDTD interface verification remains a separate numerical test.

### REL-09
Matter coupling, absorption, emission and scattering are established QED processes and fit the state-transition/coupling layer. A quantitative transition-rate test is still required before claiming computational derivation.

### REL-10
Quantum mode/occupation structure is established QFT. Photon = quantized excitation of the electromagnetic field. Ω has not derived bosonic quantization or commutators.

### REL-11
Interference/coherence fit the relation-first distinction between alternative states and relative phase. A dedicated numerical coherence benchmark remains useful but the physical phenomenon is already established.

## 16. Full relation-first architecture after the run

The current strongest architecture is not a single scalar relation. It is a hierarchy:

`local distinction`
`→ state`
`→ local comparison`
`→ constraint`
`→ connection when local representation freedom exists`
`→ curvature / field strength`
`→ dynamics`
`→ energy + momentum`
`→ propagation`
`→ boundary matching`
`→ interaction`
`→ state transition`
`→ quantized modes`
`→ occupation/correlation`
`→ measurement/information`

## 17. What the architecture explains well

The relation-first view has strong structural compatibility with:

- propagation;
- energy storage/transfer;
- transverse field structure;
- gauge covariance;
- curvature/holonomy;
- boundary constraints;
- phase relations;
- interaction as state transition;
- mode/excitation structure.

## 18. What it does NOT yet explain

It does not yet derive from first principles:

- why the gauge group is exactly U(1);
- why spacetime has the observed dimension/signature;
- the numerical value of the fine-structure constant;
- the Maxwell kinetic term as uniquely selected;
- quantization and bosonic commutation relations;
- the exact photon helicity representation from the frozen Ω axioms;
- QED radiative corrections;
- the full matter sector and charge spectrum.

These are the real remaining barriers.

## 19. Current conclusion

The experimental chain has moved beyond the original scalar analogy. A relation-first architecture survives successive tests through scalar propagation, energy balance, vector Maxwell structure, gauge covariance, curvature, polarization, boundary behavior, quantum modes and information-bearing phase relations.

However, survival/compatibility is not derivation. The strongest scientific statement currently justified is:

> A relation-first architecture provides a compact structural language capable of representing a large fraction of the established physical organization of light, while several uniquely electromagnetic/quantum ingredients remain independent inputs.

The next decisive research target is therefore not another analogy. It is a derivation/falsification attempt: freeze the Ω axioms and ask which of `connection, group, curvature, kinetic invariant, dispersion, quantization` follow uniquely and which must be supplied externally.

## Sources / verification basis

Primary verification basis includes NIST CODATA, NIST electromagnetic energy/Poynting literature, CERN field/QED material, Particle Data Group particle listings, and Einstein Online causal-structure material.
