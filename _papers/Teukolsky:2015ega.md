---
title: "Formulation of discontinuous Galerkin methods for relativistic astrophysics"
authors: "Teukolsky, Saul A."
jref: "J.Comput.Phys. 312,  (2016)"
doi: "10.1016/j.jcp.2016.02.031"
date: 2015-10-05
arxiv: "1510.01190"
insp_recid: 1396100
used_spec:
used_spectre:
abstract: |
  The DG algorithm is a powerful method for solving pdes, especially
  for evolution equations in conservation form. Since the algorithm
  involves integration over volume elements, it is not immediately
  obvious that it will generalize easily to arbitrary time-dependent
  curved spacetimes. We show how to formulate the algorithm in such
  spacetimes for applications in relativistic astrophysics. We also
  show how to formulate the algorithm for equations in non-
  conservative form, such as Einstein's field equations themselves. We
  find two computationally distinct formulations in both cases, one of
  which has seldom been used before for flat space in curvilinear
  coordinates but which may be more efficient. We also give a new
  derivation of the ALE algorithm (Arbitrary Lagrangian–Eulerian)
  using 4-vector methods that is much simpler than the usual
  derivation and explains why the method preserves the conservation
  form of the equations. The various formulations are explored with
  some simple numerical experiments that also investigate the effect
  of the metric identities on the results. The results of this paper
  may also be of interest to practitioners of DG working with
  curvilinear elements in flat space.
---
