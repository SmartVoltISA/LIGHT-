# REL-20 — Lorentz + Reparameterization Structure

Date: 2026-09-07
Status: COMPLETED — conditional structural derivation

## Question

Can locality + Lorentz invariance + reparameterization invariance constrain the form of a free-particle path functional without inserting the known relativistic action by hand?

## Setup

Take a local first-order worldline functional

`S[x] = ∫ L(u) dλ`, with `u^μ = dx^μ/dλ`.

Require:

1. Lorentz invariance: `L` depends only on Lorentz scalars built from `u^μ`.
2. Reparameterization invariance: under `λ → λ'` with positive scale factor `a`, the integrand must transform as `L(a u) = a L(u)` so that `L dλ` is invariant.
3. First-order locality: no higher derivatives and no nonlocal dependence on the full path.

For a free isotropic particle with no additional background structure, the only scalar formed from `u` is `z = u·u`.
Thus `L(u) = f(z)`.

Reparameterization homogeneity gives:

`f(a² z) = a f(z)`.

Let `y=a² z`. For timelike `z>0`, this functional equation implies

`f(z) = C sqrt(z)`.

Therefore

`L = C sqrt(u·u)`

up to the sign convention and normalization of the metric.

With `u·u = c² dτ²/dλ²`, this becomes

`S = C ∫ ds`.

The numerical test checked the homogeneity condition for power-law candidates `f(z)=z^n` over several positive `z` and scale factors. Only `n=1/2` satisfies the condition to machine precision.

## Low-velocity limit

For timelike motion,

`ds = c dt sqrt(1-v²/c²)`.

The expansion is

`sqrt(1-v²/c²) = 1 - 1/2(v²/c²) + O(v⁴/c⁴)`.

Therefore the relativistic path functional has the Newtonian quadratic kinetic structure in the low-speed limit, plus a velocity-independent constant term.

## Result

Within the explicitly stated assumptions, the square-root worldline functional is not an arbitrary extra choice: Lorentz scalar dependence plus first-order locality plus reparameterization homogeneity constrain the functional to `sqrt(u·u)` up to an overall coefficient.

This is stronger than REL-19 because the quadratic `v²` form now appears as a low-speed expansion of the constrained relativistic structure.

## Critical boundary

The derivation does NOT derive:

- Lorentz invariance itself;
- the Minkowski metric or spacetime dimension;
- the invariant speed `c`;
- the overall coefficient `C` / physical mass `m`;
- the stationary-action principle `δS=0`;
- why a free particle should admit this class of local worldline action.

Lorentz invariance and the metric are therefore still external physical structure in this experiment.

## Ω interpretation

The strongest supported conditional chain is:

`PATH`
→ `LOCALITY`
→ `LORENTZ SCALAR`
→ `REPARAMETERIZATION`
→ `HOMOGENEITY`
→ `sqrt(u·u)`
→ `proper interval`
→ `low-speed v²`

This does not yet derive spacetime. It shows how, once Lorentzian relational geometry is supplied, the allowed local path functional becomes highly constrained.

## Next target

Do not stop here. Test whether the Lorentzian metric/invariant interval itself can be reconstructed from weaker relational requirements, rather than supplied as an axiom. In parallel, map this against ORISIK/Ω results on distinction, relation, state, ordered transition, boundary and memory.
