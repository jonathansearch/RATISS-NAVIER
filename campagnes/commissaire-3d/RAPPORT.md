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

## Extensions (02/10/2026, append-only) — E3b + carte de régime (§2 variante de pureté, §6 ligne 11+)
Critères : ceux scellés (c93e4b9c…), inchangés. Échantillonnage du code d'origine (tous les 10 pas) : les dates ci-dessous sont **aliasées**.
E3b = deux courants séparés en y : le meuble n'impose que ω_z → ζ n'est PAS contaminé (contrairement à E3).

| Run | n | poussière | ν | ζ moyen (t≥0,5) | ζ>0,10 soutenu | Ωmax post-coupure |
|---|---|---|---|---|---|---|
| R13 | 500 | 7 | 0,01 | 0,0013 | 0 | 1,146 |
| R15 | 500 | 8 | 0,01 | 0,0012 | 0 | 1,146 |
| R14 | 500 | 0 | 0,01 | 0,0000 | 0 | 1,146 |
| R16 | 1000 | 7 | 0,01 | 0,0017 | 0 | 1,686 |
| R17 | 1500 | 7 | 0,01 | 0,0014 | 0 | 1,086 (1er éch. → pas d'événement) |
| R18 | 500 | 7 | 0,001 | 0,0019 | 0 | 2,466 |

Lecture : la mesure propre (E3b) retrouve le niveau de l'instrument du reste sous E3 (0,11–0,19 %), sans le meuble.
Ça vient seulement de la poussière (0 sans poussière, insensible à la graine), plat en n (ne fond pas, ne monte pas), loin de 0,10.
M3 positive partout, y compris dust-0 (instrument mort, confirmé). Pas de date convergente.
À la lettre : ζ < 0,02 mais ne fond pas → 🅾 refusé, 🅱 (« sinon »). Sonde police (1 run) : ν÷10 → 0,13 → 0,19 % (orientation, pas preuve).
