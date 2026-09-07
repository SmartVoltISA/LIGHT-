# REL-08 — Reflection, Refraction and Diffraction

## Physical target

Light changes propagation at boundaries because the field must satisfy Maxwell boundary conditions and the constitutive response of the medium. Reflection and transmission follow continuity constraints; refraction follows the change in phase relation/dispersion; diffraction follows wave evolution under apertures and obstacles.

For a simple isotropic interface, the normal-incidence Fresnel amplitude coefficient is

`r = (n1 - n2)/(n1 + n2)`

and the power reflectance is `R = |r|^2` for non-magnetic lossless media.

## Relation-first mapping

`bulk relation + boundary distinction → constrained field matching → redistribution of propagation/energy`.

The boundary is not an extra force. It changes the allowed relation between field states on the two sides.

## Status

`KNOWN / ARCHITECTURAL COMPATIBILITY`

A complete numerical REL-08 run should freeze material constitutive laws and test energy conservation across the interface, including reflected + transmitted flux.

## Important limitation

The Ω interpretation does not replace Fresnel/Maxwell equations. It identifies the boundary condition as a relation constraint and remains a hypothesis until the full numerical interface test is completed.
