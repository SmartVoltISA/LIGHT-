# REL-24 — Relation → Path → Graph distance → Metric

Date: 2026-09-07
Status: COMPLETED — structural derivation with explicit boundary

## Question

Can a distance-like structure be obtained from relations and paths without inserting a continuous spatial metric at the start?

## Construction

Start with an undirected connected graph

`G = (V,E)`

where vertices are distinguished states/nodes and edges are relations.

Define the path length of a path `P=(v0,...,vn)` as the number of traversed relations:

`L(P)=n`.

Define relational distance as the shortest-path length:

`d(v,w)=min_P L(P)`.

For a connected unweighted graph this gives:

`d(v,v)=0`

`d(v,w)=d(w,v)`

`d(v,z) ≤ d(v,w)+d(w,z)`.

Thus relation + path + minimality produces a genuine metric on the node set at the graph level.

## Countermodels / boundary

This does NOT derive a unique physical spatial metric.

1. Different graphs can satisfy the same abstract relational requirements while producing different metrics.
2. Weighted edges require an additional positive weight/length assignment.
3. A continuous manifold, dimension, differentiability, metric tensor and signature are not obtained from graph distance alone.
4. Lorentzian spacetime is not selected by ordinary shortest-path distance, which is positive-definite rather than causal/indefinite.

## Result

**POSITIVE STRUCTURAL RESULT:**

`DISTINCTION → RELATION → PATH → MINIMAL PATH → DISTANCE`

is sufficient to construct a metric on a discrete relational structure when the relation graph is connected and the path cost is the positive edge-count.

**NEGATIVE DERIVATION RESULT:**

`DISTANCE → physical spatial metric` is not automatic, and `DISTANCE → Lorentzian metric` is false without additional structure.

## Ω interpretation

This closes one previously vague gap: the word `DISTANCE` need not be primitive at the discrete relational level. A discrete distance can arise from relation, path and minimality.

The remaining missing structure is the upgrade from relational distance to physical geometry:

`RELATION → PATH → MINIMAL PATH → DISCRETE DISTANCE → CONTINUOUS GEOMETRY`

and separately:

`CAUSAL / INVARIANT STRUCTURE → LORENTZIAN GEOMETRY`.

No claim of physical derivation is made.

## Candidate chain

`DISTINCTION → RELATION → STATE → ORDERED TRANSITION → PATH → MINIMAL PATH → DISTANCE → GEOMETRY`

with causal branch:

`BOUNDED + FRAME-INVARIANT INFLUENCE → CAUSAL CONE → CONFORMAL STRUCTURE → LORENTZIAN GEOMETRY`.
