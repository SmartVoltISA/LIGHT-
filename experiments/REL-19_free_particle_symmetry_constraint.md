# REL-19 — Free-particle functional form from symmetry constraints

Date: 2026-09-07
Status: COMPLETED — form constrained, coefficient not derived

## Question

Can the form of a free-particle physical path functional be constrained without inserting `L = 1/2 m v^2` at the start?

## Assumptions under test

For a free non-relativistic particle:

1. locality in the path parameter;
2. spatial homogeneity;
3. time homogeneity;
4. spatial isotropy;
5. Galilean covariance of the equations of motion;
6. Lagrangians differing by a total time derivative are physically equivalent.

These assumptions are explicitly Newtonian/Galilean. They are not claimed to be Ω-derived.

## Step 1 — locality and homogeneity

A local first-order functional has

`S = ∫ L(x, v, t) dt`.

Spatial and temporal homogeneity remove explicit `x` and `t` dependence for a free particle:

`L = L(v)`.

## Step 2 — isotropy

Rotational invariance permits dependence only on the scalar `v²`:

`L = f(v²)`.

This is the first strong restriction. The function `f` is still arbitrary.

## Step 3 — Galilean covariance

Under a boost with constant velocity `u`:

`v -> v + u`.

Equivalent Lagrangians may differ by a total derivative. For an infinitesimal boost, the change is

`δL = 2 v·u f'(v²)`.

For this to be a total derivative of a function of `x,t`, the velocity dependence must be affine in `v`. Since isotropy makes `f` a function of `v²`, this requires

`f'(v²) = constant`.

Therefore

`f(v²) = a v² + C`.

Writing `a = m/2` gives

`L = 1/2 m v² + C`.

The finite boost check gives

`L(v+u)-L(v) = m u·v + 1/2 m u²`

which is

`d/dt [m u·x + 1/2 m u² t]`.

Hence the transformed Lagrangian differs only by a boundary term, so the equations of motion are unchanged.

## Result

The combination

`locality + homogeneity + isotropy + Galilean covariance`

is sufficient to constrain the free-particle Lagrangian to the quadratic velocity form

`L = 1/2 m v² + constant`.

This is independently consistent with standard mechanics derivations. citeturn1search0turn1search21

## Ω boundary

This result is important but must be stated precisely.

We did **not** derive mass.

We derived only the functional form up to a free coefficient:

`L ∝ v²`.

The coefficient can be named `m`, but its numerical value and physical origin remain external inputs. The additive constant is dynamically irrelevant.

Thus REL-19 advances the chain:

`PATH`
→ `LOCAL FUNCTIONAL`
→ `HOMOGENEITY + ISOTROPY`
→ `Galilean covariance`
→ `L ∝ v²`
→ `INERTIAL DYNAMICS`

but leaves

`m = ?`

open.

## Important limitation

This is a derivation inside Newtonian/Galilean mechanics, not a derivation of Newtonian spacetime itself. In particular, it does not establish that Ω must choose Galilean symmetry, nor does it establish the relativistic form of the free-particle action.

## Next target

Remove the specifically Galilean assumption and repeat the constraint search under relativistic spacetime symmetry. Test whether locality + Lorentz invariance + reparameterization structure constrain the free-particle functional toward

`S ∝ ∫ ds`

without inserting the relativistic action by hand.
