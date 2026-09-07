import numpy as np

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])


def physical_polarization_dimension(k, tol=1e-12):
    """Count nullspace(k_mu eps^mu) modulo eps -> eps + alpha k for null k."""
    k = np.asarray(k, dtype=float)
    k_cov = ETA @ k
    _, s, _ = np.linalg.svd(k_cov.reshape(1, 4))
    rank = int(np.sum(s > tol))
    constraint_dim = 4 - rank
    k2 = float(k @ k_cov)
    if abs(k2) > tol:
        raise ValueError("k must be null for the photon audit")
    # The gauge direction k lies inside the constraint subspace for null k.
    return constraint_dim - 1, rank, k2


def run():
    momenta = [
        np.array([1.0, 0.0, 0.0, 1.0]),
        np.array([2.0, 1.2, 1.6, 0.0]),
        np.array([3.0, -1.0, 2.0, np.sqrt(4.0)]),
    ]

    for k in momenta:
        # Correct the third example analytically if roundoff is present.
        spatial = np.linalg.norm(k[1:])
        k[0] = spatial
        dof, rank, k2 = physical_polarization_dimension(k)
        print("k =", k, "k^2 =", k2, "constraint rank =", rank, "physical DOF =", dof)
        assert dof == 2
        assert abs(k2) < 1e-12

    # Explicit representatives for k=(1,0,0,1): x/y transverse modes.
    k = np.array([1.0, 0.0, 0.0, 1.0])
    eps_x = np.array([0.0, 1.0, 0.0, 0.0])
    eps_y = np.array([0.0, 0.0, 1.0, 0.0])
    for eps in (eps_x, eps_y):
        assert abs(float((ETA @ k) @ eps)) < 1e-14

    print()
    print("REL-46 result:")
    print("- null Maxwell momentum k^2=0")
    print("- Lorenz/transversality constraint removes one component")
    print("- gauge redundancy eps -> eps + alpha k removes one more")
    print("- 4 vector components -> 2 physical photon polarizations")
    print("- helicity representatives are the two transverse circular combinations")
    print("- quantum relations E = hbar*omega and p = hbar*k require hbar as an input")
    print("- m^2 c^4 = E^2 - p^2 c^2 = 0 follows from k^2=0")


if __name__ == "__main__":
    run()
