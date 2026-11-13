---
title: "Machine learning and high accuracy: Neural preconditioners for computational gravity"
authors:
  - "Osburn, Thomas"
  - "Vu, Nils"
jref:
doi:
date: 2026-11-11
arxiv: "2611.16106"
insp_recid: 3227874
used_spec:
used_spectre:
abstract: |
  Machine learning (ML) developments have empowered valuable
  calculations in many areas of theoretical physics. Certain topics
  involving moderate-to-low accuracy requirements have been
  particularly fortunate because many ML techniques, such as neural
  networks, introduce a noise floor that would be difficult to
  penetrate with stricter tolerances. For this reason, topics
  requiring high accuracy can be hesitant to pursue ML. One prominent
  example is gravitational wave modeling, which relies on traditional
  methods that accommodate the high sensitivities of detectors such as
  LISA. However, recent progress in applied mathematics has identified
  hybrid methods where fast-but-noisy ML mechanisms are inserted into
  otherwise traditional numerical schemes to accelerate convergence in
  a way that ultimately meets or exceeds the accuracy of standard
  methods. We develop an optimized hybrid ML method to tackle a class
  of challenging PDEs; specifically, we demonstrate ML implementations
  for gravitational waves from asymmetric-mass black hole binaries and
  elastic waves. These require solving sparse linear algebra systems
  with Helmholtz features that are especially difficult for
  traditional iterative methods. Our new approach is to train a graph
  neural network (GNN) as a significantly faster preconditioner using
  a novel loss function based on the true residual of the iterative
  algorithm. For the most difficult regions of parameter space, our
  neural preconditioner decreases iteration counts by 2-15x compared
  to traditional preconditioners. Because the GNN operates directly on
  the sparse matrix and needs only modest physical context, it
  generalizes beyond its training domain and can be adapted to new
  problems across physics by retraining rather than redesign. Hybrid
  ML methods such as this offer a new and compelling avenue to handle
  high accuracy and speed requirements in gravitational wave modeling
  and beyond.
---
