---
title: "Surrogate model of hybridized numerical relativity binary black hole waveforms"
authors:
  - "Varma, Vijay"
  - "Field, Scott E."
  - "Scheel, Mark A."
  - "Blackman, Jonathan"
  - "Kidder, Lawrence E."
  - "Pfeiffer, Harald P."
jref: "Phys.Rev.D 99, 064045 (2019)"
doi: "10.1103/PhysRevD.99.064045"
date: 2018-12-19
arxiv: "1812.07865"
used_spec: true
used_spec: true
abstract: |
  Numerical relativity (NR) simulations provide the most accurate
  binary black hole gravitational waveforms, but are prohibitively
  expensive for applications such as parameter estimation. Surrogate
  models of NR waveforms have been shown to be both fast and accurate.
  However, NR-based surrogate models are limited by the training
  waveforms’ length, which is typically about 20 orbits before merger.
  We remedy this by hybridizing the NR waveforms using both post-
  Newtonian and effective one-body waveforms for the early inspiral.
  We present NRHybSur3dq8, a surrogate model for hybridized
  nonprecessing numerical relativity waveforms, that is valid for the
  entire LIGO band (starting at 20 Hz) for stellar mass binaries with
  total masses as low as 2.25  M⊙. We include the ℓ≤4 and (5, 5) spin-
  weighted spherical harmonic modes but not the (4, 1) or (4, 0)
  modes. This model has been trained against hybridized waveforms
  based on 104 NR waveforms with mass ratios q≤8, and |χ1z|,|χ2z|≤0.8,
  where χ1z (χ2z) is the spin of the heavier (lighter) black hole in
  the direction of orbital angular momentum. The surrogate reproduces
  the hybrid waveforms accurately, with mismatches ≲3×10-4 over the
  mass range 2.25  M⊙≤M≤300  M⊙. At high masses (M≳40  M⊙), where the
  merger and ringdown are more prominent, we show roughly 2 orders of
  magnitude improvement over existing waveform models. We also show
  that the surrogate works well even when extrapolated outside its
  training parameter space range, including at spins as large as
  0.998. Finally, we show that this model accurately reproduces the
  spheroidal-spherical mode mixing present in the NR ringdown signal.
---
