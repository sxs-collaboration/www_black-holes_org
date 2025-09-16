---
title: "Toward exponentially-convergent simulations of extreme-mass-ratio inspirals: A time-domain solver for the scalar Teukolsky equation with singular source terms"
authors:
  - "Vishal, Manas"
  - "Field, Scott E."
  - "Rink, Katie"
  - "Gottlieb, Sigal"
  - "Khanna, Gaurav"
jref: "Phys.Rev.D 110, 104009 (2024)"
doi: "10.1103/PhysRevD.110.104009"
date: 2023-07-03
arxiv: "2307.01349"
insp_recid: 2674406
used_spec:
used_spectre:
abstract: |
  Gravitational wave signals from extreme mass ratio inspirals are a
  key target for upcoming, space-based gravitational wave detectors.
  These systems are typically modeled as a distributionally forced
  Teukolsky equation, where the smaller black hole is treated as a
  Dirac delta distribution (i.e., a point-particle). Time-domain
  solvers often use regularization approaches that approximate the
  Dirac distribution. Unfortunately, such approaches often introduce
  small length scales (e.g., when the approximation is by a narrow
  Gaussian) and are a source of systematic error, especially near the
  smaller black hole. We describe a multidomain discontinuous Galerkin
  (DG) method for solving the distributionally forced <math
  display="inline"><mi>s</mi><mo>=</mo><mn>0</mn></math> Teukolsky
  equation that describes scalar fields evolving on a Kerr spacetime.
  To handle the Dirac delta, we expand the solution in spherical
  harmonics and recast the sourced Teukolsky equation as a first-
  order, one-dimensional symmetric hyperbolic system. This allows us
  to derive the method’s numerical flux to correctly account for the
  Dirac delta. As a result, our method achieves global spectral
  accuracy even at the source’s location. To connect the near field to
  future null infinity, we use the hyperboloidal layer method,
  allowing us to supply trivial outer boundary conditions and
  providing direct access to the far-field waveform. We document
  several numerical experiments where we test our method, including
  convergence tests against exact solutions, energy luminosities for
  circular orbits, the scheme’s superconvergence properties at future
  null infinity, and the late-time tail behavior of the scalar field.
  We also compare two systems that arise from different choices of the
  first-order reduction variables, finding that certain reasonable
  choices are numerically problematic in practice. The methods
  developed here may be beneficial when computing gravitational self-
  force effects, where the regularization procedure has been developed
  for the spherical harmonic modes and high accuracy is needed at the
  location of the Dirac delta.
---
