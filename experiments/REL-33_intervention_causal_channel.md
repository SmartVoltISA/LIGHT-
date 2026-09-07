# REL-33 — Intervention-based causal channel

Date: 2026-09-07
Status: COMPLETED — toy-model causal separation test

## Question

Can pre-existing correlation be nonzero while intervention-dependent information remains absent outside a causal cone? And can path diversity change the number of realizations without changing causal arrival time?

## Why intervention is required

Ordinary mutual information measures statistical association and can remain nonzero because of a common prior cause or initial preparation. It therefore does not by itself establish signaling. An intervention asks a different question: does changing A under controlled conditions change the distribution observed at B? This distinction is standard in interventionist causal analysis and in information-theoretic treatments of causal influence.

## Construction

Use a binary latent variable `Z ~ Bernoulli(1/2)`.

Initial preparation:

`A = Z`

`B = Z`

Therefore the initial correlation is maximal:

`I(Z;B) = 1 bit`.

At `t=0`, the sender chooses an intervention `U in {0,1}` and sets A to U. U is independent of Z.

Two regimes are then compared:

1. **Outside causal cone:** B has not yet received the intervention and remains determined by Z.
2. **Inside causal cone:** a local propagation chain has delivered U to B, so B=U.

The local rule is fixed by:

`reach <= R`

`time >= tau > 0`.

For graph distance D:

`N_min = ceil(D/R)`

`T_arrival >= N_min * tau`

and therefore

`v_signal <= D / T_arrival`.

## Operational causal observable

For the two interventions compare

`P(B | do(A=0))`

with

`P(B | do(A=1))`.

Use total variation distance:

`TV = 1/2 * sum_b |P(b|do(A=0)) - P(b|do(A=1))|`.

If `TV=0`, the receiver distribution is identical and the intervention has no detectable signaling effect at B.

Also compute mutual information between the intervention variable U and B under the intervention ensemble. This is a causal-information quantity, not the original pre-intervention correlation.

## Toy parameters

`D=10`

`R=2`

`tau=0.5`

Therefore:

`N_min = ceil(10/2) = 5`

`T_arrival = 5*0.5 = 2.5`

`v_bound = 10/2.5 = 4`.

Two memory/path configurations are compared:

`M1`: 1 admissible A→B path.

`M2`: 5 admissible A→B paths.

All paths use the same local reach and transition time.

## Expected / verified model result

Before step 5 (`t < 2.5`):

`P(B|do(A=0)) = (1/2, 1/2)`

`P(B|do(A=1)) = (1/2, 1/2)`

therefore

`TV = 0`

and

`I(U;B) = 0 bit`.

The original preparation still contains:

`I(Z;B) = 1 bit`.

This is the critical separation:

`correlation != controllable influence`.

At and after step 5 (`t >= 2.5`), the local channel delivers U to B:

`P(B|do(A=0)) = (1,0)`

`P(B|do(A=1)) = (0,1)`

therefore

`TV = 1`

and

`I(U;B) = 1 bit`.

For both M1 and M2 the first causal effect occurs at step 5, time 2.5, because path count does not alter the local propagation rule.

## Result

**POSITIVE CAUSAL SEPARATION.**

The model demonstrates all three quantities can be kept distinct:

`INITIAL CORRELATION`
→ exists before intervention

`INTERVENTION-DEPENDENT INFORMATION`
→ zero before causal arrival, nonzero after arrival

`PATH DIVERSITY`
→ changes the number of available routes without changing the arrival bound when local propagation rules are fixed.

This strengthens REL-31 and REL-32. The experiment is no longer only a structural graph argument; it introduces an explicit operational intervention and receiver statistic.

## Relation to the LIGHT causal program

The relevant ontology is:

`RELATION GRAPH G(t)`
→ structural connectivity

`CORRELATION C(A,B)`
→ statistical dependence

`INTERVENTION I(A→B,t)`
→ controllable causal influence

`SIGNAL SPEED`
→ rate at which intervention-dependent influence can reach B

These must not be collapsed into one quantity.

## Critical boundary

This toy model does **not** derive:

1. physical causality from relation alone;
2. the physical value `c`;
3. Lorentz invariance;
4. quantum no-signaling from first principles;
5. a universal physical memory law;
6. exponential Lieb–Robinson tails or relativistic microcausality.

It only demonstrates that the proposed distinctions are mathematically consistent and experimentally expressible with intervention-dependent observables.

## Next target

REL-34 should replace the deterministic hard causal cone with a noisy/local stochastic channel and test whether:

`TV(outside cone) -> 0`

while inside the cone it rises continuously.

Then vary path diversity and memory while holding the local channel parameters fixed. The key question becomes whether memory/path diversity changes **amplitude, reliability, or redundancy** of causal transfer without changing the front speed.
