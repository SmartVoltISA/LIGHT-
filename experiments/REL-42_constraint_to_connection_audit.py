import numpy as np


def curl_matrix(khat):
    k = np.asarray(khat, dtype=float)
    k = k / np.linalg.norm(k)
    x, y, z = k
    return np.array([[0.0, -z, y], [z, 0.0, -x], [-y, x, 0.0]])


def audit(alpha=2.0, beta=0.5):
    C = curl_matrix([0.0, 0.0, 1.0])
    Z = np.zeros((3, 3))
    M = np.block([[Z, alpha * C], [-beta * C, Z]])

    # Divergence of curl is identically zero. In Fourier representation,
    # divergence is k^T and curl symbol is C(k), hence k^T C(k)=0.
    k = np.array([0.0, 0.0, 1.0])
    div_curl_defect = np.max(np.abs(k @ C))

    # Gauge redundancy of a reconstructed potential: curl(grad chi)=0.
    # Use chi=sin(z), so grad chi=(0,0,cos z); for k || z this is
    # longitudinal and annihilated by the curl symbol.
    grad_chi = np.array([0.0, 0.0, 1.0])
    gauge_reconstruction_defect = np.max(np.abs(C @ grad_chi))

    eig = np.linalg.eigvals(M)
    reality_defect = np.max(np.abs(eig.imag))

    print("REL-42 constraint-to-connection audit")
    print("=====================================")
    print("div(curl) Fourier defect:", div_curl_defect)
    print("curl(grad chi) defect:", gauge_reconstruction_defect)
    print("principal-symbol spectral reality defect:", reality_defect)
    print("eigenvalues:", sorted(eig, key=lambda q: (q.real, q.imag)))
    print()
    print("Conclusion:")
    print("  transverse constraint is preserved by curl dynamics")
    print("  potential reconstruction has gradient redundancy")
    print("  this supports a curvature-like invariant")
    print("  but no internal gauge group is selected")


if __name__ == "__main__":
    audit()
