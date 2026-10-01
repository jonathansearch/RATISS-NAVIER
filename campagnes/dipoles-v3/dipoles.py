"""dipoles.py — BRIEF V3, montage dipôles. MIT.
Usage : python3 dipoles.py TAG montage(1dip|2dip|T2) n graine_poussiere(0=aucune) [T]"""
import json, sys, time, pathlib, os
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
NAV = pathlib.Path(os.environ['RATISS_HOME']) / 'RATISS-NAVIER' if os.environ.get('RATISS_HOME') else HERE.parents[1]
sys.path.insert(0, str(NAV))
from navier.sph import Flow

L, NU, GAM, RC, A, EPS = 4.0, 0.001, 3.0, 0.35, 0.6, 0.01

def lamb_oseen(X, x0, y0, g):
    V = np.zeros((len(X), 3))
    for ix in (-1, 0, 1):
        for iy in (-1, 0, 1):
            dx = X[:, 0] - (x0 + ix * L); dy = X[:, 1] - (y0 + iy * L)
            r2 = np.maximum(dx * dx + dy * dy, 1e-12)
            f = g / (2 * np.pi * r2) * (1 - np.exp(-r2 / RC ** 2))
            V[:, 0] += -f * dy; V[:, 1] += f * dx
    return V

def dipole(X, xc, yc, sens):  # sens=+1 avance vers +x
    return lamb_oseen(X, xc, yc + A, -sens * GAM) + lamb_oseen(X, xc, yc - A, sens * GAM)

if __name__ == '__main__':
    tag, mont, n, ds = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    T = float(sys.argv[5]) if len(sys.argv) > 5 else (2.5 if mont == 'T2' else 6.0)
    fl = Flow(n=n, nu=NU, seed=7); fl.settle()
    F = None
    if mont == '1dip': fl.V = dipole(fl.X, 1.0, 2.0, +1)
    elif mont == '2dip': fl.V = dipole(fl.X, 1.0, 2.0, +1) + dipole(fl.X, 3.0, 2.0, -1)
    elif mont == 'T2':
        from navier.furniture import Etreinte
        F = Etreinte(mode='plate', coupure='sec')
    else: raise SystemExit('montage inconnu')
    if ds: fl.V += np.random.default_rng(ds).normal(0, EPS, (n, 3))
    cfg = {'tag': tag, 'montage': mont, 'n': n, 'nu': NU, 'L': L, 'graine_flow': 7, 'poussiere': bool(ds),
           'graine_poussiere': ds, 'eps': EPS if ds else 0.0, 'Gamma': GAM, 'rc': RC, 'a': A,
           'coupure': 'sec t_cut=1.0' if mont == 'T2' else 'aucune (pas de pompe)', 'T': T,
           'echantillonnage': 'chaque pas', 'commande': ' '.join(['python3', 'dipoles.py'] + sys.argv[1:])}
    S, t0 = [], time.time()
    while fl.t < T:
        fl.step(f_ext=F)
        if not (np.isfinite(fl.V).all() and np.isfinite(fl.rho).all()):
            S.append([round(fl.t, 5), 'CRASH']); print(tag, 'CRASH', fl.t, flush=True); break
        w, vol = fl.om, fl.m / fl.rho; w2 = (w ** 2).sum(1)
        Om = float((vol * w2).sum()); Zh = float((vol * (w[:, 0] ** 2 + w[:, 1] ** 2)).sum())
        hb = fl.X[:, 2] < L / 2
        S.append([round(fl.t, 5), Om, Zh / max(Om, 1e-30), Zh, fl.energy(), fl.vmax(),
                  float((vol * w2)[hb].sum()), float((vol * w2)[~hb].sum())])
    (HERE / 'runs').mkdir(exist_ok=True)
    cfg.update({'colonnes': ['t', 'Om', 'zeta', 'Z3D', 'E', 'vmax', 'Om_bas', 'Om_haut'],
                'secondes': round(time.time() - t0), 'serie': S})
    json.dump(cfg, open(HERE / 'runs' / f'{tag}.json', 'w'))
    print(tag, cfg['secondes'], 's ok', flush=True)
