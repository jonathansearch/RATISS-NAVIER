# BRIEF V3 — « La ville trouve sa date seule » (rév. 3 — instrument du reste + discipline de mesure)

Labo : RATISS Labs — opérateur : agent de Jonathan — préfixe : 🛰️
Statut : critères à sceller (SHA-256) AVANT le premier run. Règle R5 inchangée.
Suite de : V2 « Fais voir, ne fabrique pas » (verdict 🅱 — canal vivant, plafonné).

---

## 0. Pourquoi cette campagne (une ligne)

V2 a montré que le canal 3D existe mais ne s'emballe pas. Mais V2 avait un défaut de design
que toi-même as vu : **toutes les horloges étaient réglées par la pompe**. Le pic tombait
toujours vers t ≈ 0,8–1,0, à la coupure. Même les 12 % de E3 mesuraient la date de la pompe,
pas celle de la ville.
V3 enlève la pompe. La ville doit choisir sa date toute seule.

## 1. La règle d'or — on plante le bois, jamais le feu

- **Le bois** : deux structures ordinaires qui se propulsent toutes seules et se percutent
  tête-bêche. Dans une ville plate, un anneau s'appelle un **dipôle** : deux tourbillons de
  signes opposés côte à côte qui avancent sans que personne ne pousse. C'est de la matière
  banale, pas une révolution plantée. À t=0, toute la vorticité est dans le plan. Si de la
  3D apparaît, c'est la ville qui l'a faite.
- **Le feu** : l'auto-amplification 3D. Interdite de la planter. **Une seule allumette
  autorisée : la poussière** (bruit non structuré). En symétrie parfaite, deux dipôles qui
  se percutent s'échangent leurs partenaires proprement et restent plats — la physique le
  dit. Seul le bruit du monde peut casser la symétrie et réveiller l'étreinte.
- **Le témoin qui prouve qu'on n'a pas planté le feu** : le run sans poussière. S'il
  s'allume tout seul, c'est le code qui fabrique du 3D → on ne conclut rien.

## 2. La police et les compteurs (le piège de V3)

- Police plus faible que V2 (ν ÷ 10, comme le test du commissaire). Les zones de contact
  deviennent fines ; c'est là que la 3D peut naître — mais aussi là que le code triche s'il
  n'a pas assez de compteurs.
- **Rampe agressive** : 500 / 1 500 / 4 500. Le pic fantôme ×3,9 de V2 (présent à 1 000
  seulement) est un avertissement : à faible police, si les compteurs sont trop peu
  nombreux, on mesure le code, pas la ville.
- **Clause d'inconclusif** : si le témoin T2 montre un pic fantôme à la nouvelle police,
  la campagne est **inconclusive à cette résolution** — on monte en compteurs d'abord, on
  ne rend AUCUN verdict. Jamais laisser un artefact choisir entre 🅰 et 🅾.

## 3. Les témoins d'abord (règle STOP)

| Témoin | Montage | Attente | STOP / alarme si |
|---|---|---|---|
| T0 | UN dipôle seul + poussière, 500 et 1 500 | file tout droit, fond doucement, ζ au plancher | ζ soutenu > 2 × Plancher → la salle fuit, tout arrêter |
| T1 | Deux dipôles parfaits, ZÉRO poussière, 500 | échange de partenaires propre, ζ au plancher | ζ soutenu > 2 × Plancher → le code fabrique du 3D seul → inconclusif |
| T2 | Contrôle V2 (avec pompe) à la nouvelle police, 1 500 | pas de pic fantôme | pic ×3 ou plus qui n'existe qu'à une résolution → artefact confirmé → inconclusif, monter en compteurs |

T1 sert aussi à **mesurer le Plancher** : le bruit propre de l'instrument sans poussière.
C'est lui qui règle les seuils (voir §4). Et il doit **confirmer que le script reste plat**
(ζ_T1 ≈ 0) — c'est la condition de validité de l'instrument du reste (§9).

## 4. Critères scellés — formules figées, le chiffre se remplit tout seul

**Plancher** := ζ soutenu mesuré sur T1 (le même ζ que V2 : part de l'enstrophie hors du
plan, même définition, même code).

**Toutes les mesures ci-dessous se prennent sur « le reste » (voir §9)** : ce qui déborde
du script. Dans ce montage, le script n'impose rien hors du plan — la mesure directe EST le
reste, tant que T1 confirme sa platitude. Si T1 fuit, mesure corrigée := ζ du run −
Plancher, et les verdicts se prennent sur la mesure corrigée.

- **C1 — le canal s'allume** : après le contact, ζ soutenu > 2 × Plancher, aux deux plus
  hautes résolutions.
- **C2 — c'est résolu** : en passant de 1 500 à 4 500, ζ ne fond pas (reste au-dessus de
  2 × Plancher, même ligue, pas de chute d'un facteur 2).
- **C3 — la ville se concentre seule** : il existe une fenêtre où la **quantité absolue**
  hors du plan (Z₃D = ζ × enstrophie totale) est multipliée par 3 au moins, pendant que
  l'énergie totale **ne monte pas** (elle doit plutôt baisser doucement — personne ne la
  nourrit).
  ⚠️ Pas la part, la quantité. Une part qui monte alors que tout meurt n'est pas une
  concentration, c'est un décompte qui divise par un dénominateur qui fond. C'est la vraie
  patineuse : elle rapproche les bras (l'énergie ne monte pas) et tourne plus vite (la 3D
  se concentre). La version pas-à-pas de V2 est morte (42 % de faux positifs dans le
  contrôle) — celle-ci se juge sur des quantités intégrées, pas sur du bruit pas à pas.
- **C4 — la date est à elle** : à graine fixée, la date du pic bouge de 15 % au plus entre
  1 500 et 4 500. **Entre deux graines différentes, la date a le droit de bouger** — c'est
  le bruit du monde qui règle l'heure du réveil, c'est prévu, pas un défaut. Ce qu'on
  exige : la *forme* de l'événement (montée, pic, retombée) doit être la même d'une graine
  à l'autre. **Toute date utilisée pour C4 vient d'un échantillonnage à chaque pas (§6) —
  une date aliasée ne juge pas C4.**
- **Verdicts** : 🅰 = C1+C2+C3+C4 · 🅱 = C1+C2 sans C3 · 🅾 = jamais C1. Et un 4e état
  possible : **inconclusif** (clause §2) — il se publie comme les autres.

**Ce que 🅰 ne serait pas** : même un 🅰 ici, c'est une auto-amplification d'écho à petite
échelle, sans pompe, dans un SPH — pas le problème du Clay résolu. Ce que ça changerait :
le vieux 72 122 passe de « record poussé » à « à réexaminer sans pompe ». Ni plus, ni
moins. Les trois verdicts sont publiables, comme en V2.

## 5. La campagne — 10 runs (~30 min, les 4 500 sont les plus chers)

| Campagne | Montage | Compteurs | Runs |
|---|---|---|---|
| T0 | 1 dipôle + poussière | 500, 1 500 | 2 |
| T1 | 2 dipôles parfaits, sans poussière | 500 | 1 |
| T2 | contrôle V2 avec pompe, nouvelle police | 1 500 | 1 |
| Graine A | 2 dipôles + poussière (graine 1) | 500 / 1 500 / 4 500 | 3 |
| Graine B | 2 dipôles + poussière (graine 2) | 500 / 1 500 / 4 500 | 3 |

Ordre impératif : sceller ce brief (SHA) → T0, T1, T2 → STOP ou go → graines A et B.

## 6. Mesures par run (même discipline JSON que V2) — rév. 3 : la discipline de mesure

- Graine, compteurs, police, ζ série temporelle, Ω, énergie totale, Z₃D absolu, date du pic.
- **Échantillonnage à chaque pas obligatoire pour toute date.** Leçon T3 : sur une grille
  de sortie à 0,06, le vrai pic était ENTRE deux points — la grille l'aliasait à t=1,146
  au lieu de 1,176. La grille de sortie fait partie de l'instrument. Une date mesurée sur
  grille échantillonnée est marquée « aliasée » et **inutilisable pour C4**.
- **Configuration explicite obligatoire dans chaque JSON** : graine, poussière on/off, n,
  ν, geste de coupure — écrits, jamais hérités des défauts du code. Leçon T3 :
  `Flow(seed=7)` avec poussière par défaut n'était « dust-0 » que par déduction. Un défaut
  du code ne compte pas comme preuve. (Les 4 runs T3 de la campagne précédente : les
  annoter « configuration implicite » plutôt que les relancer — leurs conclusions,
  non-convergence et indépendance au geste de coupure, tiennent dans les quatre
  configurations identiques entre elles.)
- **Ligne de base figée** : si un facteur d'amplification est rapporté, la fenêtre de base
  et sa formule sont celles-ci, identiques pour tous les runs. Leçon T3 : ×3,58 et ×1,7
  décrivaient le même événement avec des bases différentes — deux chiffres incomparables,
  un rapport qui change de base change de langue.
- Continuer d'enregistrer la séparation haut/bas de la ville (gratuit). Pas d'analyse
  maintenant — si 🅰 un jour, le réseau d'influence par secteurs (tranches d'orange)
  devient la campagne V4.
- Chaque JSON doit permettre à n'importe qui de rejouer le run en une commande (R4).

## 7. Avant le premier run — l'ordre des opérations

1. **Pousser V2 d'abord** : `etreintes-navier/` complet (furniture.py, etreintes.py, les
   14 JSON), les critères figés de V2, le verdict 🅱, et les deux notes honnêtes : pic
   ×3,9 à 1 000 seulement (suspect code) ; signature patineuse écartée (le contrôle la
   montre 42 % du temps). R4 : n'importe qui doit pouvoir rejouer 🅱 en une commande.
   Le SHA des critères figés n'a de valeur que s'il est public avant la suite.
   → **FAIT** (082e5b2, 531dc5f). 
2. **Sceller ce brief** : SHA-256, committé avant tout run.
3. Seulement ensuite : témoins → campagne.

## 8. Le piège à ne pas retomber

En V1, on voulait planter deux anneaux tout faits — le chef a bloqué : « on ne le fabrique
pas, on le force à se faire voir. » V3 respecte la règle au millimètre : le bois est banal
(dipôles plats à t=0, vorticité 100 % dans le plan), l'allumette est unique (poussière), et
le témoin sans poussière prouve que le feu n'était pas planté. Si la ville s'allume, elle
se sera allumée seule. Si elle ne s'allume pas, la ville plate gagne un titre de plus :
**le canal 3D ne vit que sous étreinte externe** — et ce titre vaut de l'or pour le labo.

## 9. L'instrument du reste (rév. 2 — leçon de commissaire-navier-3d)

La campagne précédente a tué ses propres instruments, et c'est sa plus grande découverte :
- **ζ mesurait le meuble, pas l'écho.** Dans E3 (nappes de courant opposées), ζ valait 1,0
  SANS poussière : le meuble imposait lui-même la vorticité horizontale. E2 inclinait
  l'axe de la pompe. Aucun de ces ζ ne disait rien de la ville.
- Dans la campagne d'avant (etreintes-navier), E3 laissait les courants dans le plan et ζ
  valait ≈ 0,10. Même nom de meuble, autre implémentation, autre contamination. **Seule
  une mesure qui ignore le meuble est stable d'une implémentation à l'autre.**
- M3 (patineuse pas à pas) positive même dans le contrôle plat. M2 trouvait des boucles
  d'écho là où il ne devait rien y avoir (record 278 en E3 sans poussière).
- La règle qui en sort, désormais règle de labo (**R8**) : **on ne mesure que ce qui
  déborde du script.**

Dans le montage dipôles, la leçon est satisfaite par construction :
- Le script (T1, deux dipôles parfaits) n'impose RIEN hors du plan. T1 doit le confirmer :
  ζ_T1 ≈ 0.
- Donc, dans les runs poussiéreux, **toute la vorticité hors du plan est du reste** : ce
  que la ville a fait seule à partir de la poussière. Aucune soustraction de meuble
  nécessaire.
- Si T1 fuit (le code casse la symétrie tout seul), mesure corrigée := ζ du run −
  Plancher, et les verdicts se prennent sur la mesure corrigée.
- M2 et M3 restent morts. C3 se juge sur la quantité absolue hors du plan du reste,
  intégrée, jamais sur du pas-à-pas.

### Sonde optionnelle : « le plafond est-il le tarif de la police ? » (+2 runs)

Graine A seule, 500 compteurs : un run à la police de V2, un à ν÷10. On compare le
**niveau du reste à plateau**. S'il monte quand la police faiblit, le plafond est un vrai
amortissement visqueux (propriété de la ville). S'il ne bouge pas, le plafond vient
d'ailleurs (résolution, schéma). Le niveau du reste étant indépendant de la graine (0,11 %
graine 7, 0,10 % graine 8 dans la campagne précédente), 2 runs suffisent pour un premier
verdict d'orientation — pas une preuve.
