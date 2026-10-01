# MISSION 3D — rapport (campagne 2, 11 runs, 🧮 calcul pur)
Critères figés avant le run 1 : `CRITERES-SCELLES.md` (sha256 c93e4b9c…). Runs + empreintes : `MANIFESTE-RUNS.json`. Rejouer : `python3 analyse.py`.

## Verdict à la lettre des critères : 🅱
Étreinte gagnante = E3 (deux courants). 🅰 échoue : ζ(1500)=0,9981 < ζ(500)=0,9989 (de justesse) ; pas de date convergente (événement absent à n=1000, t=1,086 à n=1500).

## Défauts d'instruments (constatés, pas cachés)
1. **ζ contaminé par construction pour E2/E3** : E3 impose ω_y = ∂u_x/∂z (ζ≈1 dès le départ, même sans poussière) ; E2 incline l'axe du swirl. ζ mesure le meuble, pas l'émergence.
2. **M3 patineuse non discriminante** : positive dans le contrôle plat et dans E3 sans poussière.
3. **M2 réseau non discriminant** : boucles réciproques dans tous les runs, maximum (278) dans E3 sans poussière.

## Seul signal propre (mesure ajoutée après coup, HORS verdict)
Part de vorticité hors de celle imposée par E3 (ωx²+ωz²)/ω² : **0,0011 (n=500) → 0,0014 (1000) → 0,0019 (1500)** ; **0,0000 sans poussière** ; graines 7/8 : 0,0011/0,0010.
→ un petit canal 3D qui naît de la poussière et ne fond pas au raffinement (il croît). Il reste < 0,2 % : vivant mais faible.

## T3 (pic post-coupure)
n=1000 : coupure sèche ×3,58 à t=1,146 ; coupure en rampe ×3,15 à t=1,146 — même date. **Le pic n'est pas le geste** de coupure. Il reste à expliquer (structure temporelle de la pompe ? effet SPH à n=1000 ?). n=500 : pas de pic en coupure sèche.

## Déviation R5
Campagne v0 (`v0-deviation/`) lancée avant réception du brief, étreintes non conformes : exclue du verdict.

## Annotation (append-only, 01/10/2026)
**Statut du 🅱 : NON TRANCHÉ — instruments invalidés après coup** (ζ contaminé par le meuble, M2/M3 positifs dans les témoins négatifs).
L'« instrument du reste » (0,11 → 0,14 → 0,19 %, 0,00 % sans poussière) devient la règle **R8** du labo
(module `ratiss.residual`, RATISS-Framework) et entre dans le prochain brief comme **hypothèse scellable**, pas comme résultat.
