# Diagnostic de l'instrument ω (02/10/2026) — à lire avant toute rév. 4 de V3

Scripts : `diag.py` (instantané, sans pas de temps), `dust.py`, `coarse.py` (n=500/1500, ν=0,001, graine flow 7). 🧮 calcul pur.

## 1. Le ω du code SPH sous-estime l'enstrophie, et ne converge pas encore
2 dipôles Lamb-Oseen (Γ=3, rc=0,35), Ω théorique ≈ 187 (4 tourbillons, images négligées).
| n | h | rc/h | Ω mesuré | part du théorique |
|---|---|---|---|---|
| 500 | 0,71 | 0,50 | 38,2 | 20 % |
| 1500 | 0,49 | 0,72 | 83,4 | 45 % |
| 4500 | 0,34 | 1,03 | 78,9 | 42 % |
→ Les Ω absolus de toutes les campagnes sont biaisés vers le bas ; les cœurs ne sont pas résolus (rc/h ≤ 1).

## 2. Ω contient de la croissance qui n'est pas physique
T1 (2 dipôles plats, sans poussière, ζ ≈ 0) : Ω passe de 31 à 707 sans aucune force pendant que E baisse (11,0 → 7,3).
En 2D visqueux incompressible, l'enstrophie ne peut que décroître. Le code est faiblement compressible (Mach ≈ 0,18),
donc ce n'est pas une preuve formelle, mais c'est un signal fort : une grande partie de Ω tardif est fabriquée par le schéma.

## 3. ζ est un rapport de mélange
Poussière isotrope seule : ζ = 0,67–0,69 (= 2/3, comme attendu pour du bruit isotrope).
Dipôles + poussière à t=0 : ζ mesuré = ζ prédit par le mélange (0,0006/0,0005 ; 0,0007/0,0007 ; 0,0013/0,0013).
→ Un ζ faible (0,1 %) peut n'être que la part d'enstrophie de la poussière. L'hypothèse « 0,19 % » doit être jugée avec ça en tête.

## 4. La poussière seule ne s'amplifie pas
Sans écoulement, Ω_poussière reste 0,03 → 0,034 (n=500) et 0,09 → 0,11 (n=1500) jusqu'à t=3, ζ ≈ 2/3 stable.

## 5. T0 n'est pas une fuite : le dipôle seul se met en 3D, de façon cohérente
ζ moyenné par cellules (la moyenne efface le bruit de particules, garde les structures) :
| run (n=500) | t | ζ particules | ζ cellules 1,0 | ζ cellules 2,0 |
|---|---|---|---|---|
| 1 dipôle + poussière | 2,0 | 0,208 | 0,113 | 0,025 |
| 1 dipôle + poussière | 3,0 | 0,202 | 0,130 | **0,124** |
| 2 dipôles sans poussière | 3,0 | 0,0002 | 0,0001 | 0,0000 |
→ La 3D de T0 survit à la moyenne à l'échelle de la demi-boîte : c'est une **structure cohérente**, née d'une poussière
qui, seule, ne bouge pas. Le dipôle amplifie la poussière d'environ ×1000 en enstrophie hors du plan.
C'est compatible avec les instabilités 3D connues d'une paire de tourbillons (Crow 1970 ; instabilité elliptique,
Leweke & Williamson 1998) — **hypothèse, mécanisme non identifié ici** (pas de longueur d'onde mesurée, Mach 0,18, cœurs sous-résolus).

## Conséquences
- Le « STOP, la salle fuit » de T0 lisait mal le témoin : le bois n'est pas banal, un dipôle seul s'allume déjà.
- Pour mesurer l'effet de la **collision**, le témoin doit être T0 (1 dipôle + même poussière) : effet = 2 dipôles − 1 dipôle (R8 appliqué à la poussière).
- Avant toute amplification annoncée : vérifier la cohérence par moyenne en cellules (critère anti-bruit) et la convergence en n.
