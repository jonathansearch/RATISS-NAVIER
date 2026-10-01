"""campagne.py — MISSION 3D, conforme au brief. MIT.
Usage : python3 campagne.py TAG mode n dust_seed(0=aucune) coupure [T]
Mesures : M1 ζ(t), M2 enstrophie par secteur 4×4×2, M3/M4 en post-traitement (analyse.py), M5 E/Ω/vmax/crash."""
import json, sys, time, pathlib, os
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
NAV = pathlib.Path(os.environ['RATISS_HOME']) / 'RATISS-NAVIER' if os.environ.get('RATISS_HOME') else HERE.parents[1]
sys.path.insert(0, str(NAV))
from navier.sph import Flow
from navier.furniture import Etreinte

tag, mode, n, ds, coup = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
T = float(sys.argv[6]) if len(sys.argv) > 6 else 2.5
NU = float(sys.argv[7]) if len(sys.argv) > 7 else 0.01
EPS = 0.01
fl = Flow(n=n, nu=NU, seed=7); fl.settle()
if ds:
    fl.V += np.random.default_rng(ds).normal(0, EPS, (n, 3))
F = Etreinte(mode=mode, coupure=coup)
out, s, t0 = [], 0, time.time()
while fl.t < T:
    fl.step(f_ext=F)
    if not (np.isfinite(fl.V).all() and np.isfinite(fl.rho).all()):
        out.append({'t': round(fl.t, 4), 'CRASH': True}); print(tag, 'CRASH', fl.t, flush=True); break
    if s % 10 == 0:
        w, vol = fl.om, fl.m / fl.rho
        w2 = (w ** 2).sum(1)
        Om = float((vol * w2).sum()); Eh = float((vol * (w[:, :2] ** 2).sum(1)).sum())
        idx = (np.floor(fl.X[:, 0] / fl.L * 4).astype(int) % 4) * 8 + (np.floor(fl.X[:, 1] / fl.L * 4).astype(int) % 4) * 2 + (np.floor(fl.X[:, 2] / fl.L * 2).astype(int) % 2)
        sect = np.bincount(idx, weights=vol * w2, minlength=32)
        out.append({'t': round(fl.t, 4), 'Om': round(Om, 5), 'zeta': round(Eh / max(Om, 1e-30), 6), 'z_xz': round(float((vol * (w[:, 0] ** 2 + w[:, 2] ** 2)).sum()) / max(Om, 1e-30), 6), 'z_x': round(float((vol * w[:, 0] ** 2).sum()) / max(Om, 1e-30), 6),
                    'E': round(fl.energy(), 5), 'vmax': round(fl.vmax(), 4), 'sect': [round(float(x), 4) for x in sect]})
    s += 1
(HERE / 'runs').mkdir(exist_ok=True)
json.dump({'tag': tag, 'mode': mode, 'n': n, 'nu': NU, 'eps': EPS if ds else 0.0, 'dust_seed': ds, 'coupure': coup,
           't_cut': 1.0, 'T': T, 'secondes': round(time.time() - t0), 'serie': out}, open(HERE / 'runs' / f'{tag}.json', 'w'))
print(tag, round(time.time() - t0), 's ok', flush=True)
