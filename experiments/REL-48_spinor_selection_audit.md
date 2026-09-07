# REL-48 — Spinor selection audit

## Question
Can locality + Lorentz/Spin(1,3) covariance + first-order linear dynamics + local U(1) charge covariance select the Dirac spinor sector, or is the spinor representation an additional input?

## Audit
1. A charged matter field can transform in many Lorentz representations while carrying the same U(1) charge: scalar, Weyl, Dirac, vector, and higher-spin representations are structurally distinct.
2. Local U(1) covariance only requires a replacement of partial derivatives by a covariant derivative, D_mu = partial_mu + i q A_mu (sign convention arbitrary). It does not select the Lorentz representation.
3. Requiring a first-order relativistic linear equation strongly narrows the possibilities, but the Clifford algebra/gamma matrices are still an additional representation-theoretic structure. A Dirac field is obtained by choosing the spin-1/2 representation (1/2,0) direct sum (0,1/2).
4. A scalar charged field with Klein-Gordon dynamics and a charged Weyl field with a first-order Weyl equation are countermodels to the claim that U(1)+locality uniquely implies a Dirac field.
5. Therefore the strongest honest result is conditional: if one additionally requires a local Lorentz-covariant first-order equation for a nontrivial spin-1/2 field, the Dirac/Clifford structure follows; spin-1/2 itself is not derived by the present Ω package.

## Mass audit
The Dirac mass term m psi_bar psi is Lorentz invariant and U(1) invariant. Therefore gauge symmetry does not determine m. For a chiral Weyl field, a mass term requires additional representation/conjugation structure; this is a separate constraint, not a consequence of U(1) alone.

## Boundary
Not derived: Spin(1,3), spinor representation, Clifford algebra, fermionic statistics/Grassmann nature, numerical mass, numerical charge, particle spectrum.

## Conclusion
NEGATIVE for unique emergence of the Dirac sector from Ω + local U(1) alone.
POSITIVE only conditionally after adding spin-1/2 + first-order relativistic dynamics + Clifford structure.
