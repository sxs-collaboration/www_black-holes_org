---
title: "A multidomain spectral method for solving elliptic equations"
authors:
  - "Harald P. Pfeiffer"
  - "Lawrence E. Kidder"
  - "Mark A. Scheel"
  - "Saul A. Teukolsky"
jref: "Comput.Phys.Commun. 152, 253-273 (2003)"
doi: "10.1016/S0010-4655(02)00847-0"
date: 2003-05-15
arxiv: "gr-qc/0202096"
used_spec: true
insp_recid: 583440
abstract: |
  We present a new solver for coupled nonlinear elliptic partial
  differential equations (PDEs). The solver is based on
  pseudo-spectral collocation with domain decomposition and can handle
  one- to three-dimensional problems. It has three distinct
  features. First, the combined problem of solving the PDE, satisfying
  the boundary conditions, and matching between different subdomains
  is cast into one set of equations readily accessible to standard
  linear and nonlinear solvers. Second, touching as well as
  overlapping subdomains are supported; both rectangular blocks with
  Chebyshev basis functions as well as spherical shells with an
  expansion in spherical harmonics are implemented. Third, the code is
  very flexible: The domain decomposition as well as the distribution
  of collocation points in each domain can be chosen at run time, and
  the solver is easily adaptable to new PDEs. The code has been used
  to solve the equations of the initial value problem of general
  relativity and should be useful in many other problems. We compare
  the new method to finite difference codes and find it superior in
  both runtime and accuracy, at least for the smooth problems
  considered here.
---
