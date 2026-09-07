import math

# REL-07: plane-wave energy, Poynting flux and momentum density.
# Vacuum: u = 1/2(eps0 E^2 + B^2/mu0), S = E x B / mu0, g=S/c^2.
# For B=E/c, S=u*c and g=u/c.

c = 299792458.0
eps0 = 8.8541878188e-12
mu0 = 1.25663706127e-6
E = 1.0
B = E / c

u = 0.5 * (eps0 * E * E + B * B / mu0)
S = E * B / mu0
g = S / (c * c)

print('REL-07 energy-momentum consistency')
print(f'u={u:.15e} J/m^3')
print(f'S={S:.15e} W/m^2')
print(f'S/(u*c)={S/(u*c):.15e}')
print(f'g={g:.15e} kg/(m^2 s)')
print(f'g/(u/c)={g/(u/c):.15e}')
print(f'c^2*mu0*eps0={c*c*mu0*eps0:.15e}')
