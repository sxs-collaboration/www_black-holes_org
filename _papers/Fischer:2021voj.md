---
title: "Unified discontinuous Galerkin scheme for a large class of elliptic equations"
authors:
  - "Fischer, Nils L."
  - "Pfeiffer, Harald P."
jref: "Phys.Rev.D 105, 024034 (2022)"
doi: "10.1103/PhysRevD.105.024034"
date: 2021-08-12
arxiv: "2108.05826"
insp_recid: 1904097
used_spectre: true
abstract: |
  We present a discontinuous Galerkin internal-penalty scheme that is
  applicable to a large class of linear and nonlinear elliptic partial
  differential equations. The unified scheme can accommodate all
  second-order elliptic equations that can be formulated in first-
  order flux form, encompassing problems in linear elasticity, general
  relativity, and hydrodynamics, including problems formulated on a
  curved manifold. It allows for a wide range of linear and nonlinear
  boundary conditions, and accommodates curved and nonconforming
  meshes. Our generalized internal-penalty numerical flux and our
  Schur-complement strategy of eliminating auxiliary degrees of
  freedom make the scheme compact without requiring equation-specific
  modifications. We demonstrate the accuracy of the scheme for a suite
  of numerical test problems. The scheme is implemented in the open-
  source spectre numerical relativity code.
---
