"""Tests RATISS-NAVIER : repos stable, forçage -> vortex, sonde quantique. MIT."""
import os as _os, pathlib as _pl  # RATISS: chemins portables (dépôts clonés côte à côte, ou RATISS_HOME)
_RATISS_HOME = _os.environ.get('RATISS_HOME') or str(_pl.Path(__file__).resolve().parents[2])
import sys
sys.path.insert(0, (_RATISS_HOME + '/RATISS-NAVIER'))


def test_repos_stable():
    from navier.run import run
    s, _, _, _ = run(n=400, T=0.4, force=False, quiet=True)
    assert s[-1]['E'] < 3.0, s[-1]
    assert s[-1]['vmax'] < 1.0, s[-1]


def test_forcage_vortex():
    from navier.run import run
    s, _, _, _ = run(n=400, T=0.6, force=True, quiet=True)
    assert s[-1]['Om'] > 5 * max(s[0]['Om'], 1e-6), s[-1]
    assert s[-1]['vmax'] > 0.5, s[-1]


def test_sonde_quantique():
    from navier.run import run
    s, _, _, _ = run(n=400, T=0.6, force=True, quiet=True)
    assert s[-1]['C'] < 1.0, s[-1]
    assert s[-1]['C'] >= 0.0, s[-1]


def test_energie_bornee():
    from navier.run import run
    s, _, _, _ = run(n=400, T=0.6, force=True, quiet=True)
    assert s[-1]['E'] < 500, s[-1]
