---
title: "General-relativistic neutron star evolutions with the discontinuous Galerkin method"
authors:
  - "Hébert, François"
  - "Kidder, Lawrence E."
  - "Teukolsky, Saul A."
jref: "Phys.Rev.D 98, 044041 (2018)"
doi: "10.1103/PhysRevD.98.044041"
date: 2018-04-05
arxiv: "1804.02003"
used_spec: true
abstract: |
  Simulations of relativistic hydrodynamics often need both high
  accuracy and robust shock-handling properties. The discontinuous
  Galerkin method combines these features—a high order of convergence
  in regions where the solution is smooth and shock-capturing
  properties for regions where it is not—with geometric flexibility
  and is therefore well suited to solve the partial differential
  equations describing astrophysical scenarios. We present here
  evolutions of a general-relativistic neutron star with the
  discontinuous Galerkin method. In these simulations, we
  simultaneously evolve the spacetime geometry and the matter on the
  same computational grid, which we conform to the spherical geometry
  of the problem. To verify the correctness of our implementation, we
  perform standard convergence and shock tests. We then show results
  for evolving, in three dimensions, a Kerr black hole; a neutron star
  in the Cowling approximation (holding the spacetime metric fixed);
  and, finally, a neutron star where the spacetime and matter are both
  dynamical. The evolutions show long-term stability, good accuracy,
  and an improved rate of convergence versus a comparable-resolution
  finite-volume method.
---
