# Commissaire NAVIER — campagne 1 (9 runs, 01/10/2026)

Question : d'où vient le blowup ? Chaîne testée : source (pompe) → amplificateur (3D) → compteur (résolution).
Rejouer un run : voir `MANIFESTE-RUNS.json` (une commande par run). Échantillonnage tous les 10 pas (dates aliasables, cf. leçon T3).

| Famille | Runs | Ce qui a été trouvé |
|---|---|---|
| SRC | SRC_off | pompe coupée : Ω = 0 exactement → **la source, c'est la pompe** |
| CPT | n 500 / 1000 / 1500 | part hors du plan r3D ≈ 0,01 et décroissante avec n ; le pic ne converge pas avec n → **le compteur domine** |
| GRN | graine 8 (vs 7) | même pic à t = 1,57 |
| AMP | coupure à t = 1 (ν 0,01 et 0,001) | pic à 1,15 puis retombée — **pas d'amplificateur** (pic post-coupure : tranché ensuite par T3 = artefact numérique, voir commissaire-3d) |
| POL | ν 0,1 / 0,001 | la police règle la durée, pas le pic |

Verdict du commissaire : **pompe + compteur**, pas d'amplificateur 3D. Suite : `campagnes/etreintes-v2`, `campagnes/commissaire-3d`, `campagnes/dipoles-v3`.
