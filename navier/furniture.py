"""navier/furniture.py — les 3 étreintes, conformes au brief MISSION 3D (01/10/2026). MIT.
Ne modifie ni vortex.py, ni sph.py, ni tests/.

E1 OBSTACLE : pompe actuelle + répulsion statique au centre  F_rep = k·max(0, 1 − r/R_obs)²·êr  (k=10, R_obs=0,6)
E2 COUDE    : pompe actuelle dont l'axe du swirl est incliné de θ(z) = π·z/L (rotation autour de x̂)
E3 COURANTS : F = +A·x̂ pour z < L/2, −A·x̂ pour z ≥ L/2 (A=4) — remplace la pompe
Coupure à t_cut (défaut 1,0) : 'sec' ou 'rampe' (Δt=0,3). L'obstacle E1 est un meuble : il reste après la coupure.
"""
import numpy as np
from .vortex import Forcing


class Etreinte:
    def __init__(self, mode='plate', L=4.0, t_cut=1.0, coupure='sec', rampe=0.3,
                 k_obs=10.0, R_obs=0.6, A_cour=4.0):
        self.f, self.mode, self.L = Forcing(L=L), mode, L
        self.t_cut, self.coupure, self.rampe = t_cut, coupure, rampe
        self.k, self.R, self.A = k_obs, R_obs, A_cour

    def gain(self, t):
        if self.t_cut < 0 or t < self.t_cut:
            return 1.0
        if self.coupure == 'rampe':
            return max(0.0, 1.0 - (t - self.t_cut) / self.rampe)
        return 0.0

    def __call__(self, X, t):
        g, z = self.gain(t), X[:, 2]
        if self.mode == 'E3':
            F = np.zeros_like(X)
            F[:, 0] = np.where(z < self.L / 2, self.A, -self.A) * g
            return F
        F = self.f(X, t) * g if g > 0 else np.zeros_like(X)
        if self.mode == 'E2' and g > 0:
            th = np.pi * z / self.L
            Fy = F[:, 1].copy()
            F[:, 1] = np.cos(th) * Fy
            F[:, 2] = np.sin(th) * Fy + np.cos(th) * F[:, 2]
        if self.mode == 'E1':
            d = X[:, :2] - self.L / 2
            r = np.linalg.norm(d, axis=1)
            mag = self.k * np.maximum(0.0, 1.0 - r / self.R) ** 2
            er = d / np.maximum(r, 1e-9)[:, None]
            F[:, :2] += mag[:, None] * er
        return F
