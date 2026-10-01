import sys, numpy as np
sys.path.insert(0,str(__import__('pathlib').Path(__file__).resolve().parents[3])); from navier.sph import Flow
n=int(sys.argv[1]); fl=Flow(n=n,nu=0.001,seed=7); fl.settle(); fl.V+=np.random.default_rng(1).normal(0,0.01,(n,3))
nxt=0
while fl.t<3.0:
    fl.step()
    if fl.t>=nxt:
        w=fl.om; vol=fl.m/fl.rho; w2=(w**2).sum(1); Om=(vol*w2).sum()
        print(f"n={n} t={fl.t:.2f} Ω={Om:.3f} ζ={(vol*(w[:,0]**2+w[:,1]**2)).sum()/max(Om,1e-30):.3f} E={fl.energy():.5f} vmax={fl.vmax():.3f}",flush=True); nxt+=0.5
