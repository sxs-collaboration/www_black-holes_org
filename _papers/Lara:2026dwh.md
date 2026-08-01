---
title: "High-accuracy drivers to simulate black hole binaries beyond general relativity with the fixing-the-equations approach"
authors:
  - "Lara, Guillermo"
  - "Pfeiffer, Harald P."
  - "Deppe, Nils"
  - "Kidder, Lawrence E."
  - "Lovelace, Geoffrey"
  - "Ma, Sizheng"
  - "Macedo, Alexandra"
  - "Moxon, Jordan"
  - "Nelli, Kyle C."
  - "Scheel, Mark A."
  - "Throwe, William"
  - "Vu, Nils L."
jref:
doi:
date: 2026-07-30
arxiv: "2607.28003"
insp_recid: 3184853
used_spec:
used_spectre:
abstract: |
  We implement the "fixing-the-equations" approach [Phys.Rev.D 96
  (2017) 8, 084043] in spectre, an NR code using a pseudo-spectral
  discontinuous Galerkin scheme, to produce long and accurate NR
  waveforms in the well-known shift-symmetric version of scalar Gauss-
  Bonnet (sGB) gravity. To achieve this, we introduce a new family of
  comoving driver equations that exploits the approximate symmetries
  of quasicircular binary systems and is designed to recover the exact
  (quasi-)stationary solutions of the fully-coupled theory. We
  validate our single black hole (BH) solutions against analytic
  predictions and show that, even for binary BHs in the early
  inspiral, the intrinsic BH quantities are relatively insensitive to
  the timescales entering the driver equation. Attention is given to
  the prescription of driver equations for tensors, for which we give
  an example of how treating tensor components as scalars can lead to
  undesired behaviour over long timescales, including spurious growth
  of the BH spins. A more appropriate generalization to the tensor
  case is given for the comoving driver, which is shown to avoid these
  issues. Overall, our implementation leverages state-of-the-art
  methods for eccentricity reduction and wave extraction with Cauchy
  Characteristic Evolution to simulate systems with eccentricity
  \(\lesssim 10^{-3}\). We obtain waveforms with phase errors
  \(\lesssim \mathcal{O}(1) \, \mathrm{rad}\) over almost 40 GW-
  cycles, which naturally incorporate memory contributions.
---
