# REL-66 — Closed path + memory + topology audit

## Question

Can global observable structure arise from local relations through closed-path
composition and retained history, rather than by inserting a global observable
by hand?

## Construction

Use phase-valued edge relations. Under a vertex rephasing,

`theta_uv -> theta_uv + lambda_u - lambda_v`.

For an open path, endpoint terms survive. For a closed path, the vertex terms
telescope and cancel.

Therefore the closed product

`H(C) = product exp(i theta_e)`

is invariant under the tested local rephasing.

## Controls

1. **Closed triangle:** loop product is invariant under random vertex
   rephasings.
2. **Open path:** the same cancellation fails because endpoint terms remain.
3. **Local flux change:** changing one edge changes the contractible loop
   observable.
4. **Noncontractible ring:** two configurations with different total holonomy
   are globally distinguishable even though a 1D ring contains no local
   plaquette curvature capable of determining that holonomy.
5. **Ring gauge control:** arbitrary vertex rephasings preserve the total ring
   holonomy.

## Result

Conditional positive chain:

`LOCAL RELATIONS`
`-> CLOSED PATH`
`-> COMPOSITION`
`-> ENDPOINT CANCELLATION`
`-> GAUGE-INVARIANT LOOP MEMORY`
`-> GLOBAL OBSERVABLE CANDIDATE`.

This is the first clean bridge in this branch from local relational data to a
global invariant without directly declaring the invariant as a primitive
observable.

## Countermodel / boundary

The ring demonstrates an equally important negative result:

`LOCAL CURVATURE DATA ↛ COMPLETE GLOBAL HOLONOMY`.

A noncontractible cycle can retain global information not reconstructible from
local plaquette curvature alone.

Therefore the stronger claim

`local relation + memory -> all global observables`

is false without further assumptions.

What remains external is the existence and classification of closed paths,
the topology/global connectivity of the state space, and the physical
admissibility of loop operations.

## Relation to the LIGHT chain

The result gives a structural bridge:

`relation -> connection-like edge data -> closed path -> holonomy`

and separately

`local curvature -> contractible-loop response`.

It does **not** derive electromagnetic U(1), Wilson loops, spacetime topology,
or quantum phase from Omega. Those identifications require additional physics.

## Status

**CONDITIONAL POSITIVE + TOPOLOGICAL BOUNDARY.**

Closed-path composition is sufficient to produce a robust global invariant in
the tested model. Topological sector structure is not derived from local
causality or memory alone.
