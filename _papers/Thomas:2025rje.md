---
title: "Optimizing Neural Network Surrogate Models: Application to Black Hole Merger Remnants"
authors:
  - "Thomas, Lucy M."
  - "Chatziioannou, Katerina"
  - "Varma, Vijay"
  - "Field, Scott E."
jref:
doi:
date: 2025-01-27
arxiv: "2501.16462"
insp_recid: 2873407
abstract: |
  Surrogate models of numerical relativity simulations of merging
  black holes provide the most accurate tools for gravitational-wave
  data analysis. Neural network-based surrogates promise evaluation
  speedups, but their accuracy relies on (often obscure) tuning of
  settings such as the network architecture, hyperparameters, and the
  size of the training dataset. We propose a systematic optimization
  strategy that formalizes setting choices and motivates the amount of
  training data required. We apply this strategy on NRSur7dq4Remnant,
  an existing surrogate model for the properties of the remnant of
  generically precessing binary black hole mergers and construct a
  neural network version, which we label NRSur7dq4Remnant_NN. The
  systematic optimization strategy results in a new surrogate model
  with comparable accuracy, and provides insights into the meaning and
  role of the various network settings and hyperparameters as well as
  the structure of the physical process. Moreover, NRSur7dq4Remnant_NN
  results in evaluation speedups of up to 8 times on a single CPU
  and a further improvement of 2,000 times when evaluated in batches
  on a GPU. To determine the training set size, we propose an
  iterative enrichment strategy that efficiently samples the parameter
  space using much smaller training sets than naive sampling.
  NRSur7dq4Remnant_NN requires \(O(10^4)\) training data, so neural
  network-based surrogates are ideal for speeding-up models that
  support such large training datasets, but at the moment cannot
  directly be applied to numerical relativity catalogs that are
  \(O(10^3)\) in size. The optimization strategy is available through
  the gwbonsai package.
---
