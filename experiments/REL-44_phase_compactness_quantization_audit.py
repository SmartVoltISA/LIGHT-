"""
REL-44 — phase compactness / quantization audit

Question:
Can local gauge covariance plus quantum single-valuedness select compact U(1)
from the non-compact additive group R?

Audit:
1. Local Lie-algebra data is identical for R and U(1): infinitesimal parameter
   lambda is real and A -> A + d lambda.
2. Introduce a charged state with transformation exp(i q lambda).
3. For U(1), lambda ~ lambda + 2*pi is the same group element. Single-valuedness
   therefore requires exp(i q*2*pi)=1, hence q is integer in minimal-charge units.
4. For R there is no periodic identification, so arbitrary real q is locally
   consistent; no quantization follows from local covariance alone.

Conclusion:
Quantum single-valuedness + a periodic internal phase can select the compact
circle group, but periodicity/compactness is itself a global input. Therefore
REL-44 does not derive U(1) from the previous local Omega chain; it identifies
exactly the additional global quantum condition needed to exclude R.
"""

import cmath
import math


def u1_single_valued(q, tol=1e-12):
    return abs(cmath.exp(2j * math.pi * q) - 1.0) < tol


def noncompact_consistent(q):
    # R has no lambda ~ lambda + 2*pi identification.
    return True


def main():
    print("REL-44 phase compactness / quantization audit")
    print("==============================================")

    charges = [0, 1, -1, 2, 0.5, math.sqrt(2)]
    for q in charges:
        print(f"q={q:.12g}: U(1) single-valued={u1_single_valued(q)}, R-consistent={noncompact_consistent(q)}")

    print("\nMinimal-charge test:")
    print("  q=1      -> periodic")
    print("  q=2      -> periodic")
    print("  q=1/2    -> not periodic for a 2*pi parameterization")
    print("  q=sqrt(2)-> not periodic")

    print("\nResult:")
    print("  - Local R and U(1) gauge covariance have the same Lie algebra.")
    print("  - Local curvature F=dA cannot distinguish them.")
    print("  - Global periodicity plus single-valued quantum phase gives integer charge labels.")
    print("  - Therefore compactness is the missing global quantum condition, not a consequence of local Omega structure alone.")


if __name__ == "__main__":
    main()
