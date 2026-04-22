---
title: "Including higher-order modes in a quadrupolar eccentric numerical relativity surrogate using universal eccentric modulation functions"
authors:
  - "Islam, Tousif"
  - "Ravichandran, Adhrit"
  - "Nee, Peter James"
  - "Field, Scott E."
  - "Varma, Vijay"
  - "Pfeiffer, Harald P."
  - "Ceja, Andrea"
  - "Ghadiri, Noora"
  - "Kidder, Lawrence E."
  - "Kumar, Prayush"
  - "Morales, Marlo"
  - "Ravishankar, Abhishek"
  - "Ramos-Buades, Antoni"
  - "Rink, Katie"
  - "Ruter, Hannes R."
  - "Scheel, Mark A."
  - "Shaikh, Md Arif"
  - "Tellez, Daniel"
jref:
doi:
date: 2026-04-20
arxiv: "2604.17868"
insp_recid: 3147122
used_spec: true
used_spectre:
abstract: |
  \texttt{gwNRHME} is a framework that converts multi-modal (i.e.,
  containing several spherical harmonic modes) quasi-circular
  waveforms into their eccentric counterparts, provided the
  quadrupolar eccentric mode is known, by exploiting universal
  eccentric modulation functions. Leveraging this framework, we
  combine the quasi-circular NR surrogate model \texttt{NRHybSur3dq8}
  with the quadrupolar, non-spinning, eccentric surrogate
  \texttt{NRSurE\_q4NoSpin\_22} to construct a multi-modal, non-
  spinning, eccentric model, denoted as \model, which includes nine
  modes: $(2,\{1,2\})$, $(3,\{1,2,3\})$, $(4,\{2,3,4\})$, and $(5,5)$.
  When compared against 156 eccentric SXS NR waveforms, \model
  achieves median frequency-domain mismatches (computed using the
  Advanced LIGO design sensitivity) of $\sim 9\times 10^{-5}$, with a
  standard deviation of $\sim 2 \times 10^{-4}$. To demonstrate the
  modularity of the framework, we further combine
  \texttt{NRSurE\_q4NoSpin\_22} with effective-one-body (EOB) models
  \texttt{SEOBNRv5HM} and \texttt{TEOBResumS-Dali} in their non-
  spinning limits, yielding eccentric waveforms with median mismatches
  of $\sim 2\times10^{-4}$ and $\sim 10^{-3}$, respectively, with
  standard deviation of $\sim 2 \times 10^{-3}$ and $\sim 2 \times
  10^{-2}$ respectively. Finally, we provide both a surrogate model,
  \texttt{gwEccEvolve\_q4NoSpin\_Sur}, and an analytical model,
  \texttt{gwEccEvNSv2}, for the eccentricity evolution up to $2M$
  before merger, based on eccentricity definitions derived from the
  universal modulation functions. The \texttt{gwNRHME} framework is
  publicly available through the \texttt{gwModels} package, and the
  resulting waveform models will be released via the
  \texttt{gwsurrogate} package.
---
