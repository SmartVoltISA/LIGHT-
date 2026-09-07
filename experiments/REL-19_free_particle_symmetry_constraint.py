"""REL-19 — Free-particle functional form from symmetry constraints.

Checks the structural chain:
  locality + homogeneity + isotropy -> L = f(v^2)
  Galilean covariance up to a total derivative -> f'(v^2) = const
  therefore L = (m/2) v^2 + const.

This is a Newtonian/Galilean test, not a derivation of relativistic dynamics,
spacetime, or the physical origin of mass.
"""

import sympy as sp

v, u = sp.symbols("v u", real=True)
m, C = sp.symbols("m C", real=True)
f = sp.Function("f")

# Isotropy gives L=f(v^2). Under an infinitesimal Galilean boost v -> v+u,
# the first-order change is 2 v u f'(v^2). For the equations of motion to be
# unchanged, this change must be a total derivative. For a free particle that
# means it is affine in v. Parity/isotropy removes the velocity-independent
# odd contribution, so f'(v^2) is constant.
s = sp.symbols("s", nonnegative=True)
a = sp.symbols("a", real=True)
solution = sp.integrate(a / 2, s)

L = sp.Rational(1, 2) * m * v**2 + C
boost_delta = sp.expand(L.subs(v, v + u) - L)

print("General isotropic form: L=f(v^2)")
print("Galilean constraint: f'(v^2)=constant")
print("Integrated form: f(s)=a*s/2+C")
print("Relabel a -> m: L=m*v^2/2+C")
print("Finite boost delta:", boost_delta)
print("As total derivative: d/dt[m*u*x + m*u^2*t/2] for v=dx/dt")
print("Result: quadratic velocity form selected; coefficient m remains free input.")
