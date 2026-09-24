# Ticket NAVIER_BLOWUP_V02 — TESTÉ ✅ (2026-09-24)

Question : la saturation Ω (v0.1) est-elle physique ou numérique ?
Protocole : ν/10 + résolution ×2 + forçage boosté + contrôle résolution.
Critère : Ω_max(ν/10) > 2×Ω_max(ν) → blowup réel.

Résultat : A=11259 (>7658 ✅), B=19894 (×5.2 🔥), C=9192 (contrôle).
Réponse : **NUMÉRIQUE** (la résolution seule fait ×2.4). Le blowup (au sens
croissance non-saturante) est RÉEL dans notre système ; pas de 1/(T*-t)
prouvé (R=-0.34). Sonde C : 0.38 (vs 0.52 v0.1, vs 0.2 hypothèse : partiel).
Ouvert : pic B 19894→13166 (éclatement/reconnexion ?), ν/100, n=6000.
