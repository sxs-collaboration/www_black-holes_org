---
title: "Numerical Relativity Using a Generalized Harmonic Decomposition"
authors: "Frans Pretorius"
jref: "Class.Quant.Grav. 22, 425-452 (2005)"
doi: "10.1088/0264-9381/22/2/014"
date: 2005-01-21
arxiv: "gr-qc/0407110"
insp_recid: 655389
abstract: |
  A new numerical scheme to solve the Einstein field equations based
  upon the generalized harmonic decomposition of the Ricci tensor is
  introduced. The source functions driving the wave equations that
  define generalized harmonic coordinates are treated as independent
  functions, and encode the coordinate freedom of
  solutions. Techniques are discussed to impose particular gauge
  conditions through a specification of the source functions. A 3D,
  free evolution, finite difference code implementing this system of
  equations with a scalar field matter source is described. The
  second-order-in-space-and-time partial differential equations are
  discretized directly without the use first order auxiliary terms,
  limiting the number of independent functions to fifteen--ten metric
  quantities, four source functions and the scalar field. This also
  limits the number of constraint equations, which can only be
  enforced to within truncation error in a numerical free evolution,
  to four. The coordinate system is compactified to spatial infinity
  in order to impose physically motivated, constraint-preserving outer
  boundary conditions. A variant of the Cartoon method for efficiently
  simulating axisymmetric spacetimes with a Cartesian code is
  described that does not use interpolation, and is easier to
  incorporate into existing adaptive mesh refinement
  packages. Preliminary test simulations of vacuum black hole
  evolution and black hole formation via scalar field collapse are
  described, suggesting that this method may be useful for studying
  many spacetimes of interest.
---
