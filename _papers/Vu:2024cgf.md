---
title: "Discontinuous Galerkin scheme for elliptic equations on extremely stretched grids"
authors: "Vu, Nils L."
jref: "Phys.Rev.D 110, 084062 (2024)"
doi: "10.1103/PhysRevD.110.084062"
date: 2024-05-09
arxiv: "2405.06120"
insp_recid: 2785388
used_spectre: true
abstract: |
  Discontinuous Galerkin (DG) methods for solving elliptic equations
  are gaining popularity in the computational physics community for
  their high-order spectral convergence and their potential for
  parallelization on computing clusters. However, problems in
  numerical relativity with extremely stretched grids, such as initial
  data problems for binary black holes that impose boundary conditions
  at large distances from the black holes, have proven challenging for
  DG methods. To alleviate this problem we have developed a primal DG
  scheme that is generically applicable to a large class of elliptic
  equations, including problems on curved and extremely stretched
  grids. The DG scheme accommodates two widely used initial data
  formulations in numerical relativity, namely the puncture
  formulation and the extended conformal thin-sandwich (XCTS)
  formulation. We find that our DG scheme is able to stretch the grid
  by a factor of <math
  display="inline"><mo>∼</mo><msup><mn>10</mn><mn>9</mn></msup></math>
  and hence allows to impose boundary conditions at large distances.
  The scheme converges exponentially with resolution both for the
  smooth XCTS problem and for the nonsmooth puncture problem. With
  this method we are able to generate high-quality initial data for
  binary black hole problems using a parallelizable DG scheme. The
  code is publicly available in the open-source spectre numerical
  relativity code.
---
