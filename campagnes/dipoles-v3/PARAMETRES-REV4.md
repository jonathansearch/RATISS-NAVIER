# BRIEF V3 — rév. 4 : paramètres et critères (scellés sur ordre du chef, 02/10/2026, avant tout run rév. 4)

Remplace `PARAMETRES-FIGES.md` (rév. 3, conservé tel quel, témoins rév. 3 « hors critères validés »).
Base : `diagnostic/DIAGNOSTIC-OMEGA.md`. Code : `dipoles_v4.py` (scellé avec ce fichier).

## Ce que la rév. 4 lève et ce qu'elle ne prouve pas
- **Le STOP de T0 (rév. 3) est levé** : la 3D d'un dipôle seul + poussière est cohérente (survit à la moyenne en cellules),
  la poussière seule ne s'amplifie pas → ce n'est pas une fuite de la salle.
- **Hypothèse Crow / elliptique NON prouvée** : aucune longueur d'onde mesurée. À tester en **rév. 5**
  (spectre en z de ω_xy, comparaison aux longueurs d'onde attendues).
- **ω biaisé vers le bas** (20–45 % de l'enstrophie théorique, non convergé : 45 % → 42 % de n=1500 à 4500).
  Pas de facteur de correction possible tant qu'il ne converge pas. Règle : **aucun Ω absolu n'est interprété ;
  les comparaisons se font à n égal**, sur des rapports (ζ, Δζ, facteurs sur base figée). Résolution des cœurs : rév. 5.
- **Compressibilité** : plus repoussée, **mesurée** dans chaque JSON (max|ρ−ρ0|/ρ0, colonne `drho_max`).
  Seuil d'alerte : > 5 % → le run est marqué « compressible », signalé dans le verdict.

## Montage (inchangé sauf la dose)
Comme rév. 3 (Lamb-Oseen Γ=3, rc=0,35, a=0,6, L=4, ν=0,001, T=6, graine flow 7, échantillonnage à chaque pas),
plus : dose de poussière = **0,9 % du v_rms du montage** (rms du vecteur bruit), calculée au départ et écrite dans le JSON.
T2 : pompe plate sèche, poussière 0,01 par composante (comme V2), T=2,5.

## Mesures
Colonnes : t, Om, zeta, Z3D, E, vmax, Om_bas, Om_haut, **zeta_c1** (ζ du ω moyenné sur 64 cellules de taille 1,0), **drho_max**.
Lissage : moyenne glissante 0,1. ζ soutenu := médiane sur t∈[3 ; 6]. Base figée : médiane sur t∈[0,5 ; 1,0].

## Runs (16)
| Groupe | Montage | n | graine poussière |
|---|---|---|---|
| T1 | 2 dipôles, sans poussière | 1500, 4500 | 0 |
| T2 | pompe, ν=0,001 | 4500 | 7 |
| Réf A | 1 dipôle | 500, 1500, 4500 | 1 |
| Coll A | 2 dipôles | 500, 1500, 4500 | 1 |
| Réf B | 1 dipôle | 500, 1500, 4500 | 2 |
| Coll B | 2 dipôles | 500, 1500, 4500 | 2 |
Ordre : T1 + T2 d'abord.

## Témoins (STOP / alarme)
- **Plancher(n)** := ζ_c1 soutenu de T1 au même n. Fuite si > 1e-3 → mesures corrigées := valeur − Plancher(n).
- **T2** : max Ω lissé sur [0,95 ; 2,5] ≥ 3 × base → pic présent à n=4500 ; comparé à 1500 (rév. 3, ×5,3) :
  présent aux deux → phénomène à documenter (pas un fantôme de résolution) ; absent à 4500 → fantôme confirmé.
  Dans les deux cas, T2 ne bloque pas les groupes dipôles (pas de pompe).

## Critères (par graine ; la collision se mesure contre sa référence 1 dipôle, même graine, même n — R8)
Δ := ζ_c1 soutenu(2 dipôles) − ζ_c1 soutenu(1 dipôle).
- **C1 — la collision ajoute de la 3D** : Δ > 2 × Plancher(n) ET ζ_c1(2 dip) ≥ 1,5 × ζ_c1(1 dip), à n=1500 et 4500.
- **C2 — résolu** : à n=4500, C1 tient encore et Δ(4500) ≥ ½ Δ(1500).
- **C3 — concentration** : Z3D_c := ζ_c1 × Ω. Il existe t∈[1 ; 6] où Z3D_c lissé(2 dip) ≥ 3 × sa base ET ≥ 1,5 × Z3D_c lissé(1 dip) au même t,
  avec E(t) ≤ E(1,0). Comparaison à n égal uniquement.
- **C4 — date** : date := argmax sur [1 ; 6] de [Z3D_c lissé(2 dip) − Z3D_c lissé(1 dip)].
  |date(4500) − date(1500)| / date(1500) ≤ 15 % pour chaque graine ; même forme pour A et B (pic intérieur t < 5,8, retombée ≤ 0,7 × pic à T).
- **Anti-bruit** : tout critère positif exige ζ_c1 ≥ ½ ζ (particules) au même instant (sinon : bruit, critère refusé).
- **Verdicts** : 🅰 = C1+C2+C3+C4 pour A et B · 🅱 = C1+C2 sans C3 · 🅾 = jamais C1 (la collision n'ajoute rien au dipôle seul)
  · **inconclusif** si T1 fuit au-delà de 1e-2 ou si un run de critère est « compressible ».
