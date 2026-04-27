---
title: "Data-Driven Acceleration of Eccentricity Reduction for Binary Black Hole Simulations"
authors:
  - "Tommasini, Vittoria"
  - "Vu, Nils L."
  - "Scheel, Mark A."
  - "Teukolsky, Saul A."
jref:
doi:
date: 2026-04-23
arxiv: "2604.22021"
insp_recid: 3149001
used_spec: true
used_spectre:
abstract: |
  Reducing orbital eccentricity in numerical relativity simulations of
  binary black holes is essential for producing astrophysically
  relevant gravitational wave models, as many of these systems are
  expected to be near-circular in nature. Standard eccentricity
  reduction procedures rely on iterative schemes, often requiring four
  or more trial simulations to achieve desired thresholds. This
  approach is computationally expensive because each trial simulation
  adds ~10% to the total simulation run time of multiple weeks to
  months. We introduce a data-driven approach that accelerates this
  process by learning the values of the initial orbital frequency,
  \(\Omega_0\), and radial velocity, \(\dot{a}_0\), that yield an evolution with
  small eccentricity. This is done using a Gaussian Process Regression
  model trained on an archive of previously eccentricity-reduced
  numerical relativity simulations. For all configurations tested,
  using the trained model consistently reduces the number of required
  eccentricity reduction iterations to just zero or one, significantly
  lowering computational costs relative to post-Newtonian initial
  guesses. These results demonstrate the power of data-driven methods
  in accelerating expensive numerical relativity simulations.
---
