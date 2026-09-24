"""SPH 3D faiblement compressible, boîte périodique + cell-list (Müller 2003).
Positions/vitesses = nos qubits-particules. MIT."""
import numpy as np

try:
    from . import kernels as K
except ImportError:
    import kernels as K


class Flow:
    def __init__(self, n=1500, L=4.0, h=None, nu=0.01, rho0=1.0, k_press=50.0,
                 seed=7):
        h = 1.4 * L / (n ** (1 / 3)) if h is None else h
        self.n, self.L, self.h, self.nu = n, L, h, nu
        self.rho0, self.kp = rho0, k_press
        rng = np.random.default_rng(seed)
        m = int(np.ceil(n ** (1 / 3)))
        g = np.linspace(0.5 * L / m, L - 0.5 * L / m, m)
        gx, gy, gz = np.meshgrid(g, g, g)
        Xg = np.column_stack([gx.ravel(), gy.ravel(), gz.ravel()])[:n]
        self.X = (Xg + rng.normal(0, 0.002 * L / m, (n, 3))) % L
        self.V = np.zeros((n, 3))
        self.m = np.full(n, rho0 * L ** 3 / n)
        self.rho = np.full(n, rho0)
        self.p = np.zeros(n)
        self.om = np.zeros((n, 3))
        self.nc = max(1, int(L / h))
        self.t = 0.0

    def _img(self, d):
        return d - self.L * np.round(d / self.L)

    def _celllist(self):
        c = np.floor(self.X / self.L * self.nc).astype(int) % self.nc
        head = {}
        for i, k in enumerate(map(tuple, c)):
            head.setdefault(k, []).append(i)
        return head, c

    def _neighbors(self):
        head, c = self._celllist()
        out = []
        for i in range(self.n):
            acc = []
            cx, cy, cz = c[i]
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    for dz in (-1, 0, 1):
                        acc += head.get(((cx + dx) % self.nc,
                                         (cy + dy) % self.nc,
                                         (cz + dz) % self.nc), [])
            out.append(acc)
        return out

    def density_pressure(self):
        h = self.h
        for i, js in enumerate(self._neighbors()):
            d = self._img(self.X[js] - self.X[i])
            r = np.linalg.norm(d, axis=1)
            m = r < h
            w = K.poly6(r[m], h)
            num = float((self.m[js][m] * w).sum())
            den = float(((self.m[js][m] / self.rho0) * w).sum())
            self.rho[i] = num / max(den, 1e-9)  # Shepard : tue le biais discret
        self.rho = np.maximum(self.rho, 1e-6)
        self.p = self.kp * (self.rho - self.rho0)

    def forces(self, f_ext=None):
        h, nu = self.h, self.nu
        A = np.zeros((self.n, 3))
        OM = np.zeros((self.n, 3))
        for i, js in enumerate(self._neighbors()):
            js = [j for j in js if j != i]
            if not js:
                continue
            d = self._img(self.X[i] - self.X[js])
            r = np.linalg.norm(d, axis=1)
            m = (r < h) & (r > 1e-12)
            if not m.any():
                continue
            d, r = d[m], r[m]
            jj = np.array(js)[m]
            gw = K.spiky_grad(d, r, h)
            pl = K.visco_lap(r, h)
            A[i] += (-((self.p[i] + self.p[jj]) / (2 * self.rho[jj])
                         * self.m[jj])[:, None] * gw).sum(0)
            A[i] += ((nu * self.m[jj] / self.rho[jj])[:, None] * (
                self.V[jj] - self.V[i]) * pl[:, None]).sum(0)
            OM[i] += ((self.m[jj] / self.rho[jj])[:, None]
                      * np.cross(self.V[jj] - self.V[i], gw)).sum(0)
        self.om = OM
        if f_ext is not None:
            A += f_ext(self.X, self.t)
        return A

    def step(self, f_ext=None, dt_max=6e-3):
        vsig = float(np.abs(self.V).max()) + np.sqrt(self.kp / self.rho0)
        dt = min(dt_max, 0.25 * self.h / max(vsig, 1e-6))
        self.density_pressure()
        A = self.forces(f_ext)
        self.V += A * dt
        self.X = (self.X + self.V * dt) % self.L
        self.t += dt
        return dt

    def settle(self, steps=30, damp=0.9):
        for _ in range(steps):
            self.density_pressure()
            self.V = (self.V + self.forces(None) * 1e-3) * damp
            self.X = (self.X + self.V * 1e-3) % self.L
        self.V[:] = 0.0
        self.t = 0.0

    def vmax(self):
        return float(np.linalg.norm(self.V, axis=1).max())

    def energy(self):
        return float(0.5 * (self.m * (self.V ** 2).sum(1)).sum())

    def enstrophy(self):
        w2 = (self.om ** 2).sum(1)
        return float((self.m / self.rho * w2).sum())
