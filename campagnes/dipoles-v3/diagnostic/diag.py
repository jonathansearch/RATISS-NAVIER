import sys, numpy as np
sys.path.insert(0,str(__import__('pathlib').Path(__file__).resolve().parents[3])); sys.path.insert(0,str(__import__('pathlib').Path(__file__).resolve().parents[1]))
from navier.sph import Flow
from dipoles import dipole, GAM, RC, L
def mesure(fl):
    fl.density_pressure(); fl.forces(None); w=fl.om; vol=fl.m/fl.rho; w2=(w**2).sum(1)
    Om=float((vol*w2).sum()); return Om, float((vol*(w[:,0]**2+w[:,1]**2)).sum())/Om
Om_th = 4 * GAM**2/(2*np.pi*RC**2) * L    # 4 tourbillons Lamb-Oseen, enstrophie analytique (images négligées)
print(f"Ω théorique 2 dipôles = {Om_th:.1f}")
for n in [500,1500,4500]:
    fl=Flow(n=n,nu=0.001,seed=7); fl.settle()
    fl.V=dipole(fl.X,1,2,1)+dipole(fl.X,3,2,-1); Om,z=mesure(fl)
    V0=fl.V.copy(); fl.V=np.random.default_rng(1).normal(0,0.01,(n,3)); Od,zd=mesure(fl)
    fl.V=V0+np.random.default_rng(1).normal(0,0.01,(n,3)); Om2,z2=mesure(fl)
    print(f"n={n:5d} h={fl.h:.2f} rc/h={RC/fl.h:.2f} | dipôles: Ω={Om:7.1f} ({Om/Om_th:.0%} du théorique) ζ={z:.5f} | poussière seule: Ω={Od:7.2f} ζ={zd:.3f} | les deux: ζ={z2:.4f} prédit≈{zd*Od/(Om+Od):.4f}")
