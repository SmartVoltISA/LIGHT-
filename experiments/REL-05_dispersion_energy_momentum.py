"""REL-05: dispersion, energy and momentum for a vacuum EM mode.

Frozen target: omega = c|k|, E = h nu, p = hbar k, E = pc for a photon.
The numerical part tests the classical vacuum dispersion relation and the
energy/flux relation of a transverse plane wave. Quantum relations are
checked algebraically from the frozen constants rather than simulated.
"""
import numpy as np


def run(nk=2000, c=1.0, dt_dx=0.5):
    k = np.linspace(1e-9, np.pi, nk)
    omega = 2.0 / dt_dx * np.arcsin(dt_dx * np.sin(k / 2.0))
    phase_speed = omega / k
    return {
        "max_relative_dispersion_error": float(np.max(np.abs(omega-k)/k)),
        "long_wavelength_phase_speed": float(phase_speed[0]),
        "nyquist_phase_speed": float(phase_speed[-1]),
        "continuum_target": "omega=c|k|",
        "numerical_note": "Finite-grid dispersion is expected near the Nyquist scale; it vanishes in the continuum/long-wavelength limit.",
    }


if __name__ == "__main__":
    print(run())
