# REL-43 — U(1) selection audit

**Date:** 2026-09-07  
**Branch:** `rel-41-actual`  
**Status:** negative result / global-structure gap identified

## Question

After REL-42, can the connection/curvature structure itself select the electromagnetic gauge group U(1), rather than merely an abelian internal structure?

## Structural input

The previous chain gives:

`transverse sector → curl → constraint preservation → potential → redundancy → curvature`

In gauge-theory language a connection has curvature. For a general non-Abelian group,

`F = dA + A ∧ A`,

where the commutator term carries the non-Abelian structure. For an Abelian group the bracket vanishes and

`F = dA`.

This distinction is standard: U(1) is Abelian, while general Yang–Mills curvature contains the commutator term. citeturn0search22turn0search23

## Test

Impose only:

1. local connection/transport structure;
2. gauge redundancy;
3. curvature as the gauge-invariant local field strength;
4. one independent internal generator / one gauge-field component;
5. commuting internal transformations.

A one-dimensional Lie algebra is necessarily Abelian. Thus the local algebra is reduced to an Abelian one-dimensional algebra.

But this does **not** uniquely determine the global group.

Two explicit candidates have the same local algebra:

### A. Additive real group R

`lambda ∈ R`

`A → A + d lambda`

`F = dA`

The parameter is non-periodic.

### B. Compact phase group U(1)

`lambda ~ lambda + 2π`

`A → A + d lambda`

`F = dA`

The parameter is periodic.

Locally these structures have the same one-dimensional Lie algebra and the same Abelian curvature construction. Electromagnetism is conventionally formulated as a U(1) gauge theory, with `F=dA` in the Abelian case. citeturn0search1turn0search24

## Numerical sanity check

The supplied 1D internal representation uses scalar multiples of the identity. The commutator is numerically zero to floating-point precision, confirming the intended Abelian local algebra. The code does not claim that numerical linear algebra can prove global group topology; that distinction is the point of the experiment.

## Result

**NEGATIVE RESULT.**

The chain

`connection + curvature + one internal commuting degree of freedom`

determines at most a **one-dimensional Abelian gauge algebra**.

It does **not** by itself select the global compact group U(1).

To select U(1), an additional global condition is required, for example:

- compactness of the internal phase;
- periodicity of the gauge parameter;
- an equivalent charge/phase quantization condition.

Thus:

`Ω local structure → Abelian 1D gauge algebra`

is supported as a structural narrowing, while

`Abelian 1D algebra → U(1)`

requires an additional global physical/topological input.

## Important consequence

This is a sharper boundary than simply saying "U(1) is an assumption".

The local Ω chain can narrow the possibilities to an Abelian one-dimensional gauge structure if the single-component/commuting requirements are independently justified.

The remaining missing ingredient is **global compactness/periodicity**, not the local curvature construction.

## Boundary

This experiment does not derive:

- why there is exactly one internal generator;
- why the internal group is compact;
- charge quantization;
- the numerical electromagnetic coupling;
- the electron representation;
- quantum electrodynamics;
- the SI normalization.

Those remain separate tests.
