import numpy as np


def local_u1_covariance(psi, dpsi, A, dlam, lam, q):
    """D=∂+iqA, psi'=exp(-iq lam)psi, A'=A+∂lam."""
    D = dpsi + 1j*q*A*psi
    psi_p = np.exp(-1j*q*lam)*psi
    dpsi_p = np.exp(-1j*q*lam)*(dpsi - 1j*q*dlam*psi)
    A_p = A + dlam
    D_p = dpsi_p + 1j*q*A_p*psi_p
    return abs(D_p - np.exp(-1j*q*lam)*D)


def u1_current(psi, Dpsi, q):
    # 1D scalar analogue of the phase current; enough to audit phase covariance.
    return q * np.imag(np.conjugate(psi) * Dpsi)


def run():
    rng = np.random.default_rng(47)
    errs = []
    current_errs = []
    for _ in range(100):
        psi = rng.normal() + 1j*rng.normal()
        dpsi = rng.normal() + 1j*rng.normal()
        A = rng.normal()
        dlam = rng.normal()
        lam = rng.normal()
        q = rng.normal()
        D = dpsi + 1j*q*A*psi
        errs.append(local_u1_covariance(psi, dpsi, A, dlam, lam, q))
        psi_p = np.exp(-1j*q*lam)*psi
        dpsi_p = np.exp(-1j*q*lam)*(dpsi - 1j*q*dlam*psi)
        A_p = A + dlam
        D_p = dpsi_p + 1j*q*A_p*psi_p
        current_errs.append(abs(u1_current(psi_p, D_p, q)-u1_current(psi, D, q)))

    print("REL-47 charge/current emergence audit")
    print("local covariance max error:", max(errs))
    print("current invariance max error:", max(current_errs))
    print()
    print("Structural result:")
    print("- Local U(1) phase covariance requires a connection in D_mu.")
    print("- The coupling q multiplies the connection in D_mu.")
    print("- The phase Noether current is gauge invariant.")
    print("- The interaction term is therefore of current-connection form A_mu J^mu.")
    print("- q is not numerically derived by this local symmetry audit; it labels the representation/charge.")
    print("- A neutral representation q=0 decouples from A_mu at minimal coupling.")
    print("- Matter field content, spin, mass, and numerical charge spectrum are not derived.")

    assert max(errs) < 1e-13
    assert max(current_errs) < 1e-13


if __name__ == "__main__":
    run()
