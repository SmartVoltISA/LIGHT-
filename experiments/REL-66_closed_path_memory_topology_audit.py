"""REL-66 — closed path + memory + topological equivalence audit.

Tests whether a global loop invariant can emerge from local edge relations once
closed paths and deformation equivalence are admitted.

Toy model: U(1)-like edge phases on a graph. Open-path phase is endpoint/gauge
dependent; closed-loop phase is invariant under vertex rephasing. Contractible
loop phase changes when local curvature/flux is changed. A noncontractible cycle
can retain a global holonomy even when every local plaquette flux is zero.

This is a structural audit, not a derivation of U(1), topology, or physical
boundary conditions from Omega.
"""

import cmath
import random


def edge_phase(theta):
    return cmath.exp(1j * theta)


def gauge_transform(theta_uv, lam_u, lam_v):
    return theta_uv + lam_u - lam_v


def path_product(edges):
    z = 1 + 0j
    for theta in edges:
        z *= edge_phase(theta)
    return z


def close(a, b, tol=1e-12):
    return abs(a - b) < tol


def main():
    rng = random.Random(6601)

    # Triangle loop: local edge relations compose to a closed-loop invariant.
    th01, th12, th20 = [rng.uniform(-3, 3) for _ in range(3)]
    loop = path_product([th01, th12, th20])

    l0, l1, l2 = [rng.uniform(-2, 2) for _ in range(3)]
    gt = [
        gauge_transform(th01, l0, l1),
        gauge_transform(th12, l1, l2),
        gauge_transform(th20, l2, l0),
    ]
    loop_g = path_product(gt)
    assert close(loop, loop_g)

    # Open path is not invariant under independent endpoint rephasing.
    open_before = path_product([th01, th12])
    open_after = path_product(gt[:2])
    assert not close(open_before, open_after)

    # Local curvature/flux changes the contractible loop observable.
    delta = 0.37
    loop_changed = path_product([th01 + delta, th12, th20])
    assert not close(loop, loop_changed)

    # Noncontractible ring countermodel: distribute total holonomy Phi evenly.
    # There are no plaquettes in the 1D ring, hence no local plaquette curvature
    # to reveal Phi, but the product around the full cycle retains it.
    n = 8
    phi0 = 0.0
    phi1 = 1.234
    ring0 = [phi0 / n] * n
    ring1 = [phi1 / n] * n
    H0 = path_product(ring0)
    H1 = path_product(ring1)
    assert not close(H0, H1)

    # Gauge transformation around the ring preserves total holonomy.
    lambdas = [rng.uniform(-1, 1) for _ in range(n)]
    ring1_g = [
        gauge_transform(ring1[i], lambdas[i], lambdas[(i + 1) % n])
        for i in range(n)
    ]
    assert close(H1, path_product(ring1_g))

    print("REL-66 closed path memory topology audit")
    print(f"closed-loop gauge residual: {abs(loop-loop_g):.3e}")
    print(f"open-path endpoint-change magnitude: {abs(open_before-open_after):.3e}")
    print(f"local-flux loop change magnitude: {abs(loop-loop_changed):.3e}")
    print(f"noncontractible holonomy separation: {abs(H0-H1):.3e}")
    print(f"ring holonomy gauge residual: {abs(H1-path_product(ring1_g)):.3e}")
    print("RESULT: closed-path composition can turn local relations into a gauge-invariant global memory/holonomy once loop structure is admitted.")
    print("COUNTERMODEL: zero local plaquette information does not determine noncontractible-cycle holonomy.")
    print("BOUNDARY: existence/classification of noncontractible loops and admissible topology remain additional structural inputs.")


if __name__ == "__main__":
    main()
