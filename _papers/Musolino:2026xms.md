---
title: "GRACE: An Open-Source Framework for GPU-Accelerated Numerical Relativity"
authors:
  - "Musolino, Carlo"
  - "Ecker, Christian"
  - "Topolski, Konrad"
  - "Cassing, Marie"
  - "Miler, Keneth"
  - "Ng, Harry Ho-Yin"
  - "Pierre, Khalil"
  - "Most, Elias R."
  - "Rezzolla, Luciano"
jref:
doi:
date: 2026-07-10
arxiv: "2607.09854"
insp_recid: 3179986
used_spec:
used_spectre:
abstract: |
  We present GRACE, a new GPU-accelerated numerical-relativity
  framework designed to run efficiently on heterogeneous high-
  performance computing platforms. Developed from scratch and built
  exclusively on open-source libraries, GRACE employs Kokkos for
  performance portability across CPU and GPU architectures and p4est
  for adaptive mesh refinement. The code evolves the equations of
  ideal GRMHD -- with divergence-free magnetic fields maintained by
  constrained transport -- self-consistently coupled to the Einstein
  equations in the Z4c formulation, on fixed or adaptively refined
  grids. We validate the implementation against a suite of standard
  tests, ranging from magnetized shock tubes and the magnetic rotor in
  flat spacetime, through (magnetized) Bondi accretion onto a
  Schwarzschild black hole and the ringdown of a perturbed spinning
  puncture, to neutron-star oscillation spectra in fixed and dynamical
  spacetimes and the merger of binary black holes. As more demanding
  applications, we evolve two binary neutron-star mergers -- an equal-
  mass, unmagnetized system with an ideal-gas equation of state and an
  unequal-mass, magnetized system with a finite-temperature tabulated
  equation of state -- finding the inspiral dynamics to agree well
  with the FIL code. We also report single-device throughput together
  with strong- and weak-scaling results on multiple GPU and CPU
  architectures. GRACE is publicly released together with GRACEpy, a
  basic post-processing and data-analysis environment.
---
