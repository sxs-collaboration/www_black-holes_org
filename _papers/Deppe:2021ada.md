---
title: "A high-order shock capturing discontinuous Galerkin–finite difference hybrid method for GRMHD"
authors:
  - "Deppe, Nils"
  - "Hébert, François"
  - "Kidder, Lawrence E."
  - "Teukolsky, Saul A."
jref: "Class.Quant.Grav. 39, 195001 (2022)"
doi: "10.1088/1361-6382/ac8864"
date: 2021-09-23
arxiv: "2109.11645"
abstract: |
  We present a discontinuous Galerkin (DG)–finite difference (FD)
  hybrid scheme that allows high-order shock capturing with the DG
  method for general relativistic magnetohydrodynamics. The hybrid
  method is conceptually quite simple. An unlimited DG candidate
  solution is computed for the next time step. If the candidate
  solution is inadmissible, the time step is retaken using robust FD
  methods. Because of its a posteriori nature, the hybrid scheme
  inherits the best properties of both methods. It is high-order with
  exponential convergence in smooth regions, while robustly handling
  discontinuities. We give a detailed description of how we transfer
  the solution between the DG and FD solvers, and the troubled-cell
  indicators necessary to robustly handle slow-moving discontinuities
  and simulate magnetized neutron stars. We demonstrate the efficacy
  of the proposed method using a suite of standard and very
  challenging 1D, 2D, and 3D relativistic magnetohydrodynamics test
  problems. The hybrid scheme is designed from the ground up to
  efficiently simulate astrophysical problems such as the inspiral,
  coalescence, and merger of two neutron stars.
---
