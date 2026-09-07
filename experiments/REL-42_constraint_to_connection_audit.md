# REL-42 — Constraint preservation, connection, and curvature audit

**Date:** 2026-09-07  
**Branch:** `rel-41-actual`  
**Status:** structural result / gauge gap isolated

## Question

After REL-41, the surviving local 3D class is curl-coupled and transverse. Does preservation of the transverse constraint force a potential/connection structure, and does that structure force U(1)?

## Step 1 — Constraint preservation

For a curl-coupled pair

`∂t A = α curl B`

`∂t B = -β curl A`,

apply divergence:

`∂t(div A) = α div(curl B) = 0`

`∂t(div B) = -β div(curl A) = 0`.

Therefore `div A` and `div B` are conserved under the principal dynamics. If the initial physical sector is transverse, it remains transverse.

This is a genuine structural consequence of the curl operator. It does not yet say that A or B is a gauge connection.

## Step 2 — Potential reconstruction

A divergence-free vector field on a sufficiently regular simply connected spatial domain can locally be represented as a curl:

`B = curl A_pot`.

However this reconstruction is not unique because

`curl(A_pot + grad χ) = curl A_pot`.

Thus the mathematical pattern

`potential → derivative → gauge-equivalent representatives → invariant curl`

appears naturally once the transverse/curl structure is represented by a potential.

This is the same structural relation used in electromagnetism: the field strength is represented locally as `F=dA`, while `A` is non-unique under addition of an exact form. citeturn0search10turn0search6

## Step 3 — What is actually forced

The audit establishes a hierarchy:

`transverse constraint`
→ `curl structure`
→ `local potential representation (under regularity/topology assumptions)`
→ `potential redundancy`
→ `curvature-like invariant`.

This is stronger than merely observing that Maxwell has gauge symmetry.

But the following implication is **not** established:

`potential redundancy → U(1)`.

A connection can take values in many internal groups. Abelian U(1) requires an additional internal one-dimensional compact phase structure (or an equivalent physical principle). Local covariance by itself does not select that group.

## Step 4 — Maxwell/QED cross-check

In standard gauge theory, local U(1) invariance introduces a gauge field/connection and the invariant field strength has the form

`F_{μν}=∂_μ A_ν-∂_ν A_μ`.

The resulting gauge-field equations are Maxwell equations. citeturn0search0turn0search5

This confirms the direction of the structural chain, but it is an external physics construction, not an Ω derivation.

## Result

**POSITIVE STRUCTURAL RESULT, WITH A HARD BOUNDARY.**

REL-41's transverse curl selection naturally creates the mathematical conditions under which a potential/curvature description and representation redundancy appear.

But Ω has **not** derived:

- a specific internal gauge group;
- U(1) specifically;
- charge quantization;
- coupling constant;
- electromagnetic matter coupling;
- the quantum phase interpretation;
- topology/global bundle structure.

The new pressure point is therefore sharply isolated:

`STRUCTURAL CURL / CURVATURE`
→ **`INTERNAL GROUP SELECTION`**
→ `U(1)`?

## Important distinction

Do not state that gauge redundancy is the same thing as electromagnetic gauge invariance. The first can arise as redundancy of a potential representation; U(1) gauge theory is a stronger physical/mathematical structure.

## Candidate REL-43

Test whether the combination of:

1. one real local phase degree of freedom;
2. composition of local transformations;
3. continuity of the transformation parameter;
4. compact periodic identification;
5. locality of the associated connection;
6. a positive local quadratic field action;

selects the Abelian compact group U(1), or whether multiple groups/countermodels survive.

The test must not assume the name `U(1)` in the input model.