"""Run visuel n=6000 par chunks (pickle reprise). Usage :
visual_chunk.py --t0 0 --t1 0.85 [--fresh]. MIT."""
import sys
sys.path.insert(0, '/home/user/RATISS-NAVIER')
import json
import os
import pickle
import numpy as np

D = '/home/user/RATISS-NAVIER/demos/'
PK = D + 'visual_state.pkl'


def main():
    a = sys.argv
    t0 = float(a[a.index('--t0') + 1])
    t1 = float(a[a.index('--t1') + 1])
    fresh = '--fresh' in a
    nu = float(a[a.index('--nu') + 1]) if '--nu' in a else 0.001
    tag = a[a.index('--tag') + 1] if '--tag' in a else 'visual'
    PK = D + tag + '_state.pkl'
    FS, FN = D + tag + '_serie.json', D + tag + '_snaps.json'
    from navier.sph import Flow
    from navier.vortex import Forcing
    from navier.qtracers import Tracers
    if fresh or not os.path.exists(PK):
        fl = Flow(n=6000, nu=nu, seed=7)
        fl.settle()
        fc = Forcing(A_in=8.0, A_sw=6.0, A_pulse=14.0)
        tr = Tracers(6000)
        d = np.linalg.norm(fl.X[:, :2] - 2.0, axis=1)
        inner = np.where(d < 0.9)[0][:8]
        outer = np.where(d > 1.5)[0][:8]
        tr.bell(list(zip(map(int, inner), map(int, outer))))
        watch = [int(x) for x in inner]
        serie, snaps, s = [], [], 0
        pickle.dump({'fl': fl, 'tr': tr, 'watch': watch, 's': 0}, open(PK, 'wb'))
        json.dump([], open(FS, 'w'))
        json.dump([], open(FN, 'w'))
    else:
        st = pickle.load(open(PK, 'rb'))
        fl, tr, watch, s = st['fl'], st['tr'], st['watch'], st['s']
        fc = Forcing(A_in=8.0, A_sw=6.0, A_pulse=14.0)
        serie = json.load(open(FS))
        snaps = json.load(open(FN))
    n0 = s
    crash = False
    while fl.t < t1:
        dt = fl.step(f_ext=fc)
        if not (np.isfinite(fl.V).all() and np.isfinite(fl.rho).all()):
            print(f'[boss] CRASH a t={fl.t:.3f}', flush=True)
            crash = True
            break
        tr.step(np.linalg.norm(fl.om, axis=1), dt)
        if s % 10 == 0:
            serie.append({'t': round(fl.t, 4), 'vmax': round(fl.vmax(), 4),
                          'Om': round(fl.enstrophy(), 2),
                          'E': round(fl.energy(), 2),
                          'C': round(float(np.mean([tr.concurrence(x) for x in watch])), 4)})
        if s % 15 == 0:
            snaps.append({'X': fl.X.tolist(), 'V': fl.V.tolist(),
                          'om': np.linalg.norm(fl.om, axis=1).tolist(),
                          't': round(fl.t, 3)})
        s += 1
    pickle.dump({'fl': fl, 'tr': tr, 'watch': watch, 's': s}, open(PK, 'wb'))
    json.dump(serie, open(FS, 'w'))
    json.dump(snaps, open(FN, 'w'))
    print(f'[{tag}] t={fl.t:.2f} crash={crash} steps={s - n0} Om={serie[-1]["Om"]} '
          f'C={serie[-1]["C"]} frames={len(snaps)}', flush=True)


if __name__ == '__main__':
    main()
