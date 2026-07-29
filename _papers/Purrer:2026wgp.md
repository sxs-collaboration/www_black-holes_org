---
title: "Fast, accurate, and differentiable: a neural-network surrogate for NRSur7dq4 precessing binary black hole waveforms"
authors:
  - "Pürrer, Michael"
  - "Girish, Ashwin"
  - "Thomas, Lucy M."
  - "Field, Scott E."
  - "Varma, Vijay"
jref:
doi:
date: 2026-07-27
arxiv: "2607.24960"
insp_recid: 3183830
used_spec:
used_spectre:
abstract: |
  We present a neural network surrogate model that emulates the
  NRSur7dq4 gravitational waveform model for precessing binary black
  hole mergers. The surrogate decomposes the waveform into constituent
  quantities and trains an independent multilayer perceptron (MLP) for
  each. We validate the surrogate against NRSur7dq4 on 10,000
  waveforms spanning its full parameter space (\(1 \leq q \leq 4\),
  \(|χ_{A,B}| \leq 0.8\)). For representative total masses between 60
  and 300 \(M_\odot\), median sky-averaged frequency-domain mismatches
  range from \(8.0 \times 10^{-5}\) to \(1.7 \times 10^{-4}\), with
  95th percentiles below \(10^{-3}\). On an NVIDIA L40S GPU the JAX
  surrogate evaluates a single waveform in about 1 ms end-to-end,
  roughly 10 times faster than the LALSimulation C implementation of
  NRSur7dq4, and sustains about 140 times the LALSimulation throughput
  at batch size 64, making it well suited for both low-latency
  parameter-estimation samplers and large-scale waveform generation.
  The full NRSur7dq4 NN waveform-to-likelihood pipeline is implemented
  in JAX and is differentiable. This is the first neural-network
  surrogate of a precessing numerical-relativity waveform model to
  combine validated NR-faithful accuracy with a fully differentiable,
  GPU-accelerated inference pipeline, enabling gradient-based
  inference approaches via automatic differentiation including Fisher
  information matrices, GPU-accelerated nested sampling, gradient-
  based MCMC and importance sampling.
---
