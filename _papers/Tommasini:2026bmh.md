---
title: "Data-driven acceleration of eccentricity reduction for binary black hole simulations"
authors:
  - "Tommasini, Vittoria"
  - "Vu, Nils L."
  - "Scheel, Mark A."
  - "Teukolsky, Saul A."
jref: "Phys.Rev.D 114, 044071 (2026)"
doi: "10.1103/1q92-j84n"
date: 2026-04-23
arxiv: "2604.22021"
insp_recid: 3149001
used_spec: true
used_spectre:
abstract: |
  Reducing orbital eccentricity in numerical relativity simulations of
  binary black holes is essential for producing astrophysically
  relevant gravitational wave models, as many of these systems are
  expected to be near circular in nature. Standard eccentricity-
  reduction procedures rely on iterative schemes, often requiring four
  or more trial simulations to achieve desired thresholds. This
  approach is computationally expensive because each trial simulation
  adds <math display="inline"><mo>∼</mo><mn>10</mn><mo>%</mo></math>
  to the total simulation run-time of multiple weeks to months. We
  introduce a data-driven approach that accelerates this process by
  learning the values of the initial orbital frequency, <math
  display="inline"><msub><mi
  mathvariant="normal">Ω</mi><mn>0</mn></msub></math>, and radial
  velocity, <math display="inline"><msub><mover
  accent="true"><mi>a</mi><mo>˙</mo></mover><mn>0</mn></msub></math>,
  that yield an evolution with small eccentricity. This is done using
  a Gaussian process regression model trained on an archive of
  previously eccentricity-reduced numerical relativity simulations.
  For all configurations tested, using the trained model consistently
  reduces the number of required eccentricity-reduction iterations to
  just zero or one, significantly lowering computational costs
  relative to post-Newtonian initial guesses. These results
  demonstrate the power of data-driven methods in accelerating
  expensive numerical relativity simulations.
---
