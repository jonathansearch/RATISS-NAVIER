"""Setup 'OpenAI-like' : repos + force LISSE compacte -> vortex contractant.
Cylindre (axe z) : inflow radial + swirl azimutal + pulses anneau short-lived
(moyenne nulle, enveloppe gaussienne). Le spin-up vient de r.vθ conservé. MIT."""
import numpy as np


class Forcing:
    def __init__(self, L=4.0, R=0.8, A_in=6.0, A_sw=4.0, A_pulse=10.0,
                 m_mode=4, omega=6.0, active=True):
        self.c, self.R = L / 2, R
        self.A_in, self.A_sw, self.A_pulse = A_in, A_sw, A_pulse
        self.m, self.om, self.active = m_mode, omega, active

    def __call__(self, X, t):
        if not self.active:
            return np.zeros_like(X)
        d = X[:, :2] - self.c
        r = np.linalg.norm(d, axis=1)
        th = np.arctan2(d[:, 1], d[:, 0])
        F = np.zeros_like(X)
        core = np.exp(-(r / self.R) ** 2)
        er = np.column_stack([np.cos(th), np.sin(th), np.zeros_like(th)])
        et = np.column_stack([-np.sin(th), np.cos(th), np.zeros_like(th)])
        ramp = min(1.0, t / 0.3)
        F += (-self.A_in * core * r / self.R)[:, None] * er * ramp
        F += (self.A_sw * core)[:, None] * et * ramp
        ring = np.exp(-((r - 1.5 * self.R) / (0.4 * self.R)) ** 2)
        env = np.exp(-((t - 0.6) / 0.25) ** 2)  # short-lived
        puls = self.A_pulse * ring * env * np.cos(self.m * th - self.om * t)
        F += (puls * 0.5)[:, None] * er + (puls * 0.5)[:, None] * et
        return F
