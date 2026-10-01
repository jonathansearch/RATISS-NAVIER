import sys, numpy as np
sys.path.insert(0,str(__import__('pathlib').Path(__file__).resolve().parents[3])); sys.path.insert(0,str(__import__('pathlib').Path(__file__).resolve().parents[1]))
from navier.sph import Flow; from dipoles import dipole, L
mont, ds = sys.argv[1], int(sys.argv[2]); n=500
fl=Flow(n=n,nu=0.001,seed=7); fl.settle()
fl.V = dipole(fl.X,1,2,1) if mont=='1dip' else dipole(fl.X,1,2,1)+dipole(fl.X,3,2,-1)
if ds: fl.V += np.random.default_rng(ds).normal(0,0.01,(n,3))
for tc in [0.0,1.0,2.0,3.0]:
    while fl.t<tc: fl.step()
    fl.density_pressure(); fl.forces(None); w=fl.om; vol=fl.m/fl.rho
    zp=(vol*(w[:,0]**2+w[:,1]**2)).sum()/(vol*(w**2).sum(1)).sum()
    out=[]
    for k in (4,2):   # cellules de taille 1,0 et 2,0
        c=np.floor(fl.X/L*k).astype(int)%k; idx=c[:,0]*k*k+c[:,1]*k+c[:,2]
        W=np.array([np.bincount(idx,weights=vol*w[:,j],minlength=k**3) for j in range(3)]).T
        out.append(((W[:,0]**2+W[:,1]**2).sum()/(W**2).sum()))
    # rapport : ce qui survit à la moyenne / ce qui existe particule par particule (hors plan, et dans le plan)
    print(f"{mont} dust{ds} t={fl.t:.2f} ζ_particules={zp:.4f} ζ_cellules1.0={out[0]:.4f} ζ_cellules2.0={out[1]:.4f}",flush=True)
