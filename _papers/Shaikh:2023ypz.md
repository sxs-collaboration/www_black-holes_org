---
title: "Defining eccentricity for gravitational wave astronomy"
authors:
  - "Shaikh, Md Arif"
  - "Varma, Vijay"
  - "Pfeiffer, Harald P."
  - "Ramos-Buades, Antoni"
  - "van de Meent, Maarten"
jref: "Phys.Rev.D 108, 104007 (2023)"
doi: "10.1103/PhysRevD.108.104007"
date: 2023-02-22
arxiv: "2302.11257"
insp_recid: 2635504
used_spec: true
used_spectre:
abstract: |
  Eccentric compact binary mergers are significant scientific targets
  for current and future gravitational wave observatories. To detect
  and analyze eccentric signals, there is an increasing effort to
  develop waveform models, numerical relativity simulations, and
  parameter estimation frameworks for eccentric binaries.
  Unfortunately, current models and simulations use different internal
  parametrizations of eccentricity in the absence of a unique natural
  definition of eccentricity in general relativity, which can result
  in incompatible eccentricity measurements. In this paper, we adopt a
  standardized definition of eccentricity and mean anomaly based
  solely on waveform quantities and make our implementation publicly
  available through an easy-to-use python package, gw_eccentricity.
  This definition is free of gauge ambiguities, has the correct
  Newtonian limit, and can be applied as a postprocessing step when
  comparing eccentricity measurements from different models. This
  standardization puts all models and simulations on the same footing
  and enables direct comparisons between eccentricity estimates from
  gravitational wave observations and astrophysical predictions. We
  demonstrate the applicability of this definition and the robustness
  of our implementation for waveforms of different origins, including
  post-Newtonian theory, effective-one-body, extreme mass ratio
  inspirals, and numerical relativity simulations. We focus on
  binaries without spin precession in this work, but possible
  generalizations to spin-precessing binaries are discussed.
---
