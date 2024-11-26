---
title: "A scalable elliptic solver with task-based parallelism for the SpECTRE numerical relativity code"
authors:
  - "Vu, Nils L."
  - "Pfeiffer, Harald P."
  - "Bonilla, Gabriel S."
  - "Deppe, Nils"
  - "Hébert, François"
  - "Kidder, Lawrence E."
  - "Lovelace, Geoffrey"
  - "Moxon, Jordan"
  - "Scheel, Mark A."
  - "Teukolsky, Saul A."
  - "Throwe, William"
  - "Wittek, Nikolas A."
  - "Wlodarczyk, Tom"
jref: "Phys.Rev.D 105, 084027 (2022)"
doi: "10.1103/PhysRevD.105.084027"
date: 2021-11-12
arxiv: "2111.06767"
abstract: |
  Elliptic partial differential equations must be solved numerically
  for many problems in numerical relativity, such as initial data for
  every simulation of merging black holes and neutron stars. Existing
  elliptic solvers can take multiple days to solve these problems at
  high resolution and when matter is involved, because they are either
  hard to parallelize or require a large amount of computational
  resources. Here we present a new solver for linear and nonlinear
  elliptic problems that is designed to scale with resolution and to
  parallelize on computing clusters. To achieve this we employ a
  discontinuous Galerkin discretization, an iterative multigrid-
  Schwarz preconditioned Newton-Krylov algorithm, and a task-based
  parallelism paradigm. To accelerate convergence of the elliptic
  solver we have developed novel subdomain-preconditioning techniques.
  We find that our multigrid-Schwarz preconditioned elliptic solves
  achieve iteration counts that are independent of resolution, and our
  task-based parallel programs scale over 200 million degrees of
  freedom to at least a few thousand cores. Our new code solves a
  classic initial data problem for binary black holes faster than the
  spectral code SpEC when distributed to only eight cores, and in a
  fraction of the time on more cores. It is publicly accessible in the
  next-generation SpECTRE numerical relativity code. Our results pave
  the way for highly parallel elliptic solves in numerical relativity
  and beyond.
---
