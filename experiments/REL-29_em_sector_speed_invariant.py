import math

# Coupled local sectors:
# dE/dt = A dB/dx
# dB/dt = C dE/dx
# => d2E/dt2 = A*C*d2E/dx2

tests = [(1.0, 1.0), (4.0, 0.25), (2.0, 8.0), (0.3, 3.0)]

for A, C in tests:
    print(A, C, math.sqrt(A * C))

# Independent field rescaling E'=lambda E, B'=mu B
A, C = 2.0, 8.0
lam, mu = 3.7, 0.42
Ap = A * mu / lam
Cp = C * lam / mu
print("rescaled_product_error", abs(Ap * Cp - A * C))
print("speed", math.sqrt(A * C), math.sqrt(Ap * Cp))

# CODATA 2022 displayed values
mu0 = 1.25663706127e-6
epsilon0 = 8.8541878188e-12
v = 1.0 / math.sqrt(mu0 * epsilon0)
print("vacuum_speed_from_displayed_constants", v)
print("difference_from_exact_SI_c", v - 299792458.0)
