---
title: "Self-force calculations with numerical relativity methods"
authors:
  - "Vu, Nils L."
  - "Nishimura, Nami"
  - "Osburn, Thomas"
  - "Thompson, Jonathan E."
  - "Kidder, Lawrence E."
  - "Upton, Samuel D."
  - "Wardell, Barry"
jref: "Phys.Rev.D 114, 064077 (2026)"
doi: "10.1103/lbyk-26gh"
date: 2026-06-03
arxiv: "2606.04998"
insp_recid: 3165053
used_spec:
used_spectre:
abstract: |
  To model gravitational waveforms from extreme mass-ratio inspirals
  for the upcoming LISA space mission, gravitational self-force
  calculations are needed to second order in perturbation theory.
  However, to date these calculations have only been attempted for the
  simplest case of circular orbits in Schwarzschild spacetime. In this
  work, we present a new computational method aimed at performing
  generic second-order self-force calculations in Kerr spacetime using
  methods from the adjacent field of numerical relativity. We perform
  an <math display="inline"><mi>m</mi></math>-mode separation of
  variables, add null (“<math
  display="inline"><mi>v</mi><mi>t</mi><mi>u</mi></math>”) slicing in
  horizon-penetrating coordinates, and solve the resulting elliptic
  partial differential equations (PDEs) using high-order discontinuous
  Galerkin discretization, adaptive mesh refinement, and an iterative
  Krylov-type linear solver with parallelizable multigrid-Schwarz
  preconditioning. We find that our method achieves exponential
  convergence for the self-force on a scalar point charge in Kerr
  spacetime up to spins of <math display="inline"><mo
  stretchy="false">|</mo><mi>a</mi><mo
  stretchy="false">|</mo><mo>/</mo><mi>M</mi><mo>=</mo><mn>0.998</mn></math>
  (Thorne limit) on circular equatorial orbits as close as the
  innermost stable circular orbit (ISCO) (prograde and retrograde),
  despite the nonsmooth solution on the grid. We solve for <math
  display="inline"><mrow><mn>20</mn><mtext> </mtext><mi>m</mi></mrow></math>-modes
  in parallel in a few seconds and retain the flexibility to extend
  the method to gravitational self-force and more generic orbits in
  the future. The code to perform these calculations is publicly
  available in the open-source numerical relativity code spectre.
---
