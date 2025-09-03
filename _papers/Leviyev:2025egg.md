---
title: "Efficient Bayesian Sampling with Langevin Birth-Death Dynamics"
authors:
  - "Leviyev, Alex"
  - "Iacovelli, Francesco"
  - "Zimmerman, Aaron"
jref:
doi:
date: 2025-09-02
arxiv: "2509.01942"
insp_recid: 2965908
used_spec:
used_spectre:
abstract: |
  Bayesian inference plays a central role in scientific and
  engineering applications by enabling principled reasoning under
  uncertainty. However, sampling from generic probability
  distributions remains a computationally demanding task. This
  difficulty is compounded when the distributions are ill-conditioned,
  multi-modal, or supported on topologically non-Euclidean spaces.
  Motivated by challenges in gravitational wave parameter estimation,
  we propose simulating a Langevin diffusion augmented with a birth-
  death process. The dynamics are rescaled with a simple
  preconditioner, and generalized to apply to the product spaces of a
  hypercube and hypertorus. Our method is first-order and
  embarrassingly parallel with respect to model evaluations, making it
  well-suited for algorithmic differentiation and modern hardware
  accelerators. We validate the algorithm on a suite of toy problems
  and successfully apply it to recover the parameters of GW150914 --
  the first observed binary black hole merger. This approach addresses
  key limitations of traditional sampling methods, and introduces a
  template that can be used to design robust samplers in the future.
---
