---
title: "Living on the edge: Testing for compact population features at the edges of parameter space"
authors:
  - "Hussain, Asad"
  - "Isi, Maximiliano"
  - "Zimmerman, Aaron"
jref:
doi:
date: 2025-10-22
arxiv: "2510.20010"
insp_recid: 3072650
used_spec:
used_spectre:
abstract: |
  Many astrophysical population studies involve parameters that exist
  on a bounded domain, such as the dimensionless spins of black holes
  or the eccentricities of planetary orbits, both of which are
  confined to $[0, 1]$. In such scenarios, we often wish to test for
  distributions clustered near a boundary, e.g., vanishing spin or
  orbital eccentricity. Conventional approaches -- whether based on
  Monte Carlo, kernel density estimators, or machine-learning
  techniques -- often suffer biases at the boundaries. These biases
  stem from sparse sampling near the edge, kernel-related smoothing,
  or artifacts introduced by domain transformations. We introduce a
  truncated Gaussian mixture model framework that substantially
  mitigates these issues, enabling accurate inference of narrow, edge-
  dominated population features. While our method has broad
  applications to many astronomical domains, we consider gravitational
  wave catalogs as a concrete example to demonstrate its power. In
  particular, we maintain agreement with published constraints on the
  fraction of zero-spin binary black hole systems in the GWTC-3
  catalog -- results originally derived at much higher computational
  cost through dedicated reanalysis of individual events in the
  catalog. Our method can achieve similarly reliable results with a
  much lower computational cost. The method is publicly available in
  the open-source packages gravpop and truncatedgaussianmixtures.
---
