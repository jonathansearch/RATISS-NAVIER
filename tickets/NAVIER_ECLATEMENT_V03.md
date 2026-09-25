# Ticket NAVIER_ECLATEMENT_V03 — TESTÉ ✅ (2026-09-25)

Question : capturer la reconnexion du vortex en GIF avec ν/100.
Objectif : Ω>50000, C→0.15-0.20.

Résultat (RUN-D, ν=0.0001, n=3000, BOOST) :
- Ω_max=28696 (×1.44 vs B, < 50000 : objectif partiel).
- C_min=0.296 (vs 0.15-0.20 visés : partiel).
- **Cascade d'éclatements** : 15k → 11k → 19k → 28.7k → 20.6k.
  Pics et creux multiples = reconnexions en cascade, pas un seul event.
- Fit : exp raide (0.66), pas de 1/(T*-t) (R=-0.59).
- GIF : `demos/eclatement.gif` (14 frames).

Verdict : la résolution domine la viscosité dans ce régime SPH
(n6000/ν.001=40k > n3000/ν.0001=28.7k). Prochain : n=6000 + ν/100.
