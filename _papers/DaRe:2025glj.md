---
title: "Modeling the BMS transformation induced by a binary black hole merger"
authors:
  - "Da Re, Guido"
  - "Mitman, Keefe"
  - "Stein, Leo C."
  - "Scheel, Mark A."
  - "Teukolsky, Saul A."
  - "Sun, Dongze"
  - "Boyle, Michael"
  - "Deppe, Nils"
  - "Field, Scott E."
  - "Kidder, Lawrence E."
  - "Moxon, Jordan"
  - "Nelli, Kyle C."
  - "Throwe, William"
  - "Varma, Vijay"
  - "Vu, Nils L."
jref:
doi:
date: 2025-03-12
arxiv: "2503.09569"
used_spec: true
abstract: |
  Understanding the characteristics of the remnant black hole formed
  in a binary black hole merger is crucial for conducting
  gravitational wave astronomy. Typically, models of remnant black
  holes provide information about their mass, spin, and kick velocity.
  However, other information related to the supertranslation
  symmetries of the BMS group, such as the memory effect, is also
  important for characterizing the final state of the system. In this
  work, we build a model of the BMS transformation that maps a binary
  black hole's inspiral frame to the remnant black hole's canonical
  rest frame. Training data for this model are created using high-
  precision numerical relativity simulations of quasi-circular systems
  with mass ratios \(q \le 8\) and spins parallel to the orbital angular
  momentum with magnitudes \(\chi_{1}, \chi_{2} \le 0.8\). We use
  Gaussian Process Regression to model the BMS transformations over
  the three-dimensional parameter space \(\left(q, \chi_{1}^{z},
  \chi_{2}^{z}\right)\). The physics captured by this model is strictly
  non-perturbative and cannot be obtained from post-Newtonian
  approximations alone, as it requires knowledge of the strong
  nonlinear effects that are sourced during the merger. Apart from
  providing the first model of the supertranslation induced by a
  binary black hole merger, we also find that the kick velocities
  predicted using Cauchy-characteristic evolution waveforms are, on
  average, \(\sim 5\%\) larger than the ones obtained from extrapolated
  waveforms. Our work has broad implications for improving
  gravitational wave models and studying the large-scale impact of
  memory, such as on the cosmological background. The fits produced in
  this work are available through the Python package
  <code>surfinBH</code> under the name <code>NRSur3dq8BMSRemnant</code>.
---
