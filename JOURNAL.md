# JOURNAL — RATISS-NAVIER 🌊

## v0.1 : Turbulence Quantique et Sonde Bell (2026-09-24)
Réponse au papier OpenAI (blowup fini, énergie bornée) avec NOTRE méthode :
SPH 3D + forçage lisse + sonde quantique (paires de Bell, déphasage ∝ |ω|).

| Run (n=1500, ν=0.01, T=2.5) | vmax | Ω | E | C |
|---|---|---|---|---|
| Force ON | 2.78 | 3829 | 34.8 (bornée ✓) | 0.52 |
| Force OFF (témoin) | 0.0 | 0.0 | 0.0 | 1.0 |

Verdict : pas de blowup fini (Ω sature, R=-0.22 vs 1/(T*-t)) ; E bornée
(comme OpenAI) ; sonde C : 1→0.52 (la cohérence mesure la vorticité).
Debug héroïque : Shepard (repos parfait 0.0), settling, Kq calibré.

## v0.2 : Chasse au blowup RÉEL (2026-09-24)
Ordre du chef : ν/10, résolution ×2, forçage boosté. La saturation v0.1
était-elle physique ou numérique ?

| Run (T=2.5) | Ω_max | C_min | E_fin | vs v0.1 |
|---|---|---|---|---|
| A (ν=0.001, n=3000) | 11259 | 0.465 | 65.5 | ×2.9 ✅ |
| B (ν=0.001, n=3000, BOOST) | **19894** | 0.379 | 130.5 | ×5.2 🔥 |
| C (ν=0.01, n=3000, contrôle) | 9192 | 0.715 | 27.7 | ×2.4 |

Verdict : **la saturation était NUMÉRIQUE** (résolution ×2.4 à elle seule).
Critère chef (Ω>2×3829=7658) : DÉPASSÉ (11259). Fit B : exp raide (0.54),
toujours pas de 1/(T*-t) (R=-0.34) → croissance explosive mais pas de
singularité prouvée. Sonde : 0.52→0.38 (répond, pas encore 0.2).
B pic à 19894 puis 13166 : le vortex éclate (reconnexion ?) — à investiguer.
