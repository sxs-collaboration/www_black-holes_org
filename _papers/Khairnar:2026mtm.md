---
title: "Fixing the center-of-mass frame of numerical relativity waveforms using the post-Newtonian center-of-mass charge"
authors:
  - "Khairnar, Aniket"
  - "Stein, Leo C."
  - "Boyle, Michael"
  - "Deppe, Nils"
  - "Kidder, Lawrence E."
  - "Mitman, Keefe"
  - "Moxon, Jordan"
  - "Nelli, Kyle C."
  - "Throwe, William"
  - "Vu, Nils L."
jref:
doi:
date: 2026-03-25
arxiv: "2603.24661"
insp_recid: 3136426
used_spec: true
used_spectre: true
abstract: |
  The Bondi--van der Burg--Metzner--Sachs (BMS) frame of gravitational
  waves produced by numerical relativity (NR) simulations is crucial
  for building accurate waveform models. A proper comparison of NR
  waveforms with other models requires fixing the arbitrary BMS frame.
  In this work we improve the center-of-mass (CoM) frame fixing for
  quasicircular, nonprecessing binary systems. Past work approximated
  the CoM motion with just a linear fit. We compute a post-Newtonian
  result of the boosted CoM charge to also capture its physical out-
  spiraling oscillations. We show that using the analytical results
  improves the robustness of the fit parameters -- translation and
  boost vectors -- to the choice of duration and time of the fitting
  window. Our analysis demonstrates a maximum improvement in
  robustness when the window is placed at the center of the inspiral.
  We quantified this improvement by computing the ratio of variances
  of fit parameters when the fit window size is varied. The largest
  improvement in robustness of parameters is by a factor of $\sim 25$
  for the boost vector and $\sim 20$ for the translation vector.
  Finally, we incorporate this method into the BMS frame-fixing
  routine of the python package $\texttt{scri}$ for waveforms produced
  with Cauchy-characteristic evolution.
---
