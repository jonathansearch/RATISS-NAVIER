"""COMMISSAIRE — teste la chaîne causale du blowup : source -> amplificateur -> compteur. MIT.
Usage : python3 campagnes/commissaire-1/commissaire.py TAG n nu seed t_cut force(0/1) T
  t_cut = instant où la pompe est coupée (-1 = jamais)."""
import json, sys, time, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from navier.sph import Flow
from navier.vortex import Forcing

tag, n, nu, seed, t_cut, force, T = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5]), sys.argv[6] == '1', float(sys.argv[7])
fl = Flow(n=n, nu=nu, seed=seed); fl.settle()
fc = Forcing(active=force)
def pump(X, t):
    if t_cut >= 0 and t >= t_cut:
        return np.zeros_like(X)
    return fc(X, t)
out, s, t0 = [], 0, time.time()
while fl.t < T:
    F = pump(fl.X, fl.t)
    P = float((fl.m[:, None] * fl.V * F).sum())          # puissance injectée par la pompe
    fl.step(f_ext=pump)
    if not np.isfinite(fl.V).all():
        out.append({'t': fl.t, 'CRASH': True}); break
    if s % 10 == 0:
        w = fl.om; wz2 = float((w[:, 2] ** 2).mean()); wp2 = float((w[:, :2] ** 2).mean())
        out.append({'t': round(fl.t, 4), 'Om': round(fl.enstrophy(), 5), 'vmax': round(fl.vmax(), 4),
                    'E': round(fl.energy(), 5), 'P': round(P, 5),
                    'r3D': round((wp2 / max(wz2, 1e-30)) ** 0.5, 5)})   # vorticité hors-plan / dans le plan
    s += 1
res = {'tag': tag, 'n': n, 'nu': nu, 'seed': seed, 't_cut': t_cut, 'force': force, 'T': T,
       'secondes': round(time.time() - t0), 'serie': out}
(HERE / 'runs').mkdir(exist_ok=True)
json.dump(res, open(HERE / 'runs' / f'{tag}.json', 'w'))
print(tag, 'fini', res['secondes'], 's', out[-1], flush=True)
