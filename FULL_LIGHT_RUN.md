# LIGHT — Full Physical Run

## Purpose

Complete research pass over physical properties of electromagnetic radiation/light and their mapping onto the Ω relation-first architecture.

Rule: `physical fact → standard model/equation → experiment/calculation → Ω mapping → falsification pressure`.

An architectural match is not a derivation.

## Established physical structure

Light is electromagnetic radiation; in QFT the photon is a quantized excitation of the electromagnetic field. Vacuum propagation is null, photons are massless, physical photon modes have two helicities, and electromagnetic radiation carries energy, momentum and angular momentum.

Core kinematics:

`ω = c|k|`
`ν = c/λ`
`E = hν = ħω`
`p = ħk = h/λ`
`E = pc`
`E²-p²c²=0`.

Plane-wave vacuum constraints:

`k·E=0`, `k·B=0`, `E·B=0`, `|B|=|E|/c`.

Energy density and flow:

`u = 1/2(ε₀E²+B²/μ₀)`
`S = E×H`
`g=S/c²`.

Boundary behavior includes reflection, transmission, refraction and diffraction. Matter coupling includes emission, absorption and scattering. Quantum structure adds mode occupation, single-photon states, interference/coherence and QED corrections.

## Experimental chain

### REL-01 / REL-01E
Scalar nearest-neighbour relation reproduces wave-like propagation and stable numerical energy accounting. Supportive at the tested numerical layer.

### REL-02E
Minimal transverse Maxwell discretization reproduces vacuum propagation and energy balance. Measured propagation speed ≈ `0.99936 c`; final relative energy error ≈ `-2.39e-5`; full energy range ≈ `1.28e-3`.

### REL-03
Discrete U(1) link connection, plaquette curvature, covariant comparison and gauge-invariant energy remain invariant under local gauge transformations to machine precision. Compatibility only; U(1) remains an external QED input.

### REL-04
Removing U(1) while retaining locality, local representation freedom and representation-independent predictions creates structural pressure for a connection and curvature/holonomy. The group itself is not selected.

### REL-05 — dispersion and massless kinematics
Frozen Yee-like 1D scheme with `c=1`, `dx=1`, `dt=0.5` obeys

`sin²(ωdt/2)=(c dt/dx)² sin²(kdx/2)`.

Numerical phase-speed ratio `ω/(ck)`:

- `k/π=0.01`: `0.999969157` → `-0.0030843%`
- `k/π=0.10`: `0.996911009` → `-0.308899%`
- `k/π=0.50`: `0.920213825` → `-7.97862%`
- `k/π=0.90`: `0.730705245` → `-26.9295%`

This cleanly separates continuum physics from lattice discretization: the long-wavelength limit approaches `ω=ck`, while high-k modes acquire numerical dispersion. A quantum compatibility check using `E=ħω`, `p=ħk` gives `E²-p²c²=0` for the continuum massless relation. It does not derive `ħ`.

### REL-06 — polarization/helicity structure
A transverse field with two independent components supports linear, elliptic and circular polarization. The normalized handedness invariant used in the test is `S3/S0 = 2AxAy sin(δ)/(Ax²+Ay²)`.

Results:

- linear: `0`
- elliptic test: `0.692820323`
- circular +: `+1`
- circular −: `−1`

For the ideal plane-wave construction, `E·B=0` and `cB/E=1` to numerical precision. This is a structural polarization test, not a derivation of the photon representation; a full 3D Lorentz/helicity test remains open.

### REL-07 — energy-momentum consistency
Using 2022 CODATA vacuum constants and a unit-amplitude plane wave:

`u = 8.85418781879e-12 J/m³`
`S = 2.65441872979e-3 W/m²`
`S/(uc) = 0.999999999999403`
`g = 2.95343914849e-20 kg/(m² s)`
`g/(u/c) = 0.999999999999403`
`c²μ₀ε₀ = 1.0000000000011935`.

Thus the energy-flow/momentum-density relations are numerically consistent with the frozen constants. A full spatial stress-tensor conservation test remains open.

### REL-08 — boundary response
Normal-incidence Fresnel tests for ideal lossless nonmagnetic media give:

- `n1=1,n2=1.5`: `R=0.04`, `T=0.96`, `R+T=1`
- `n1=1,n2=2`: `R=0.111111111`, `T=0.888888889`
- `n1=1.5,n2=2`: `R=0.0204081633`, `T=0.979591837`
- equal media: `R=0`, `T=1`.

This supports the boundary-constraint layer analytically/numerically. Full FDTD interface and diffraction simulations remain open.

### REL-09
Emission, absorption and scattering are established QED processes and fit the interaction/state-transition layer. Quantitative transition-rate calculation is still required for a computational test.

### REL-10
Quantized modes, photon occupation and bosonic statistics are established QFT. Ω has not derived commutation relations or bosonic quantization.

### REL-11
Interference and coherence fit the relation-first distinction between alternative states and relative phase. Dedicated numerical coherence benchmarking remains useful.

## Architecture after the run

`local distinction → state → comparison → constraint → connection → curvature/field strength → dynamics → energy+momentum → propagation → boundary → interaction → state transition → modes → quantization → occupation/correlation → measurement/information`.

## Hard unresolved barriers

The architecture still does not derive from frozen Ω axioms:

1. exact gauge group U(1);
2. spacetime dimension/signature;
3. unique Maxwell kinetic invariant;
4. numerical value of `α`;
5. quantum commutation/bosonic quantization;
6. exact photon helicity representation;
7. QED radiative corrections;
8. matter charge spectrum.

These are now the principal falsification/derivation targets rather than additional descriptive properties.

## Current scientific conclusion

The relation-first architecture survives a progressively richer chain of tests from scalar propagation through energy, vector Maxwell structure, gauge covariance, curvature, dispersion, polarization, energy-momentum and boundary constraints. The evidence supports **structural compatibility and computational representation**, not derivation of electromagnetism from Ω.

The decisive next move is to freeze the Ω axioms and attempt to recover the missing electromagnetic/quantum structures without inserting them by hand.

## Verification basis

NIST 2022 CODATA and fundamental-constant database; CERN QED/gauge/polarization material; standard Maxwell/QED equations and experimentally established phenomena.
