import math

# REL-05: frozen Yee-like 1D vacuum dispersion relation.
# c=1, dx=1, dt=0.5. For mode k:
# sin^2(w dt/2) = (c dt/dx)^2 sin^2(k dx/2)

C = 1.0
DX = 1.0
DT = 0.5

modes = [0.01, 0.10, 0.50, 0.90]
print('REL-05 numerical dispersion')
for frac in modes:
    q = frac * math.pi
    k = q / DX
    omega_num = (2.0 / DT) * math.asin((C * DT / DX) * math.sin(q / 2.0))
    phase_ratio = omega_num / (C * k)
    err_pct = (phase_ratio - 1.0) * 100.0
    print(f'k/pi={frac:.2f}  omega_num={omega_num:.12g}  omega/ck={phase_ratio:.12g}  error_pct={err_pct:.6g}')

# Quantum compatibility layer: E=hbar*omega, p=hbar*k => E^2-p^2 c^2=0
hbar = 1.054571817e-34
k = 0.1 * math.pi
omega = C * k
E = hbar * omega
p = hbar * k
mass_shell = E * E - p * p * C * C
print(f'quantum_compatibility_mass_shell={mass_shell:.6e}')
