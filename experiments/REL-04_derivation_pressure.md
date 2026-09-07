# REL-04 — Derivation Pressure: Connection Without Importing U(1)

## Question

REL-03 demonstrated that a discrete U(1) connection/curvature construction is compatible with the relation-first architecture. REL-04 asks the harder question:

> Can the need for a connection-like object be motivated from local-state comparison and representation invariance before choosing the electromagnetic group U(1)?

## Frozen starting assumptions

Only:

1. a set of local states `s(x)`;
2. local changes of representation `s(x) -> T_x s(x)`;
3. comparison between neighboring points;
4. requirement that physical predictions not depend on the arbitrary local representation choice;
5. locality of the comparison rule.

No U(1), A_mu, F_muν, Maxwell equation, or electromagnetic coupling is assumed in the architectural step.

## Structural pressure

A direct difference `s(x+dx)-s(x)` compares representatives living in potentially different local frames. If the representative transformation varies with position, a raw derivative generally does not transform in the same way as the state.

To preserve local covariance, the comparison must contain an additional compensating local relation. In differential-geometric language this is a connection.

For a general representation transformation `T(x)`, the covariant comparison has the schematic form

`D_mu = ∂_mu + Γ_mu`

with a transformation law for `Γ_mu` chosen so that `D_mu s` transforms covariantly.

The curvature is then the non-commutativity/holonomy of local comparisons:

`[D_mu, D_nu] ~ F_muν`.

This establishes a structural pressure toward connection → curvature, but it does not select the electromagnetic U(1) group.

## What REL-04 can and cannot establish

### Can establish

- local representation freedom creates a need for a compensating comparison rule;
- the compensating object has connection-like transformation behavior;
- closed-loop comparison naturally produces an invariant curvature/holonomy quantity;
- the architecture therefore has a route from local distinction to connection and curvature.

### Cannot establish yet

- that the group must be U(1);
- that the connection is electromagnetic;
- Maxwell dynamics;
- photon quantization;
- the numerical value of α.

## Falsification pressure

The Ω claim is weakened if a simpler local, representation-independent comparison exists that avoids any connection-like structure while retaining nontrivial spatially varying local transformations.

The claim is also weakened if the proposed derivation secretly assumes the group structure, linearity, or gauge field in disguised notation.

## Result

`STRUCTURAL SUPPORT / NOT U(1) DERIVATION`

REL-04 therefore advances the architecture by identifying a genuine structural necessity candidate, while preserving the distinction between deriving a connection and deriving electromagnetism.

## Next tests

- Determine which minimal assumptions select an Abelian group.
- Compare U(1) against non-Abelian alternatives under the same frozen criteria.
- Test whether the Maxwell kinetic invariant is selected by locality, symmetry, dimensionality, stability, and energy positivity rather than inserted manually.
