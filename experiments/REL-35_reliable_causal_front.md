# REL-35 — Reliable causal front under path diversity

Date: 2026-09-07
Status: COMPLETED — toy-model separation test

## Question

Can path diversity improve the reliability and effective reach of a causal signal without increasing the maximum speed of the causal front?

## Model

A controllable binary intervention propagates through local transitions.

Each local hop has:

`reach = 1`

`time >= tau`

and independently flips the bit with probability `p`.

For a path of `N` hops, the effective crossover probability is

`eps_N = [1 - (1 - 2p)^N] / 2`.

For an odd number `K` of independent paths, the receiver uses majority vote. The measured causal distinguishability is

`TV = |P(B=1 | do(A=1)) - P(B=1 | do(A=0))|`.

For a uniform binary intervention, the corresponding mutual information is also computed.

## Main run

Parameters:

`p = 0.10`

`tau = 0.5`

reliability threshold:

`TV >= 0.50`

The maximum reliable distance in local hops was:

`K=1   -> N=3`

`K=3   -> N=4`

`K=5   -> N=5`

`K=11  -> N=7`

`K=25  -> N=9`

`K=101 -> N=12`

Corresponding times are:

`1.5, 2.0, 2.5, 3.5, 4.5, 6.0`.

Thus path diversity increases the distance over which a fixed causal distinguishability threshold can be maintained.

## Fixed-distance test

At `N=10` hops:

`K=1   -> TV = 0.1074`

`K=3   -> TV = 0.1604`

`K=5   -> TV = 0.1998`

`K=11  -> TV = 0.2852`

`K=25  -> TV = 0.4135`

`K=101 -> TV = 0.7220`

The local front still arrives after

`T_front = N tau = 5.0`.

Path multiplicity changes the reliability of the already-arrived signal; it does not change the local propagation time.

## Result

**POSITIVE STRUCTURAL SEPARATION:**

`PATH DIVERSITY`

can increase

`RELIABILITY / EFFECTIVE RELIABLE REACH`

without increasing

`CAUSAL FRONT SPEED`.

The model therefore separates three quantities:

`v_front`

maximum speed at which a controllable influence can first arrive,

`TV`

strength/distinguishability of the intervention effect,

`R_reliable`

maximum distance at which a chosen reliability threshold is maintained.

For this model:

`v_front = 1/tau`

while `R_reliable` increases with path diversity.

## Interpretation for Ω

This strengthens the previous REL-32/REL-33 separation:

`MEMORY`
→ changes admissible structure / path space

`PATH DIVERSITY`
→ changes redundancy and possible realizations

`NOISE`
→ degrades individual transitions

`REDUNDANCY`
→ can recover reliable causal influence

`LOCALITY + MINIMUM TRANSITION TIME`
→ fixes the causal-front speed

Therefore:

`WHAT CAN BE TRANSMITTED RELIABLY`

and

`HOW FAST CAUSAL INFLUENCE CAN FIRST ARRIVE`

are not the same physical quantity.

## Relation to known physics

This separation is compatible with Lieb–Robinson-type results, where local dynamics impose an effective light cone while influence outside the cone is suppressed rather than simply identified with ordinary correlation. Modern work also formulates explicit lower bounds on quantum message-delivery time. See the external references recorded during the research pass.

## Critical boundary

Not established:

1. That the toy-model front corresponds to the relativistic speed of light.
2. That `v_front = c` follows from Ω.
3. That memory physically generates additional paths in a real field theory.
4. That path diversity can increase signal capacity without energetic or dynamical cost.
5. That redundancy has any universal geometric interpretation.

## Current strongest chain

`DISTINCTION`
→ `RELATION`
→ `LOCALITY`
→ `BOUNDED INFLUENCE`
→ `CAUSAL CONE`
→ `PATH DIVERSITY`
→ `NOISE / RELIABILITY`

with the explicit separation

`CAUSAL FRONT SPEED ≠ RELIABLE INFORMATION REACH`.

## Next target

REL-36 should test whether a continuum limit can produce a stable finite characteristic speed from a local update rule, while varying lattice spacing and time step together. The key audit is whether the dimensionless speed survives refinement and whether an invariant scale can emerge rather than being inserted by hand.
