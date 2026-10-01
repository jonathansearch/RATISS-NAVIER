# Annexe au BRIEF V3 rév. 3 — paramètres figés (écrits par l'agent, scellés AVEC le brief, avant tout run)

Le brief laisse quelques mots sans chiffre. Ils sont fixés ici, une fois pour toutes.

## Montage (dipoles.py)
- Boîte périodique L=4, code `navier/sph.py` intouché, `Flow(n, nu, seed=7)` puis `settle()`.
  Le jitter de réseau du code (0,002·L/m, graine 7) et la couche incomplète si n n'est pas un cube
  sont du **bruit propre du code** : ils font partie du Plancher (T1), ce n'est pas de la poussière.
- Dipôle = deux tourbillons de Lamb-Oseen, uniformes en z (vorticité 100 % selon z à t=0 :
  ζ=0 analytiquement), Γ=±3, rayon de cœur rc=0,35, demi-écart a=0,6, images périodiques ±1.
  Vitesse propre ≈ Γ/(4πa) ≈ 0,40.
- 1 dipôle (T0) : centre (1,0 ; 2,0), avance vers +x. 2 dipôles : (1,0 ; 2,0) vers +x et (3,0 ; 2,0) vers −x.
- Police ν=0,001 (V2 : 0,01). dt du code (dt_max=6e-3). T=6.
- Poussière : V += N(0 ; 0,01) sur les 3 composantes, `numpy.random.default_rng(graine)`.
  Graine A=1, graine B=2, T0 : graine 1. T1 : aucune poussière.
- T2 : `Etreinte(mode='plate', coupure='sec')` (t_cut=1), n=1500, ν=0,001, poussière graine 7, T=2,5.

## Mesures — chaque pas (pas de grille)
t, Ω=Σ vol·|ω|², ζ=Σ vol·(ωx²+ωy²)/Ω, Z3D=ζ·Ω, E, vmax, Ω haut/bas (z≷L/2). Config complète écrite dans chaque JSON.

## Définitions figées
- **Lissage** : moyenne glissante sur 0,1 unité de temps (quantités intégrées, jamais le pas brut).
- **ζ soutenu** := médiane de ζ sur t∈[3 ; 6] (« après le contact »).
- **Plancher** := ζ soutenu de T1.
- **STOP T0 / alarme T1** : ζ soutenu > 2×Plancher (T0) ; pour T1, « fuite » si ζ soutenu_T1 > 1e-3
  → mesure corrigée = ζ − Plancher partout.
- **Base figée** (seule base autorisée pour tout facteur) : médiane sur t∈[0,5 ; 1,0].
- **C1** : ζ soutenu > 2×Plancher à n=1500 ET 4500 (pour chaque graine).
- **C2** : ζ soutenu(4500) > 2×Plancher ET ≥ ½·ζ soutenu(1500).
- **C3** : max sur t∈[1 ; 6] de Z3D lissé ≥ 3×base(Z3D), avec E(t_pic) ≤ E(1,0).
- **Date du pic** := argmax sur t∈[1 ; 6] de Z3D lissé. **C4** : |date(4500)−date(1500)|/date(1500) ≤ 15 %
  pour chaque graine, ET même forme pour A et B = pic intérieur (t_pic < 5,8) et retombée
  Z3D lissé(T) ≤ 0,7×pic.
- **T2 pic fantôme** : max Ω lissé sur [0,95 ; 2,5] ≥ 3×base(Ω) → inconclusif provisoire ;
  re-run à une autre résolution seulement sur ordre du chef.
- **Verdicts** : par graine, puis campagne = 🅰 / 🅱 / 🅾 / inconclusif comme au §4 du brief
  (🅰 exige les deux graines).
