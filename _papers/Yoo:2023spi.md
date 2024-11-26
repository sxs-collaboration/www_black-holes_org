---
title: "Numerical relativity surrogate model with memory effects and post-Newtonian hybridization"
authors:
  - "Yoo, Jooheon"
  - "Mitman, Keefe"
  - "Varma, Vijay"
  - "Boyle, Michael"
  - "Field, Scott E."
  - "Deppe, Nils"
  - "Hébert, François"
  - "Kidder, Lawrence E."
  - "Moxon, Jordan"
  - "Pfeiffer, Harald P."
  - "Scheel, Mark A."
  - "Stein, Leo C."
  - "Teukolsky, Saul A."
  - "Throwe, William"
  - "Vu, Nils L."
jref: "Phys.Rev.D 108, 064027 (2023)"
doi: "10.1103/PhysRevD.108.064027"
date: 2023-06-05
arxiv: "2306.03148"
used_spec: true
abstract: |
  Numerical relativity simulations provide the most precise templates
  for the gravitational waves produced by binary black hole mergers.
  However, many of these simulations use an incomplete waveform
  extraction technique—extrapolation—that fails to capture important
  physics, such as gravitational memory effects. Cauchy-characteristic
  evolution (CCE), by contrast, is a much more physically accurate
  extraction procedure that fully evolves Einstein’s equations to
  future null infinity and accurately captures the expected physics.
  In this work, we present a new surrogate model, NRHybSur3dq8_CCE,
  built from CCE waveforms that have been mapped to the post-Newtonian
  (PN) BMS frame and then hybridized with PN and effective one-body
  (EOB) waveforms. This model is trained on 102 waveforms with mass
  ratios q≤8
  and aligned spins χ1z,χ2z∈[-0.8,0.8]. The model spans the
  entire LIGO-Virgo-KAGRA (LVK) frequency band (with
  f<sub>low</sub>=20Hz)
  for total masses M≳2.25M⊙ and includes the
  ℓ≤4 and
  (ℓ,m)=(5,5) spin-weight -2 spherical harmonic
  modes, but not the (3, 1), (4, 2) or (4, 1) modes. We find that
  NRHybSur3dq8_CCE can accurately reproduce the training waveforms
  with mismatches ≲2×10<sup>-4</sup>
  for total masses 2.25M⊙≤M≤300M⊙ and
  can, for a modest degree of extrapolation, capably model outside of
  its training region. Most importantly, unlike previous waveform
  models, the new surrogate model successfully captures memory
  effects.
---
