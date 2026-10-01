"""analyse.py — applique les critères scellés (CRITERES-SCELLES.md) + M2 réseau d'influence. MIT."""
import json, glob, pathlib
import numpy as np
H = pathlib.Path(__file__).resolve().parent
R = {json.load(open(f))['tag']: json.load(open(f)) for f in sorted(glob.glob(str(H / 'runs' / '*.json')))}

def zmoy(s, k='zeta'): return float(np.mean([p[k] for p in s if p['t'] >= 0.5 and k in p]))
def soutenu(s, seuil=0.10, duree=0.5):
    best, t0 = 0.0, None
    for p in s:
        if p['zeta'] > seuil:
            t0 = p['t'] if t0 is None else t0; best = max(best, p['t'] - t0)
        else: t0 = None
    return best >= duree, round(best, 3)
def patineuse(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[j]['t'] - s[i]['t'] > 0.3: break
            if max(s[j]['sect']) >= 1.2 * max(s[i]['sect']) and s[j]['E'] < s[i]['E']:
                return True, s[i]['t'], s[j]['t']
    return False, None, None
def evenement(s):
    a = [p for p in s if p['t'] > 1.0]
    k = int(np.argmax([p['Om'] for p in a]))
    return (None if k == 0 or a[k]['t'] <= 1.05 else a[k]['t']), round(a[k]['Om'] / a[0]['Om'], 3)
def reseau(s, lagmax=10):
    """M2 : 32 secteurs ; pour chaque paire, retard du max de corrélation croisée (signaux détrendus, normalisés).
    Boucle réciproque = paire (i,j) où i mène j à un retard ET j mène i à un autre retard, les deux > 0,5."""
    S = np.array([p['sect'] for p in s if p['t'] >= 1.0]).T
    S = (S - S.mean(1, keepdims=True)) / (S.std(1, keepdims=True) + 1e-12)
    m = S.shape[1]; boucles = 0; liens = 0
    for i in range(32):
        for j in range(i + 1, 32):
            c = {L: float(np.mean(S[i, :m - L] * S[j, L:])) if L >= 0 else float(np.mean(S[i, -L:] * S[j, :m + L]))
                 for L in range(-lagmax, lagmax + 1) if L != 0}
            pos = max(v for L, v in c.items() if L > 0); neg = max(v for L, v in c.items() if L < 0)
            liens += (pos > 0.5) + (neg > 0.5); boucles += (pos > 0.5 and neg > 0.5)
    return liens, boucles

print(f"{'run':22s} {'ζ moy':>7s} {'ζ>0,1 soutenu':>14s} {'ωx²+ωz²':>8s} {'ωx²':>7s} {'patineuse':>10s} {'événement':>10s} {'M2 liens/boucles':>17s}")
T = {}
for k, d in R.items():
    s = d['serie']
    if 'CRASH' in s[-1]: print(k, 'CRASH', s[-1]); continue
    sou = soutenu(s); pat = patineuse(s); ev = evenement(s); lb = reseau(s)
    T[k] = dict(z=zmoy(s), sou=sou, xz=zmoy(s, 'z_xz') if 'z_xz' in s[-1] else None, x=zmoy(s, 'z_x') if 'z_x' in s[-1] else None, pat=pat, ev=ev, lb=lb)
    xz = f"{T[k]['xz']:.4f}" if T[k]['xz'] is not None else '   —   '
    x = f"{T[k]['x']:.4f}" if T[k]['x'] is not None else '  —  '
    print(f"{k:22s} {T[k]['z']:7.4f} {str(sou[0])+' '+str(sou[1]):>14s} {xz:>8s} {x:>7s} {str(pat[0]):>10s} {str(ev[0])+' x'+str(ev[1]):>10s} {str(lb):>17s}")

# Gagnante (n=500, dust-7)
cands = {'E1': 'R03_E1', 'E2': 'R04_E2', 'E3': 'R02_E3'}
g = max(cands, key=lambda e: T[cands[e]]['z'])
print('\nÉtreinte gagnante (ζ moyen max, n=500, dust-7) :', g)
z500, z1500 = T['R02_E3']['z'], T['R08_E3_n1500']['z']
e1000, e1500 = T['R07_E3_n1000']['ev'][0], T['R08_E3_n1500']['ev'][0]
conv = (e1000 is not None and e1500 is not None and abs(e1500 - e1000) / ((e1000 + e1500) / 2) <= 0.15)
A = dict(zeta_soutenu=T['R02_E3']['sou'][0], ne_fond_pas=z1500 >= z500, patineuse=T['R02_E3']['pat'][0],
         date_convergente=conv)
print('Critères 🅰 sur', g, ':', A, f"(ζ500={z500:.4f}, ζ1500={z1500:.4f}, événements n1000={e1000}, n1500={e1500})")
plate = all(T[cands[e]]['z'] < 0.02 for e in cands)
print('VERDICT (lettre des critères) :', '🅰' if all(A.values()) else ('🅾' if plate else '🅱'))
json.dump({'tableau': {k: {**v, 'pat': list(v['pat'])} for k, v in T.items()}, 'gagnante': g, 'criteres_A': A,
           'verdict_lettre': '🅰' if all(A.values()) else ('🅾' if plate else '🅱')},
          open(H / 'VERDICT.json', 'w'), indent=1, default=str)
