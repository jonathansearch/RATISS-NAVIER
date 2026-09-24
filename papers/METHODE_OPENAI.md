# Méthode OpenAI — "Finite Time Blowup for Navier–Stokes" (08/09/2026, 166p + Lean)

## Résultat
NS 3D incompressible, tout ν>0, force externe LISSE à support compact,
départ au REPOS → vitesse max NON BORNÉE en temps fini (t=1),
énergie cinétique totale BORNÉE (→0 dans le cœur !). Cas C/D de Clay.
Preuve : analytique + Lean (10 000 agents, 88h). Non vérifiée indépendamment (C).

## Mécanisme (τ = 1-t, 0<h<1/100)
- Cœur : largeur radiale ~τ^1/2, longueur axiale ~τ^(1/2-h) → spaghetti.
- Vitesses (azimutale+axiale) ~τ^(-1/2-h) → ∞.
- Volume ~τ^(3/2-h), v² ~τ^(-1-2h) → ÉNERGIE ~τ^(1/2-3h) → 0. ✓ bornée
- Physique : conservation r·vθ (inflow radial → spin-up) + outflow axial
  (pas d'accumulation) + diffusion visqueuse qui reste d'ordre 1 en radial.
- L'astuce : anneau de PULSES oscillatoires short-lived, moyenne angulaire
  NULLE mais flux de quantité de mouvement QUADRATIQUE non nul → la force
  requise reste lisse pendant que le vortex diverge.
- Cycle de correction ×∞ : harmoniques angulaires → amplitudes → opérateur
  oscillation-rapide → 5 équations intégrales (pression+moment). σ_j=1/5+j/10.

## Ce qu'on réplique (comportement, pas la preuve)
Setup SPH 3D : repos + force lisse compacte (inflow radial + swirl + pulses
anneau) → on mesure vmax(t), Ω(t) (BKM), E(t) et on fit l'exposant :
même chose (α≈1/2) ou autre chose ? + sonde quantique inédite (C(t) vs Ω).
