---
title: "Radiation outer boundary conditions and near-to-far field signal transformations for the Bardeen-Press equation"
authors:
  - "Bishoyi, Som Dev"
  - "Field, Scott E."
  - "Lau, Stephen R."
jref:
doi:
date: 2026-04-24
arxiv: "2604.22734"
insp_recid: 3148999
used_spec:
used_spectre:
abstract: |
  Several theoretical and astrophysical problems - including
  gravitational-wave modeling for extreme mass-ratio inspirals -
  require accurate time-domain solutions of the spin-weight $s=-2$
  Teukolsky equation in Boyer-Lindquist coordinates. Because such
  simulations are performed on finite computational domains, they
  typically introduce an artificial outer boundary where nontrivial
  boundary conditions must be imposed. If these conditions are
  inaccurate, then spurious reflections and slowly-growing unphysical
  modes may corrupt long-time evolutions. We develop and implement
  exact radiation outer boundary conditions for the Bardeen-Press
  equation (a harmonic moment of the $a=0$ Teukolsky equation), making
  the artificial boundary transparent at any finite radius. We also
  construct near-to-far field teleportation kernels that map field
  data recorded at finite radius $r_1$ to the data reaching $r_2 >
  r_1$. The possible choice $r_2 = \infty$ corresponds to asymptotic
  waveform evaluation, that is propagation of the data to future null
  infinity. We show that both boundary and teleportation kernels are
  well approximated by exponential sums, with associated error bounds.
  Implemented in a time-domain solver, our kernel-based boundary
  conditions eliminate unphysical late-time growth and give the
  correct late-time decay rates, affording efficient long-duration
  simulations for waveform modeling and related blackhole perturbation
  calculations.
---
