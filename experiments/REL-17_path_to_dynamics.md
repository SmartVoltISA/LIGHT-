# REL-17 — Path → Dynamics Separation

Date: 2026-09-07
Status: COMPLETED — negative boundary confirmed

## Question

Does a generic notion of VALUE determine a physical trajectory, or is a physical action/dynamical law additional structure?

## Test

Two trajectories share the same endpoints `x(0)=0`, `x(T)=1`:

`x₁(t)` — straight path

`x₂(t)=x₁(t)+0.2 sin(2πt/T)` — curved path

An endpoint-only value function

`V(P) = −|x(T)−1|`

assigns the same value to both trajectories.

A separate supplied mechanical action is evaluated:

`S = ∫ [1/2 m v² − 1/2 kx²] dt`

with `m=2`, `k=3` and `dt=0.1`.

## Result

Numerical run:

`V(x₁) = V(x₂) = 0`

`S(x₁) = −0.4262500000000002`

`S(x₂) = 0.09471041507902246`

A small interior perturbation of the straight path gives a nonzero finite-difference variation of the supplied action:

`dS/dε ≈ −0.1498015`

Therefore the endpoint value does not determine the physical trajectory, while the supplied action distinguishes paths and provides a variational structure.

## Interpretation

This sharpens REL-16.

`VALUE` can express preference, but a generic value function is underdetermined. To obtain physical dynamics, the value must contain additional structure equivalent to a local path functional, and the selection condition must be specified.

In ordinary mechanics this structure is supplied by the action and the stationary-action condition:

`δS = 0`

The experiment does **not** show that physical action is derived from abstract VALUE. It shows what additional information is missing if VALUE is to become a physical path-selection principle.

## Ω boundary

The current chain should therefore remain:

`WILL → MEMORY → VALUE → CHOICE → PATH → ACTION → CHANGE`

with the explicit possibility that a future theory may establish a relation between VALUE and physical ACTION, but without identifying them prematurely.

## Next target

Find the minimum additional constraints required to turn a generic path-value functional into a physical variational law while testing locality, symmetry, time-translation invariance and conservation.
