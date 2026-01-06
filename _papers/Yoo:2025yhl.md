---
title: "Learning Post-Newtonian Corrections from Numerical Relativity"
authors:
  - "Yoo, Jooheon"
  - "Boyle, Michael"
  - "Deppe, Nils"
jref:
doi:
date: 2025-11-13
arxiv: "2511.10522"
insp_recid: 3082751
used_spec: true
used_spectre:
abstract: |
  Accurate modeling of gravitational waveforms from compact binary
  coalescences remains central to gravitational-wave (GW) astronomy.
  Post-Newtonian (PN) approximations capture the early inspiral
  dynamics analytically but break down near merger, while numerical
  relativity (NR) provides the accurate yet computationally expensive
  waveforms over limited parameter ranges. We develop a physics-
  informed neural network (PINN) framework that learns corrections
  mapping PN dynamics and waveforms to their NR counterparts. As a
  demonstration of the approach, we use the TaylorT4 PN model as the
  baseline, and train the network on a remarkably small dataset of
  only eight hybridized NR surrogate waveforms (NRHybSur3dq8) to learn
  higher-order corrections to the orbital dynamics and waveform modes
  for nonspinning noneccentric systems. Physically motivated loss
  terms enforce known limits and symmetries, such as vanishing
  corrections in the Newtonian limit and suppression of odd-\(m\) modes
  in equal-mass systems, promoting consistent and reliable
  extrapolation beyond the training region. We simultaneously
  incorporate corrections that account for the different meaning of
  mass parameters in PN and NR descriptions. The learned corrections
  significantly reduce the phase and amplitude error through the
  inspiral up to about \(200M\) before the merger. This approach
  provides a differentiable and computationally efficient bridge
  between PN and NR, offering a path toward waveform models that
  generalize more robustly beyond existing NR datasets.
---
