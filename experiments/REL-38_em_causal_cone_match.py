import math

# REL-38: compare a generic causal-cone speed with the vacuum
# electromagnetic characteristic speed. No c is inserted into the
# electromagnetic calculation.

# Generic local causal rule
ell = 2.0
tau = 0.5
v_cone = ell / tau

# Maxwell vacuum characteristic speed from independently supplied
# electromagnetic coefficients.
mu0 = 1.25663706127e-6
eps0 = 8.8541878188e-12
v_em = 1.0 / math.sqrt(mu0 * eps0)

# SI exact defined value of c, used only as an external comparison.
c_si = 299_792_458.0

rel_err_em_vs_c = (v_em - c_si) / c_si
rel_err_cone_vs_c = (v_cone - c_si) / c_si

print(f'v_cone={v_cone:.12g}')
print(f'v_em={v_em:.12g}')
print(f'c_si={c_si:.12g}')
print(f'rel_err_em_vs_c={rel_err_em_vs_c:.12e}')
print(f'rel_err_cone_vs_c={rel_err_cone_vs_c:.12e}')

assert v_em > 0
assert abs(v_em - c_si) / c_si < 1e-10
assert v_cone != c_si

# Structural matching condition: if the local causal sector is identified
# with the EM vacuum characteristic sector, then its dimensional scale must
# satisfy ell/tau = 1/sqrt(mu0*eps0). This is a constraint, not a derivation.
required_tau = ell / v_em
print(f'required_tau_for_EM_match={required_tau:.12e}')
print('MATCH_CONDITION: ell/tau = 1/sqrt(mu0*eps0)')
print('STATUS: electromagnetic cone speed is fixed by EM coefficients; generic causal speed remains independent unless an additional identification/constraint is supplied.')
