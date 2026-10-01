"""Analyse des témoins selon PARAMETRES-FIGES.md (scellé)."""
import json, numpy as np, pathlib
R = pathlib.Path(__file__).parent / 'runs'
def load(t):
    d = json.load(open(R / f'{t}.json')); a = np.array([r for r in d['serie'] if r[1] != 'CRASH'], float); return d, a
def lisse(a, col):
    t = a[:, 0]; out = np.empty(len(t))
    for i, ti in enumerate(t): m = np.abs(t - ti) <= 0.05; out[i] = a[m, col].mean()
    return out
def soutenu(a): m = (a[:, 0] >= 3) & (a[:, 0] <= 6); return float(np.median(a[m, 2]))
def base(a, col): m = (a[:, 0] >= 0.5) & (a[:, 0] <= 1.0); return float(np.median(a[m, col]))
out = {}
_, t1 = load('T1_2dip_n500_sec'); P = soutenu(t1)
out['Plancher'] = P; out['T1_fuite'] = P > 1e-3
for t in ['T0_1dip_n500', 'T0_1dip_n1500']:
    d, a = load(t); z = soutenu(a)
    out[t] = {'zeta_soutenu': z, 'ratio_plancher': z / P, 'STOP': z > 2 * P, 'zeta_t0': a[0, 2], 'E0': a[0, 4], 'Efin': a[-1, 4], 'tfin': a[-1, 0]}
d, a = load('T2_ctrl_pompe_n1500'); Ol = lisse(a, 1); m = (a[:, 0] >= 0.95)
i = Ol[m].argmax(); b = base(a, 1)
out['T2'] = {'max_Om_lisse_post': float(Ol[m][i]), 't': float(a[m, 0][i]), 'base': b, 'facteur': float(Ol[m][i] / b), 'fantome': bool(Ol[m][i] / b >= 3), 'tfin': a[-1, 0]}
out['T1_detail'] = {'zeta_t0': t1[0, 2], 'zeta_max': float(t1[:, 2].max()), 'E0': t1[0, 4], 'Efin': t1[-1, 4], 'tfin': t1[-1, 0], 'npas': len(t1)}
print(json.dumps(out, indent=1, default=float))
json.dump(out, open(pathlib.Path(__file__).parent / 'TEMOINS.json', 'w'), indent=1, default=float)
