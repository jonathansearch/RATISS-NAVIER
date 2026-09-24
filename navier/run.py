"""Run blowup : repos + forçage -> vmax, Ω (BKM), E, C(t). MIT."""
import numpy as np


def run(n=1500, nu=0.01, T=2.5, force=True, n_pairs=8, seed=7, sample=20,
        quiet=False, snap_every=0, A_in=6.0, A_sw=4.0, A_pulse=10.0):
    from .sph import Flow
    from .vortex import Forcing
    from .qtracers import Tracers
    fl = Flow(n=n, nu=nu, seed=seed)
    fl.settle()
    fc = Forcing(active=force, A_in=A_in, A_sw=A_sw, A_pulse=A_pulse)
    tr = Tracers(n)
    d = np.linalg.norm(fl.X[:, :2] - 2.0, axis=1)
    inner = np.where(d < 0.9)[0][:n_pairs]
    outer = np.where(d > 1.5)[0][:n_pairs]
    tr.bell(list(zip(map(int, inner), map(int, outer))))
    watch = [int(a) for a in inner]
    serie, snaps, s = [], [], 0
    while fl.t < T:
        dt = fl.step(f_ext=fc)
        tr.step(np.linalg.norm(fl.om, axis=1), dt)
        if s % sample == 0:
            serie.append({'t': round(fl.t, 4), 'vmax': round(fl.vmax(), 4),
                          'Om': round(fl.enstrophy(), 4),
                          'E': round(fl.energy(), 4),
                          'C': round(float(np.mean([tr.concurrence(a)
                                                    for a in watch])), 4)})
        if snap_every and s % snap_every == 0:
            snaps.append({'X': fl.X.copy(), 'om': np.linalg.norm(fl.om, axis=1),
                          't': round(fl.t, 3)})
        s += 1
    if not quiet:
        print(f"[run] n={n} nu={nu} force={force} -> "
              f"vmax={serie[-1]['vmax']} Om={serie[-1]['Om']} "
              f"E={serie[-1]['E']} C={serie[-1]['C']} ({len(serie)} pts)")
    return serie, fl, tr, snaps
