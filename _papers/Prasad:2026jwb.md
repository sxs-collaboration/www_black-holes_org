---
title: "A catalog of long, eccentric and precessing binary black hole simulations from ICTS-TIFR"
authors:
  - "Prasad, Vaishak"
  - "Kumar, Prayush"
  - "Boyle, Michael"
  - "Kidder, Lawrence E."
  - "Pfeiffer, Harald P."
  - "Scheel, Mark A."
jref:
doi:
date: 2026-10-14
arxiv: "2610.19688"
insp_recid: 3215101
used_spec:
used_spectre:
abstract: |
  We present a catalogue of 31 binary black hole simulations performed
  with the Spectral Einstein Code (SpEC) on the Sonic cluster at ICTS-
  TIFR, Bengaluru between August 2023 and December 2024, targeting the
  sparsely covered corner of parameter space in which orbital
  eccentricity and spin-orbit precession are present simultaneously:
  17 configurations are both eccentric and precessing, spanning mass
  ratios \(1 \le q \le 11\) and initial eccentricities up to
  \(\hat{e}_0 = 0.40\). The longest, EccPrecDiff002, inspirals for 80
  orbits (159 gravitational-wave cycles), to our knowledge the longest
  simultaneously eccentric and precessing binary black hole evolution
  to date. Compile-time optimisation of SpEC and its third-party
  library stack for the AMD Zen-2 architecture delivered a 90% speedup
  of the initial-data solver and a 40% speedup of the evolution,
  roughly half of the latter traceable to a single defect in how
  pre-2.34 glibc reported cache topology on AMD processors. The
  campaign consumed \(1.18 \times 10^{6}\) CPU-hours. We document the
  post-processing pipeline and validate the frame transformation and
  waveforms. Eccentricity is measured from the waveforms and compared
  against the initial data. The first law of binary black hole
  mechanics, a test of approximate helical symmetry, is satisfied to
  better than 0.54% for every configuration with \(e_ω < 0.2\), and we
  show that even precessing systems can be regarded as possessing
  approximate helical symmetry in the co-precessing frame. Using the
  aligned-spin simulations to calibrate the numerical floor, the co-
  precessing approximation's mirror-symmetry violation lies three to
  four ordersof magnitude above it, growing from 0.7% to 5.3%with
  opening angle. EccPrecDiff002 spans the band above 5 Hz without
  hybridisationfor \(M \le 62\,M_\odot\), giving a single-
  interferometer signal-to-noise ratio of 961 in Cosmic Explorer at 1
  Gpc.
---
