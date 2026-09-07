# REL-21 — Relational requirements and metric countermodels

## Question

Can the weak relational requirements

`DISTINCTION + RELATION + ORDER + BOUNDARY + LOCALITY`

uniquely derive Lorentzian spacetime geometry and a finite invariant propagation speed?

## Construction

Two compatible kinematic models are compared.

1. **Galilean countermodel**
   - absolute ordered time: `t' = t`;
   - spatial transformation: `x' = x - vt`;
   - local propagation remains representable as ordered local transitions;
   - a signal speed transforms as `u' = u - v`.
   - Therefore no nonzero finite speed is invariant under arbitrary boosts.

2. **Lorentz positive control**
   - `t' = γ(t - vx/c²)`;
   - `x' = γ(x - vt)`;
   - `γ = 1/sqrt(1-v²/c²)`;
   - Minkowski interval `c²t² - x²` is invariant.

## Numerical result

For boosts `v ∈ {0.2, 0.5, 0.8}` and three spacetime samples, the maximum Lorentz interval error was approximately

`1.61 × 10^-15`.

For the Galilean countermodel, the tested signal speeds changed under nonzero boosts; the maximum tested change was `0.7`.

## Result

**NEGATIVE DERIVATION RESULT.**

The weak relational requirements do not uniquely select Lorentzian geometry.
They admit at least a Galilean countermodel. Therefore the following must enter as an additional physical/kinematic constraint if Lorentz structure is to be obtained:

`RELATIONAL REQUIREMENTS + RELATIVITY/CAUSAL-CONE CONSTRAINT → LORENTZIAN STRUCTURE`

A finite invariant propagation speed `c` is not derived by this experiment. It is part of the additional constraint.

## What is closed

The previous gap is now classified precisely rather than left ambiguous:

- Lorentzian metric: **not derived from the weak relational set**.
- invariant speed `c`: **not derived from the weak relational set**.
- Minkowski interval: **conditional consequence once Lorentz kinematics is supplied**.
- low-speed Newtonian limit: remains a consequence of the supplied Lorentz structure.

## Ω status

This is a **boundary result**, not a failure of the architecture. It identifies the minimum missing class of assumptions that must be independently derived or explicitly promoted as physical input.

It prevents circular reasoning: the Lorentz metric and `c` must not be smuggled into the relation architecture and then reported as predictions.
