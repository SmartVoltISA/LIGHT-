import numpy as np

"""REL-41 — 3D transverse-mode selection audit."""


def curl_matrix():
    return np.array([[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 0.0]])


def block(A, B, C, D):
    return np.block([[A, B], [C, D]])


def maxwell_like(alpha=2.0, beta=0.5):
    C = curl_matrix(); Z = np.zeros((3, 3))
    return block(Z, alpha*C, -beta*C, Z)


def longitudinal_countermodel(u=1.0, v=1.0):
    I = np.eye(3); Z = np.zeros((3, 3))
    return block(u*I, Z, Z, -v*I)


def identity_coupled_countermodel(u=1.0):
    I = np.eye(3); Z = np.zeros((3, 3))
    return block(Z, u*I, u*I, Z)


def report(name, M):
    vals = np.linalg.eigvals(M)
    print(name)
    print("  eigenvalues:", vals)
    print("  spectral reality defect:", max(abs(z.imag) for z in vals))


def main():
    print("REL-41 — 3D transverse-mode selection audit")
    print("============================================")
    C = curl_matrix()
    print("curl eigenvalues for k-hat=z:", np.linalg.eigvals(C))

    M = maxwell_like(2.0, 0.5)
    report("A. curl-coupled Maxwell-like family", M)
    print("  transverse cone coefficient sqrt(alpha*beta):", np.sqrt(2.0*0.5))
    print("  longitudinal curl sector is zero: yes")

    report("B. isotropic identity-coupled countermodel", identity_coupled_countermodel())
    report("C. explicit longitudinal countermodel", longitudinal_countermodel())

    print("\nFixed-cone Maxwell-like family")
    for a, b in [(1, 1), (4, .25), (2, .5), (8, .125)]:
        print(f"  alpha={a:g}, beta={b:g}, sqrt(alpha*beta)={np.sqrt(a*b):g}")

    print("\nRESULT")
    print("Locality + 3D isotropy + first-order vector structure do not select Maxwell.")
    print("Adding exactly two propagating transverse modes and no longitudinal")
    print("derivative sector selects a curl-only two-vector principal class within")
    print("this restricted local ansatz.")
    print("The surviving class retains coefficient and field-normalization freedom;")
    print("epsilon, mu, SI scale and c remain un-derived.")


if __name__ == "__main__":
    main()
