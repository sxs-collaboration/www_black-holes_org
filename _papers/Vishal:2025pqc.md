---
title: "Superconvergent discontinuous Galerkin method for the scalar Teukolsky equation on hyperboloidal domains: Efficient waveform and self-force computation"
authors:
  - "Vishal, Manas"
  - "Field, Scott E."
  - "Gottlieb, Sigal"
  - "Ryan, Jennifer"
jref: "Gen.Rel.Grav. 57, 104 (2025)"
doi: "10.1007/s10714-025-03435-9"
date: 2025-03-14
arxiv: "2503.11523"
insp_recid: 2900517
used_spec:
used_spectre:
abstract: |
  The long-time evolution of extreme mass-ratio inspiral systems
  requires minimal phase and dispersion errors to accurately compute
  far-field waveforms, while high accuracy is essential near the
  smaller black hole (modeled as a Dirac delta distribution) for self-
  force computations. Spectrally accurate methods, such as nodal
  discontinuous Galerkin (DG) methods, are well suited for these
  tasks. Their numerical errors typically decrease as $\propto (\Delta
  x)^{N+1}$, where $\Delta x$ is the subdomain size and $N$ is the
  polynomial degree of the approximation. However, certain DG schemes
  exhibit superconvergence, where truncation, phase, and dispersion
  errors can decrease as fast as $\propto (\Delta x)^{2N+1}$.
  Superconvergent numerical solvers are, by construction, extremely
  efficient and accurate. We theoretically demonstrate that our DG
  scheme for the scalar Teukolsky equation with a distributional
  source is superconvergent, and this property is retained when
  combined with the hyperboloidal layer compactification technique.
  This ensures that waveforms, total energy and angular-momentum
  fluxes, and self-force computations benefit from superconvergence.
  We empirically verify this behavior across a family of hyperboloidal
  layer compactifications with varying degrees of smoothness.
  Additionally, we show that dissipative self-force quantities for
  circular orbits, computed at the point particle’s location, also
  exhibit a certain degree of superconvergence. Our results underscore
  the potential benefits of numerical superconvergence for efficient
  and accurate gravitational waveform simulations based on DG methods.
---
