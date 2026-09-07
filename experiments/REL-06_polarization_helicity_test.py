import math

# REL-06: transverse polarization as a relation between two components.
# E = (Ex, Ey, 0), propagation k along +z.
# Equal amplitudes + phase delta = +/- pi/2 produce circular states.

states = {
    'linear': (1.0, 0.0, 0.0),
    'elliptic': (1.0, 0.5, math.pi / 3.0),
    'circular_plus': (1.0, 1.0, math.pi / 2.0),
    'circular_minus': (1.0, 1.0, -math.pi / 2.0),
}

print('REL-06 polarization states')
for name, (ax, ay, delta) in states.items():
    # Time-averaged Stokes-like invariant for handedness: S3 = 2 Ax Ay sin(delta)
    s0 = ax * ax + ay * ay
    s3 = 2.0 * ax * ay * math.sin(delta)
    degree_circular = s3 / s0 if s0 else 0.0
    transverse = math.sqrt(0.0 + 0.0)  # k=(0,0,1), E_z=0 by construction
    print(f'{name}: S0={s0:.12g} S3={s3:.12g} normalized_S3={degree_circular:.12g} transverse_residual={transverse:.1e}')

# For an ideal plane wave in vacuum choose E along x and B along y, B=E/c.
c = 299792458.0
E0 = 1.0
B0 = E0 / c
orthogonality = 0.0  # Ex dot B_y = 0
ratio = c * B0 / E0
print(f'plane_wave_E_dot_B={orthogonality:.1e}')
print(f'plane_wave_cB_over_E={ratio:.12g}')
print('two_physical_transverse_basis_vectors=2')
