---
title: "NRSur7dq4v2: A multi-domain precessing surrogate model with improved accuracy"
authors:
  - "Ravishankar, Abhishek"
  - "Varma, Vijay"
  - "Field, Scott E."
  - "Mitman, Keefe"
  - "Deppe, Nils"
  - "Stein, Leo C."
  - "Boyle, Michael"
  - "Scheel, Mark A."
jref:
doi:
date: 2026-09-07
arxiv: "2609.07873"
insp_recid: 3201133
used_spec:
used_spectre:
abstract: |
  Numerical relativity simulations provide the most accurate waveforms
  for binary black hole coalescences, but are prohibitively expensive
  for direct use in gravitational-wave data analysis. Surrogate models
  overcome this cost, and NRSur7dq4 is commonly used in parameter
  estimation for this reason. However, there is evidence in the
  literature that NRSur7dq4's accuracy could be improved in the
  merger-ringdown portion of the waveform, which is particularly
  important for the analysis of high-mass binary black hole events.
  Motivated by these observations, we construct NRSur7dq4v2, a multi-
  domain extension of NRSur7dq4 in which overlapping temporal
  subdomains allow tighter, independent error control over the
  inspiral and merger-ringdown portions of the waveform before they
  are smoothly combined. To assess the new model's performance in the
  merger-ringdown regime, we infer the mass and spin of the remnant
  black hole from quasi-normal fits to the ringdown portion of the
  surrogate waveform. We find that NRSur7dq4v2 produces significantly
  improved remnant mass and spin estimates, with gains of roughly
  factors of \(3\) to \(10\) over NRSur7dq4. Compared to NRSur7dq4,
  NRSur7dq4v2 also includes modes up to \(\ell=5\), includes more
  accurate modeling of certain subdominant modes, and introduces a
  runtime model-complexity feature that gives users direct control
  over the tradeoff between evaluation cost and accuracy. Finally,
  alongside the model development, we have optimized the gwsurrogate
  package to achieve a fourfold speedup for precessing surrogates. The
  resulting precessing surrogates called through gwsurrogate are now
  slightly faster than their LALSimulation counterparts.
---
