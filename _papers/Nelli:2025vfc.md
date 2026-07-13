---
title: "Horizon tracking for asynchronous parallel black hole simulations"
authors:
  - "Nelli, Kyle C."
  - "Throwe, William"
  - "Deppe, Nils"
  - "Scheel, Mark A."
  - "Kidder, Lawrence E."
  - "Vu, Nils L."
  - "Teukolsky, Saul A."
jref:
doi:
date: 2025-08-11
arxiv: "2508.08408"
insp_recid: 2959691
used_spec:
used_spectre: true
abstract: |
  In the field of gravitational wave science, next-generation
  detectors will be substantially more accurate than the current suite
  of detectors. Numerical relativity simulations of binary black hole
  (BBH) gravitational waveforms must become faster, more efficient,
  and more accurate to be used in analyses of these next-generation
  detections. One approach, which the <code>SpECTRE</code> code
  employs, is using spectral methods for accuracy along with
  asynchronous task-based parallelism to avoid idle time in
  simulations and make the most efficient use of computational
  resources. When writing an asynchronous application, algorithms must
  be redesigned compared to their synchronous counterparts. To
  illustrate this process, we present novel methods for dynamically
  tracking the apparent horizons in evolutions of BBH mergers using a
  feedback control system, all in the context of asynchronous
  parallelism. We also briefly detail how these methods can be applied
  to binary neutron star simulations performed with asynchronous
  parallelism.
---
