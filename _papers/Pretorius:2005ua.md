---
title: "Adaptive Mesh Refinement for Coupled Elliptic-Hyperbolic Systems"
authors:
  - "Frans Pretorius"
  - "Matthew W. Choptuik"
jref: "J. Comput. Phys. 218, 246-274 (2006)"
doi: "10.1016/j.jcp.2006.02.011"
date: 2006-10-10
arxiv: "gr-qc/0508110"
insp_recid: 690926
abstract: |
  We present a modification to the Berger and Oliger adaptive mesh
  refinement algorithm designed to solve systems of coupled,
  non-linear, hyperbolic and elliptic partial differential
  equations. Such systems typically arise during constrained evolution
  of the field equations of general relativity. The novel aspect of
  this algorithm is a technique of "extrapolation and delayed
  solution" used to deal with the non-local nature of the solution of
  the elliptic equations, driven by dynamical sources, within the
  usual Berger and Oliger time-stepping framework. We show empirical
  results demonstrating the effectiveness of this technique in
  axisymmetric gravitational collapse simulations. We also describe
  several other details of the code, including truncation error
  estimation using a self-shadow hierarchy, and the
  refinement-boundary interpolation operators that are used to help
  suppress spurious high-frequency solution components ("noise").
---
