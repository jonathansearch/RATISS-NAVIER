"""Traceurs QUANTIQES (notre truc, OpenAI n'a pas ça) : chaque particule porte
|ψ> ; paires de Bell dans le cylindre ; déphasage p ~ |ω| locale.
La cohérence C(t) devient une SONDE de la singularité. MIT."""
import numpy as np

Z2 = np.array([[1, 0], [0, -1]], complex)


class Tracers:
    def __init__(self, n, Kq=0.02, seed=3):  # calibre : plage dynamique C
        self.n = n
        self.Kq = Kq
        rng = np.random.default_rng(seed)
        self.psi = np.tile(np.array([1, 0], complex), (n, 1))
        self.pairs = {}
        self.rng = rng

    def bell(self, pairs):
        for a, b in pairs:
            v = np.array([1, 0, 0, 1], complex) / np.sqrt(2)
            self.pairs[a] = [b, v, False]
            self.pairs[b] = [a, v, False]

    def step(self, wmag, dt):
        for i in range(self.n):
            p = min(0.5, self.Kq * wmag[i] * dt)
            if p <= 0:
                continue
            if i in self.pairs:
                b, s, mixed = self.pairs[i]
                rho = s if mixed else np.outer(s, s.conj())
                w = 0 if i < b else 1
                z1 = Z2 if w == 0 else np.eye(2)
                z2 = np.eye(2) if w == 0 else Z2
                k0 = np.sqrt(1 - p) * np.eye(4)
                k1 = np.sqrt(p) * np.kron(z1, z2)
                rho = k0 @ rho @ k0.T.conj() + k1 @ rho @ k1.T.conj()
                self.pairs[i] = [b, rho, True]
                if b in self.pairs:
                    self.pairs[b] = [i, rho, True]
            else:
                a, c = self.psi[i]
                self.psi[i] = np.array([a, c * (1 - p)], complex)
                self.psi[i] /= max(np.linalg.norm(self.psi[i]), 1e-12)

    def concurrence(self, a):
        from .qsub import concurrence, concurrence_mixed
        _, s, mixed = self.pairs[a]
        return concurrence_mixed(s) if mixed else concurrence(s)
