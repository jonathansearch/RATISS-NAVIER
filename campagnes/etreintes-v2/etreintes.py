"""Campagne des 3 étreintes. Usage : python3 scripts/etreintes.py TAG mode n eps dust_seed coupure [nu] [T]. MIT."""
import json, sys, time, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from navier.sph import Flow
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from furniture_v2 import Pompe3D, poussiere

tag, mode, n, eps, ds, coup = sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
nu = float(sys.argv[7]) if len(sys.argv) > 7 else 0.01
T = float(sys.argv[8]) if len(sys.argv) > 8 else 2.5
fl = Flow(n=n, nu=nu, seed=7); fl.settle()
fl.V = poussiere(fl.V, eps, ds)
P = Pompe3D(mode=mode, t_cut=1.0, coupure=coup)
out, s, t0 = [], 0, time.time()
while fl.t < T:
    P.V = fl.V
    fl.step(f_ext=P)
    if not np.isfinite(fl.V).all():
        out.append({'t': fl.t, 'CRASH': True}); break
    if s % 10 == 0:
        w = fl.om; vol = fl.m / fl.rho
        Ez = float((vol * w[:, 2] ** 2).sum()); Eh = float((vol * (w[:, :2] ** 2).sum(1)).sum())
        top = fl.X[:, 2] > fl.L / 2
        out.append({'t': round(fl.t, 4), 'Om': round(Ez + Eh, 5), 'zeta': round(Eh / max(Ez + Eh, 1e-30), 5),
                    'E': round(fl.energy(), 5), 'wmax': round(float(np.linalg.norm(w, axis=1).max()), 4),
                    'Om_haut': round(float((vol[top] * (w[top] ** 2).sum(1)).sum()), 4),
                    'Om_bas': round(float((vol[~top] * (w[~top] ** 2).sum(1)).sum()), 4)})
    s += 1
(pathlib.Path(__file__).resolve().parent).mkdir(exist_ok=True)
json.dump({'tag': tag, 'mode': mode, 'n': n, 'eps': eps, 'dust_seed': ds, 'coupure': coup, 'nu': nu, 'T': T,
           'secondes': round(time.time() - t0), 'serie': out}, open(pathlib.Path(__file__).resolve().parent / f'{tag}.json', 'w'))
print(tag, round(time.time() - t0), 's', out[-1], flush=True)
