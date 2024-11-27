---
title: "Surrogate models for precessing binary black hole simulations with unequal masses"
authors:
  - "Varma, Vijay"
  - "Field, Scott E."
  - "Scheel, Mark A."
  - "Blackman, Jonathan"
  - "Gerosa, Davide"
  - "Stein, Leo C."
  - "Kidder, Lawrence E."
  - "Pfeiffer, Harald P."
jref: "Phys.Rev.Research. 1, 033015 (2019)"
doi: "10.1103/PhysRevResearch.1.033015"
date: 2019-05-22
arxiv: "1905.09300"
used_spec: true
abstract: |
  Only numerical relativity simulations can capture the full
  complexities of binary black hole mergers. These simulations,
  however, are prohibitively expensive for direct data analysis
  applications such as parameter estimation. We present two new fast
  and accurate surrogate models for the outputs of these simulations:
  the first model, NRSur7dq4, predicts the gravitational waveform and
  the second model, \RemnantModel, predicts the properties of the
  remnant black hole. These models extend previous 7-dimensional, non-
  eccentric precessing models to higher mass ratios, and have been
  trained against 1528 simulations with mass ratios \(q\leq4\) and spin
  magnitudes \(\chi_1,\chi_2 \leq 0.8\), with generic spin directions.
  The waveform model, NRSur7dq4, which begins about 20 orbits before
  merger, includes all \(\ell \leq 4\) spin-weighted spherical harmonic
  modes, as well as the precession frame dynamics and spin evolution
  of the black holes. The final black hole model, \RemnantModel,
  models the mass, spin, and recoil kick velocity of the remnant black
  hole. In their training parameter range, both models are shown to be
  more accurate than existing models by at least an order of
  magnitude, with errors comparable to the estimated errors in the
  numerical relativity simulations. We also show that the surrogate
  models work well even when extrapolated outside their training
  parameter space range, up to mass ratios \(q=6\).
---
