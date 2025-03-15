---
title: "Probing the ringdown perturbation in binary black hole coalescences with an improved quasi-normal mode extraction algorithm"
authors:
  - "Mitman, Keefe"
  - "Pretto, Isabella"
  - "Siegel, Harrison"
  - "Scheel, Mark A."
  - "Teukolsky, Saul A."
  - "Boyle, Michael"
  - "Deppe, Nils"
  - "Kidder, Lawrence E."
  - "Moxon, Jordan"
  - "Nelli, Kyle C."
  - "Throwe, William"
  - "Vu, Nils L."
jref:
doi:
date: 2025-03-12
arxiv: "2503.09678"
abstract: |
  Using gravitational waves to probe the geometry of the ringing
  remnant black hole formed in a binary black hole coalescence is a
  well-established way to test Einstein's theory of general
  relativity. However, doing so requires knowledge of when the
  predictions of black hole perturbation theory, i.e., quasi-normal
  modes (QNMs), are a valid description of the emitted gravitational
  wave as well as what the amplitudes of these excitations are. In
  this work, we develop an algorithm to systematically extract QNMs
  from the ringdown of black hole merger simulations. Our algorithm
  improves upon previous ones in three ways: it fits over the two-
  sphere, enabling a complete model of the strain; it performs a
  reverse-search in time for QNMs using a more robust nonlinear least
  squares routine called \texttt{VarPro}; and it checks the variance
  of QNM amplitudes, which we refer to as ``stability'', over an
  interval matching the natural time scale of each QNM. Using this
  algorithm, we not only demonstrate the stability of a multitude of
  QNMs and their overtones across the parameter space of quasi-
  circular, non-precessing binary black holes, but we also identify
  new quadratic QNMs that may be detectable in the near future using
  ground-based interferometers. Furthermore, we provide evidence which
  suggests that the source of remnant black hole perturbations is
  roughly independent of the overtone index in a given angular
  harmonic across binary parameter space, at least for overtones with
  $n\leq2$. This finding may hint at the spatiotemporal structure of
  ringdown perturbations in black hole coalescences, as well as the
  regime of validity of perturbation theory in the ringdown of these
  events. Our algorithm is made publicly available at the following
  GitHub repository: https://github.com/keefemitman/qnmfinder.
---
