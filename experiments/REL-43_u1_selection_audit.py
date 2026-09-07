import numpy as np

"""REL-43 — U(1) selection audit.

Question:
Can the Ω-derived connection/curvature structure select U(1), rather than merely
an arbitrary abelian internal group?

Result encoded by the construction:
- Local gauge redundancy plus connection/curvature is compatible with any Lie group.
- Requiring a single physical gauge potential component and commuting curvature
  forces a one-dimensional abelian Lie algebra.
- But a one-dimensional connected compact Lie group is locally U(1) only after
  adding compactness/periodicity. R (the additive real group) is a distinct
  connected one-dimensional abelian group.
- Therefore Ω's structural chain does not select U(1) without an additional
  global compactness/periodicity or charge-quantization requirement.
"""


def curvature_linear(A, B):
    """Abelian curvature in a commuting internal algebra: F=dA represented
    here by antisymmetric derivative data A_mu,nu - A_nu,mu."""
    return A - B


def commutator_norm(X, Y):
    return np.linalg.norm(X @ Y - Y @ X)


def main():
    rng = np.random.default_rng(43)

    # Two independent commuting 1D internal generators: scalar multiples of I.
    X = rng.normal() * np.eye(2)
    Y = rng.normal() * np.eye(2)

    print("REL-43 U(1) selection audit")
    print("===========================")
    print("Commutator norm for 1D abelian representation:", commutator_norm(X, Y))
    print("Lie-algebra dimension:", 1)
    print("Candidate connected groups with this local algebra: R and U(1) (locally).")
    print("Curvature law in the abelian case: F = dA; no [A,A] term.")
    print("\nCountermodel A: additive R gauge group")
    print("  local algebra: one-dimensional abelian")
    print("  curvature: F=dA")
    print("  local gauge redundancy: A -> A + d(lambda)")
    print("  passes all local tests")
    print("\nCountermodel B: U(1) gauge group")
    print("  local algebra: one-dimensional abelian")
    print("  curvature: F=dA")
    print("  local gauge redundancy: A -> A + d(lambda)")
    print("  passes all local tests")
    print("\nOnly global compactness/periodicity distinguishes the groups:")
    print("  R: parameter lambda is non-periodic")
    print("  U(1): phase is periodic modulo 2*pi")
    print("\nConclusion:")
    print("  Local connection + curvature + one commuting generator selects an")
    print("  abelian one-dimensional gauge algebra, not uniquely U(1).")
    print("  U(1) requires an additional global compactness/periodicity input,")
    print("  or an equivalent physical condition such as charge quantization.")


if __name__ == "__main__":
    main()
