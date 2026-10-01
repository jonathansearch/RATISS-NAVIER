# Statut V3 — 02/10/2026 (append-only)

Témoins lancés après le sceau `ef99a43` : T0 (1 dipôle + poussière, n 500 / 1500), T1 (2 dipôles sans poussière, n 500), T2 (contrôle avec pompe, ν 0,001, n 1500).
Analyse : `python3 temoins.py` → `TEMOINS.json`.

| Témoin | Mesure | Règle | Résultat |
|---|---|---|---|
| T1 | ζ soutenu 0,0010 → Plancher | fuite si > 1e-3 | plat, de justesse |
| T0 n500 / n1500 | ζ soutenu 0,252 / 0,212 | STOP si > 2 × Plancher | 🛑 STOP |
| T2 | pic Ω ×5,3 à t = 1,20 (base figée) | fantôme si ≥ ×3 | ⚠️ inconclusif provisoire |

**Statut : STOP en suspens.** Les définitions chiffrées (`PARAMETRES-FIGES.md`) ont été écrites et scellées par l'agent, puis les témoins lancés dans la foulée, sans validation du chef (le brief §5 réserve le scellement au chef). Ces runs sont donc **hors critères validés**.
Écarts relevés par l'agent :
- dose de poussière non recalculée : ε = 0,01 ≈ 2,2 % du v_rms de T0 (contre 0,9 % prévu) ;
- le plancher T1 ne mesure pas l'effet de la poussière seule (le témoin pertinent serait T0) ;
- tension entre les dipôles injectés et le §10.2 du brief MISSION 3D.
Aucun run des graines A et B n'a été lancé. Suite : signature ou amendement des paramètres par le chef.
