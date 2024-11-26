---
title: "Parameter control for eccentric, precessing binary black hole simulations with SpEC"
authors:
  - "Knapp, Taylor"
  - "Chatziioannou, Katerina"
  - "Pfeiffer, Harald"
  - "Scheel, Mark A."
  - "Kidder, Lawrence E."
jref:
doi:
date: 2024-10-03
arxiv: "2410.02997"
used_spec: true
abstract: |
  Numerical relativity simulations of merging black holes provide the
  most accurate description of the binary dynamics and the emitted
  gravitational wave signal. However, practical considerations such as
  imperfect initial data and initial parameters mean that achieving
  target parameters, such as the orbital eccentricity or the black
  hole spin directions, at the beginning of the usable part of the
  simulation is challenging. In this paper, we devise a method to
  produce simulations with specific target parameters, namely the
  Keplerian orbital parameters - eccentricity, semi-major axis, mean
  anomaly - and the black hole spin vectors using SpEC. The method is
  an extension of the current process for achieving vanishing
  eccentricity and it is based on a parameter control loop that
  iteratively numerically evolves the system, fits the orbit with
  analytical post-Newtonian equations, and calculates updated input
  parameters. Through SpEC numerical simulations, we demonstrate
  $\lesssim 10^{-3}$ and $O(\rm degree)$ convergence for the orbital
  eccentricity and the spin directions respectively in $\leq7$
  iterations. These tests extend to binaries with mass ratios $q \leq
  3$, eccentricities $e \leq 0.65$, and spin magnitudes $|\chi | \leq
  0.75$. Our method for controlling the orbital and spin parameters of
  numerical simulations can be used to produce targeted simulations in
  sparsely covered regions of the parameter space or study the
  dynamics of relativistic binaries.
---
