"""Chasse au blowup : force ON vs OFF + fit BKM + GIF.
Usage : --only ON | --only OFF | (rien = gif depuis snaps.json). MIT."""
import sys
sys.path.insert(0, '/home/user/RATISS-NAVIER')
import json
import os
import numpy as np

D = '/home/user/RATISS-NAVIER/demos/'


def fit_bkm(ts, Om):
    ts, Om = np.array(ts), np.array(Om)
    m = (ts > 1.0) & (Om > 1e-6)
    ts, Om = ts[m], Om[m]
    if len(ts) < 4:
        return {'exp_rate': 0.0, 'bkm_Tstar': None, 'bkm_R': 0.0}
    exp = np.polyfit(ts, np.log(Om), 1)
    best = (-2, ts[-1] + 1.0)
    for Ts in np.linspace(ts[-1] + 0.2, ts[-1] + 3.0, 12):
        with np.errstate(all='ignore'):
            r = np.corrcoef(np.log(Ts - ts), np.log(Om))[0, 1]
        if np.isfinite(r) and r > best[0]:
            best = (r, Ts)
    return {'exp_rate': round(float(exp[0]), 3),
            'bkm_Tstar': round(float(best[1]), 2),
            'bkm_R': round(float(best[0]), 4)}


def do_run(tag, force):
    from navier.run import run
    s, fl, tr, snaps = run(n=1500, T=2.5, force=force, sample=40,
                           snap_every=120 if force else 0, quiet=True)
    R = {}
    if os.path.exists(D + 'blowup.json'):
        R = json.load(open(D + 'blowup.json'))
    R[tag] = {'serie': s, 'fit': fit_bkm([p['t'] for p in s], [p['Om'] for p in s])}
    json.dump(R, open(D + 'blowup.json', 'w'))
    if snaps:
        json.dump(snaps, open(D + 'snaps.json', 'w'),
                  default=lambda o: o.tolist() if hasattr(o, 'tolist') else o)
    print(f"[blowup] force {tag}: vmax={s[-1]['vmax']} Om={s[-1]['Om']} "
          f"E={s[-1]['E']} C={s[-1]['C']} fit={R[tag]['fit']}", flush=True)


def do_gif():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    R = json.load(open(D + 'blowup.json'))
    snaps = json.load(open(D + 'snaps.json'))
    S = R['ON']['serie']
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.4, 3.4), dpi=80)
    NF = len(snaps)

    def frame(i):
        ax1.clear()
        ax2.clear()
        sn = snaps[i]
        X = np.array(sn['X'])
        om = np.array(sn['om'])
        m = np.abs(X[:, 2] - 2.0) < 0.5
        ax1.scatter(X[m, 0], X[m, 1], c=om[m], s=8, cmap='inferno', vmin=0, vmax=8)
        ax1.set_xlim(0, 4)
        ax1.set_ylim(0, 4)
        ax1.set_aspect('equal')
        ax1.set_title(f"Coupe |vorticite| t={sn['t']:.2f}")
        ts = [p['t'] for p in S]
        ax2.plot(ts, [p['Om'] for p in S], 'r-', label='enstrophie Ω')
        ax2.plot(ts, np.array([p['vmax'] for p in S]) * 10, 'b--', label='vmax×10')
        ax2.plot(ts, np.array([p['C'] for p in S]) * 200, 'g-', label='C×200 (sonde)')
        ax2.axvline(sn['t'], color='k', lw=0.8)
        ax2.set_xlim(0, 2.5)
        ax2.legend(fontsize=7)
        ax2.grid(alpha=0.3)
        ax2.set_title('Chasse au blowup (force ON)')
        return []

    FuncAnimation(fig, frame, frames=NF, interval=100).save(D + 'blowup.gif', writer='pillow')
    print('[blowup] gif ok')


if __name__ == '__main__':
    if '--only' in sys.argv:
        tag = sys.argv[sys.argv.index('--only') + 1]
        do_run(tag, tag == 'ON')
    else:
        do_gif()
