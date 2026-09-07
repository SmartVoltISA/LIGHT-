import numpy as np

# REL-20: numerical check of the reparameterization homogeneity condition
# for power-law candidates f(z)=z^n, z=u.u>0.

z_values = np.array([0.2, 0.5, 1.0, 2.0, 5.0])
scales = np.array([0.3, 0.7, 1.4, 3.0])
exponents = [0.0, 0.25, 0.5, 1.0, 2.0]

errors = {}
for n in exponents:
    vals = []
    for z in z_values:
        for a in scales:
            vals.append(abs((a * a * z) ** n - a * (z ** n)))
    errors[n] = max(vals)

print("homogeneity errors for f(z)=z^n:")
for n, err in errors.items():
    print(f"n={n}: max_error={err:.16e}")

# Low-speed expansion check for sqrt(1-beta^2) = 1 - beta^2/2 + O(beta^4).
betas = [0.01, 0.05, 0.1, 0.2]
print("\nlow-speed expansion residuals:")
for beta in betas:
    exact = np.sqrt(1.0 - beta * beta)
    quadratic = 1.0 - 0.5 * beta * beta
    print(f"beta={beta}: residual={exact - quadratic:.16e}")

assert errors[0.5] < 1e-12
assert errors[0.25] > 1e-3
assert errors[1.0] > 1e-3
assert errors[2.0] > 1e-3
print("\nREL-20 PASS: n=1/2 is the tested homogeneous power-law solution.")
