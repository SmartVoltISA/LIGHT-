# REL-32 — Memory, path diversity, and causal signal bound

Date: 2026-09-07
Status: COMPLETED — toy-model separation test

## Question

Can memory and diversity of admissible paths change the space of possible futures without increasing the maximum speed of controllable causal transfer?

## Construction

Separate:

`M` — retained memory/configuration

`P(M)` — admissible paths after memory constraints

`Diversity(M) = |P(M)|`

`v_signal` — maximum controllable signal speed

Memory is allowed to modify the transition graph and therefore the number of admissible paths. The local propagation rule is kept fixed.

For every local update:

`reach <= R`

and

`time >= tau > 0`.

Therefore a signal crossing graph distance `D` satisfies

`N >= ceil(D/R)`

and

`T_signal >= ceil(D/R) tau`.

Hence

`v_signal <= D / (ceil(D/R) tau)`.

The bound depends on the local transition rule, not on the number of admissible alternative paths.

## Toy configurations

Configuration M1:

- graph distance A→B: `D=10`
- local reach: `R=2`
- transition time: `tau=0.5`
- admissible A→B paths: `1`

Configuration M2:

- same distance `D=10`
- same local reach `R=2`
- same transition time `tau=0.5`
- admissible A→B paths: `5`

For both:

`N_min = ceil(10/2) = 5`

`T_min = 5*0.5 = 2.5`

`v_max = 10/2.5 = 4`.

Thus

`Diversity(M1) != Diversity(M2)`

while

`v_signal(M1) = v_signal(M2) = 4`.

## Result

**POSITIVE STRUCTURAL SEPARATION:**

Memory can alter the accessible future path space without changing the causal speed bound, provided the local reach and transition-time constraints remain unchanged.

Therefore the following quantities are logically distinct:

`MEMORY`
→ changes constraints / admissible paths

`PATH DIVERSITY`
→ changes number of available realizations

`CAUSAL SPEED`
→ determined by local reach and minimum transition time in this model

## Interpretation

This gives a precise version of the hypothesis:

`memory/diversity may change WHAT can happen`

without changing

`the maximum speed at WHICH a controllable change can propagate`.

The experiment does not establish that physical memory or physical relation networks behave this way universally. It only proves the separation is internally consistent and not logically contradictory.

## Relation to known physics

Lieb–Robinson-type results independently separate local interaction structure from a finite propagation velocity/light-cone bound. In lattice quantum systems, the number and geometry of allowed interaction paths can affect dynamics while locality imposes propagation bounds. Recent work also gives lower bounds on quantum message delivery time. This motivates treating path diversity and signal speed as separate observables rather than identifying them.

## Critical boundary

Not established:

1. That physical memory can modify global relation structure instantaneously.
2. That correlations themselves can change faster than light in relativistic systems.
3. That a superluminal controllable channel exists.
4. That `v_signal=c` follows from memory or path diversity.

## Next target

Build an intervention-based information channel with two regions A and B. Initialize correlation independently of the later intervention. Measure the intervention-dependent information at B as a function of distance and time. Then vary memory/path diversity while keeping the local propagation rule fixed.

Desired separation:

`correlation structure` may be nonzero,

while

`intervention-dependent information outside the causal cone` remains zero or exponentially suppressed.
