"""furniture.py — le mobilier 3D de la ville (étreintes + poussière). Ne touche pas aux modules scellés. MIT.

E1 obstacle  : sphère de frein (Brinkman) décentrée, finie en z -> la poussée bute différemment selon l'étage.
E2 coude     : la poussée horizontale tourne avec l'altitude (angle 2*pi*z/L).
E3 tête-bêche: le swirl change de signe avec l'altitude (sin 2*pi*z/L) -> deux courants opposés.
Poussière    : bruit de vitesse non structuré eps*N(0,1) après settle() (eps=0.01 ~ 0.9 % de v_rms).
Coupure      : 'sec' (instantanée) ou 'rampe' (descente linéaire sur 0.3) — témoin T3.
"""
import numpy as np
from navier.vortex import Forcing


class Pompe3D:
    def __init__(self, mode='base', L=4.0, t_cut=1.0, coupure='sec', rampe=0.3, k_obs=20.0):
        self.f = Forcing(L=L)
        self.mode, self.L, self.t_cut, self.coupure, self.rampe, self.k = mode, L, t_cut, coupure, rampe, k_obs
        self.V = None   # injecté par la boucle pour le frein E1

    def gain(self, t):
        if self.t_cut < 0 or t < self.t_cut:
            return 1.0
        if self.coupure == 'rampe':
            return max(0.0, 1.0 - (t - self.t_cut) / self.rampe)
        return 0.0

    def __call__(self, X, t):
        g = self.gain(t)
        F = self.f(X, t) * g if g > 0 else np.zeros_like(X)
        z = X[:, 2]
        if self.mode == 'E2' and g > 0:
            a = 2 * np.pi * z / self.L
            c, s = np.cos(a), np.sin(a)
            Fx, Fy = F[:, 0].copy(), F[:, 1].copy()
            F[:, 0], F[:, 1] = c * Fx - s * Fy, s * Fx + c * Fy
        if self.mode == 'E3' and g > 0:
            F[:, :2] *= np.sin(2 * np.pi * z / self.L)[:, None]
        if self.mode == 'E1' and self.V is not None:   # l'obstacle reste après la coupure (c'est un meuble)
            c0 = np.array([2.0 + 1.0, 2.0, 2.0])
            d = X - c0
            d -= self.L * np.round(d / self.L)
            inside = np.exp(-(np.linalg.norm(d, axis=1) / 0.4) ** 2)
            F -= (self.k * inside)[:, None] * self.V
        return F


def poussiere(V, eps, seed):
    if eps <= 0:
        return V
    return V + eps * np.random.default_rng(seed).normal(size=V.shape)
