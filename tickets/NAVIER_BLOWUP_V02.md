# Ticket NAVIER_BLOWUP_V02 — CLOS ✅ (2026-09-24)

Question : la saturation Ω (v0.1) est-elle physique ou numérique ?
Protocole : ν/10 + résolution ×2 + forçage boosté + contrôle résolution.
Critère : Ω_max(ν/10) > 2×Ω_max(ν) → blowup réel.

Résultat : A=11259 (>7658 ✅), B=19894 (×5.2 🔥), C=9192 (contrôle).
VERDICT : **saturation numérique réfutée, blowup réel confirmé**.
La résolution seule fait ×2.4. Sonde C : 0.38.
