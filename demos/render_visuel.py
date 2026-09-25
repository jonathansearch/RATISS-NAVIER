"""Rendu ciné n=6000 : coupes + quiver + 3D + courbes. MIT."""
import sys
sys.path.insert(0, '/home/user/RATISS-NAVIER')
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

D = '/home/user/RATISS-NAVIER/demos/'
snaps = json.load(open(D + 'visual_snaps.json'))
serie = json.load(open(D + 'visual_serie.json'))
NF = len(snaps)
print(f'[rendu] {NF} frames, n=6000', flush=True)

fig, ((a1, a2), (a3, a4)) = plt.subplots(2, 2, figsize=(8, 6), dpi=90)


def frame(i):
    for ax in (a1, a2, a3, a4):
        ax.clear()
    sn = snaps[i]
    X = np.array(sn['X'])
    V = np.array(sn['V'])
    om = np.array(sn['om'])
    m = np.abs(X[:, 2] - 2.0) < 0.4
    a1.scatter(X[m, 0], X[m, 1], c=om[m], s=6, cmap='inferno', vmin=0, vmax=15)
    q = np.where(m)[0][::12]
    a1.quiver(X[q, 0], X[q, 1], V[q, 0], V[q, 1], color='cyan', alpha=0.6,
              width=0.004, scale=30)
    a1.set_xlim(0, 4)
    a1.set_ylim(0, 4)
    a1.set_aspect('equal')
    a1.set_title(f"Coupe xy + vitesses t={sn['t']:.2f}")
    m2 = np.abs(X[:, 1] - 2.0) < 0.4
    a2.scatter(X[m2, 0], X[m2, 2], c=om[m2], s=6, cmap='inferno', vmin=0, vmax=15)
    a2.set_xlim(0, 4)
    a2.set_ylim(0, 4)
    a2.set_aspect('equal')
    a2.set_title('Coupe xz (le spaghetti ?)')
    proj = X[:, 0] * 0.8 + X[:, 2] * 0.35
    a3.scatter(proj, X[:, 1], c=om, s=3, cmap='plasma', vmin=0, vmax=15, alpha=0.7)
    a3.set_title('Vue 3D inclinée (6000 particules)')
    ts = [p['t'] for p in serie]
    a4.plot(ts, [p['Om'] for p in serie], 'r-', label='Ω')
    a4.plot(ts, np.array([p['C'] for p in serie]) * 30000, 'g-', label='C×30000')
    a4.axvline(sn['t'], color='k', lw=0.8)
    a4.set_xlim(0, 2.5)
    a4.legend(fontsize=7)
    a4.grid(alpha=0.3)
    a4.set_title('Enstrophie vs sonde')
    return []


FuncAnimation(fig, frame, frames=NF, interval=130).save(D + 'visuel6000.gif', writer='pillow')
print('[rendu] gif ok')
