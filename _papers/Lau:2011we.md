---
title: "Implicit-explicit evolution of single black holes"
authors:
  - "Lau, S. R."
  - "Lovelace, G."
  - "Pfeiffer, H. P."
jref: "Physical Review D 84, 084023 (2011)"
doi: "10.1103/PhysRevD.84.084023"
date: 2011-10-01
arxiv: "1105.3922"
used_spec: true
insp_recid: 900633
abstract: |
  Numerical simulations of binary black holes---an important
  predictive tool for the detection of gravitational waves---are
  computationally expensive, especially for binaries with high mass
  ratios or with rapidly spinning constituent holes. Existing codes
  for evolving binary black holes rely on explicit timestepping
  methods, for which the timestep size is limited by the smallest
  spatial scale through the Courant-Friedrichs-Lewy condition. Binary
  inspiral typically involves spatial scales (the spatial resolution
  required by a small or rapidly spinning hole) which are orders of
  magnitude smaller than the relevant (orbital, precession, and
  radiation-reaction) timescales characterizing the inspiral.
  Therefore, in explicit evolutions of binary black holes, the
  timestep size is typically orders of magnitude smaller than the
  relevant physical timescales. Implicit timestepping methods allow
  for larger timesteps, and they often reduce the total computational
  cost (without significant loss of accuracy) for problems dominated
  by spatial rather than temporal error, such as for binary-black-hole
  inspiral in corotating coordinates. However, fully implicit methods
  can be difficult to implement for nonlinear evolution systems like
  the Einstein equations. Therefore, in this paper we explore
  implicit-explicit (IMEX) methods and use them for the first time to
  evolve black-hole spacetimes. Specifically, as a first step toward
  IMEX evolution of a full binary-black-hole spacetime, we develop an
  IMEX algorithm for the generalized harmonic formulation of the
  Einstein equations and use this algorithm to evolve stationary and
  perturbed single-black-hole spacetimes. Numerical experiments
  explore the stability and computational efficiency of our method.
---
