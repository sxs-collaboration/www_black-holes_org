---
title: "SpECTRE: A task-based discontinuous Galerkin code for relativistic astrophysics"
authors:
  - "Kidder, Lawrence E."
  - "Field, Scott E."
  - "Foucart, Francois"
  - "Schnetter, Erik"
  - "Teukolsky, Saul A."
  - "Bohn, Andy"
  - "Deppe, Nils"
  - "Diener, Peter"
  - "Hébert, François"
  - "Lippuner, Jonas"
  - "Miller, Jonah"
  - "Ott, Christian D."
  - "Scheel, Mark A."
  - "Vincent, Trevor"
jref: "J.Comput.Phys. 335, 7061 (2017)"
doi: "10.1016/j.jcp.2016.12.059"
date: 2016-08-31
arxiv: "1609.00098"
insp_recid: 1484813
abstract: |
  We introduce a new relativistic astrophysics code, SpECTRE, that
  combines a discontinuous Galerkin method with a task-based
  parallelism model. SpECTRE's goal is to achieve more accurate
  solutions for challenging relativistic astrophysics problems such as
  core-collapse supernovae and binary neutron star mergers. The
  robustness of the discontinuous Galerkin method allows for the use
  of high-resolution shock capturing methods in regions where
  (relativistic) shocks are found, while exploiting high-order
  accuracy in smooth regions. A task-based parallelism model allows
  efficient use of the largest supercomputers for problems with a
  heterogeneous workload over disparate spatial and temporal scales.
  We argue that the locality and algorithmic structure of
  discontinuous Galerkin methods will exhibit good scalability within
  a task-based parallelism framework. We demonstrate the code on a
  wide variety of challenging benchmark problems in (non)-relativistic
  (magneto)-hydrodynamics. We demonstrate the code's scalability
  including its strong scaling on the NCSA Blue Waters supercomputer
  up to the machine's full capacity of <math altimg="si1.gif"
  display="inline"
  overflow="scroll"><mn>22</mn><mo>,</mo><mn>380</mn></math> nodes
  using <math altimg="si2.gif" display="inline"
  overflow="scroll"><mn>671</mn><mo>,</mo><mn>400</mn></math> threads.
---
