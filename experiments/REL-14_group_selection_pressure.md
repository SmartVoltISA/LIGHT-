# REL-14 — Group-selection pressure without choosing U(1)

## Question

REL-13 established a representation-agnostic result: if local descriptions may change independently, a consistent comparison between neighboring states requires a compensating transport/connection rule.

REL-14 asks the next question:

> Does that requirement select the electromagnetic group U(1), or is it compatible with many different groups?

## Frozen test families

1. `R+` — positive real local rescaling (`GL(1,R)+`).
2. `U(1)/SO(2)` — one-angle phase/rotation representation. These are locally isomorphic and therefore are not treated as independent physical selections.
3. `SO(3)` — non-Abelian rotation transport.
4. `GL(2,R)` — general invertible 2×2 linear transport.

For local frames `T_i`, define transport

`U(i,j) = T_i T_j^{-1}`.

The covariant discrete comparison is

`D_i ψ = U(i,j) ψ_j − ψ_i`.

Under a local change `ψ_i → T_i ψ_i`, the link transforms as

`U(i,j) → T_i U(i,j) T_j^{-1}`.

This is the discrete covariance test; no electromagnetic U(1) dynamics are inserted.

## Numerical result

With `N=24` local frames and deterministic random states (`seed=14`):

| family | raw comparison error | connection covariance error | composition error | commutator norm |
|---|---:|---:|---:|---:|
| R+ | 5.15e-2 | 3.61e-16 | 1.11e-16 | 2.22e-16 |
| U(1)/SO(2) | 1.52e-1 | 3.68e-16 | 1.86e-16 | 2.52e-17 |
| SO(3) | 8.96e-2 | 3.70e-16 | 1.61e-16 | 1.57e-3 |
| GL(2,R) | 5.05e-2 | 3.66e-16 | 1.57e-16 | 5.88e-4 |

The raw comparison is representation-dependent, while the compensating transport restores covariance to machine precision in every tested family.

The first two families commute in this construction; SO(3) and GL(2,R) show non-trivial commutator structure.

## Result

**REL-14 does not select U(1).**

The strongest statement supported by the experiment is broader:

`local representation freedom → comparison problem → transport/connection`

The following remain free at this level:

- Abelian versus non-Abelian group structure;
- compact versus non-compact group structure;
- representation dimension;
- the physical matter representation;
- coupling strength;
- Maxwell kinetic dynamics;
- quantum commutation/quantization rules;
- spacetime dimension and metric assumptions.

Therefore the existence of a connection is structurally earlier than the choice of electromagnetic U(1).

## Important consequence for Ω

This is a useful **negative result**, not a failure.

If Ω is to explain why electromagnetism specifically has U(1), the next derivation cannot simply repeat local covariance. It must introduce additional constraints capable of excluding the other admissible structures.

Candidate constraints to test separately:

1. one complex phase degree of freedom;
2. Abelian composition;
3. massless vector excitation;
4. exactly two physical transverse photon polarizations;
5. coupling to a conserved electric charge;
6. locality and Lorentz invariance;
7. positive-definite/unitary quantum representation;
8. empirical value and running of the electromagnetic coupling `α`.

No claim is made here that this list derives U(1). It is the next falsifiable search space.

## Status

**Structural support / exclusion boundary.**

REL-14 strengthens the connection result while explicitly failing to derive U(1). That boundary should remain visible in the Ω record.
