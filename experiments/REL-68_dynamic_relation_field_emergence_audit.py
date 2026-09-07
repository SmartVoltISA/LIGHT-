import numpy as np


def periodic_gradient(x, dx):
    return (np.roll(x, -1) - np.roll(x, 1)) / (2.0 * dx)


def rhs(A, B, alpha, beta, dx):
    return alpha * periodic_gradient(B, dx), beta * periodic_gradient(A, dx)


def run(alpha, beta, n=256, dx=1.0, dt=0.001, steps=2000):
    x = np.arange(n) * dx
    A = np.exp(-((x - 0.35*n*dx)/(0.06*n*dx))**2)
    B = np.exp(-((x - 0.55*n*dx)/(0.05*n*dx))**2)
    def energy(a, b):
        return 0.5 * np.sum(beta*a*a + alpha*b*b) * dx
    e0 = energy(A, B)
    for _ in range(steps):
        k1a, k1b = rhs(A, B, alpha, beta, dx)
        k2a, k2b = rhs(A + 0.5*dt*k1a, B + 0.5*dt*k1b, alpha, beta, dx)
        k3a, k3b = rhs(A + 0.5*dt*k2a, B + 0.5*dt*k2b, alpha, beta, dx)
        k4a, k4b = rhs(A + dt*k3a, B + dt*k3b, alpha, beta, dx)
        A += dt*(k1a + 2*k2a + 2*k3a + k4a)/6
        B += dt*(k1b + 2*k2b + 2*k3b + k4b)/6
    ef = energy(A, B)
    return e0, ef, abs(ef-e0)/e0


def characteristic_speed(alpha, beta):
    M = np.array([[0.0, alpha], [beta, 0.0]])
    vals = np.linalg.eigvals(M)
    return np.sort(vals), np.sqrt(alpha*beta)


def main():
    for alpha, beta in [(1.0, 1.0), (4.0, 0.25), (2.0, 8.0)]:
        vals, v = characteristic_speed(alpha, beta)
        assert np.max(np.abs(np.sort(vals) - np.array([-v, v]))) < 1e-14
        e0, ef, err = run(alpha, beta)
        print(f"alpha={alpha} beta={beta} speed={v:.12g} energy_rel_error={err:.3e}")
        assert err < 2e-5
    print("REL-68 PASS: local dynamic relation supports finite propagation and a conserved quadratic energy-like quantity.")
    print("Boundary: these properties also occur in non-electromagnetic hyperbolic systems.")


if __name__ == "__main__":
    main()
