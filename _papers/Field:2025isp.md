---
title: "GWSurrogate: A Python package for gravitational wave surrogate models"
authors:
  - "Field, Scott E."
  - "Varma, Vijay"
  - "Blackman, Jonathan"
  - "Gadre, Bhooshan"
  - "Galley, Chad R."
  - "Islam, Tousif"
  - "Mitman, Keefe"
  - "Pürrer, Michael"
  - "Ravichandran, Adhrit"
  - "Scheel, Mark A."
  - "Stein, Leo C."
  - "Yoo, Jooheon"
jref: "J.Open Source Softw. 10, 7073 (2025)"
doi: "10.21105/joss.07073"
date: 2025-03-29
arxiv: "2504.08839"
insp_recid: 2910075
used_spec: true
used_spectre: true
abstract: |
  Fast and accurate waveform models are fundamentally important to
  modern gravitational wave astrophysics, enabling the study of
  merging compact objects like black holes and neutron stars. However,
  generating high-fidelity gravitational waveforms through numerical
  relativity simulations is computationally intensive, often requiring
  days to months of computation time on supercomputers. Surrogate
  models provide a practical solution to dramatically accelerate
  waveform evaluations (typically tens of milliseconds per evaluation)
  while retaining the accuracy of computationally expensive
  simulations. The GWSurrogate Python package provides easy access to
  these gravitational wave surrogate models through a user-friendly
  interface. Currently, the package supports 16 surrogate models, each
  varying in duration, included physical effects (e.g., nonlinear
  memory, tidal forces, harmonic modes, eccentricity, mass ratio
  range, precession effects), and underlying solution methods (e.g.,
  Effective One Body, numerical relativity, black hole perturbation
  theory). GWSurrogate models follow the waveform model conventions
  used by the LIGO-Virgo-Kagra collaboration, making the package
  immediately suitable for both theoretical studies and practical
  gravitational wave data analysis. By enabling rapid and precise
  waveform generation, GWSurrogate serves as a production-level tool
  for diverse applications, including parameter estimation, template
  bank generation, and tests of general relativity.
---
