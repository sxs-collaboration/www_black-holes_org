---
title: "Automated determination of the end time of junk radiation in binary black hole simulations"
authors:
  - "Pretto, Isabella G."
  - "Scheel, Mark A."
  - "Teukolsky, Saul A."
jref:
doi:
date: 2024-07-29
arxiv: "2407.20470"
used_spec: true
abstract: |
  When numerically solving Einstein's equations for the evolution of
  binary black holes, physical imperfections in the initial data
  manifest as a transient, high-frequency pulse of ''junk radiation.''
  This unphysical signal must be removed before the waveform can be
  used. Improvements in the efficiency of numerical simulations now
  allow waveform catalogs containing thousands of waveforms to be
  produced. Thus, an automated procedure for identifying junk
  radiation is required. To this end, we present a new algorithm based
  on the empirical mode decomposition (EMD) from the Hilbert-Huang
  transform. This approach allows us to isolate and measure the high-
  frequency oscillations present in the measured irreducible masses of
  the black holes. The decay of these oscillations allows us to
  estimate the time from which the junk radiation can be ignored. To
  make this procedure more precise, we propose three distinct
  threshold criteria that specify how small the contribution of junk
  radiation has to be before it can be considered negligible. We apply
  this algorithm to 3403 BBH simulations from the SXS catalog to find
  appropriate values for the thresholds in the three criteria. We find
  that this approach yields reliable decay time estimates, i.e., when
  to consider the simulation physical, for over 98.6% of the
  simulations studied. This demonstrates the efficacy of the EMD as a
  suitable tool to automatically isolate and characterize junk
  radiation in the simulation of binary black hole systems.
---
