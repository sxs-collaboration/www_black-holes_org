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
jref: "Phys.Rev.D 114, 044078 (2026)"
doi: "10.1103/fq4r-rt3z"
date: 2026-04-20
arxiv: "2604.17868"
insp_recid: 3147122
used_spec: true
used_spectre:
abstract: |
  gwNRHME is a framework that converts multimodal (i.e., containing
  several spherical harmonic modes) quasicircular waveforms into their
  eccentric counterparts, provided the quadrupolar eccentric mode is
  known, by exploiting universal eccentric modulation functions.
  Leveraging this framework, we combine the quasicircular numerical
  relativity (NR) surrogate model NRHybSur3dq8 with the quadrupolar,
  nonspinning, eccentric surrogate NRSurE_q4NoSpin_22 to construct a
  multimodal, nonspinning, eccentric model, denoted as
  gwNRHME_NRSur_q4, which includes nine modes: <math
  display="inline"><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mo
  stretchy="false">{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo
  stretchy="false">}</mo><mo stretchy="false">)</mo></math>, <math
  display="inline"><mo stretchy="false">(</mo><mn>3</mn><mo>,</mo><mo
  stretchy="false">{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo
  stretchy="false">}</mo><mo stretchy="false">)</mo></math>, <math
  display="inline"><mo stretchy="false">(</mo><mn>4</mn><mo>,</mo><mo
  stretchy="false">{</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo
  stretchy="false">}</mo><mo stretchy="false">)</mo></math>, and (5,
  5). When compared against 156 eccentric Simulating eXtreme
  Spacetimes NR waveforms, gwNRHME_NRSur_q4 achieves median frequency-
  domain mismatches (computed using the Advanced LIGO design
  sensitivity) of <math
  display="inline"><mo>∼</mo><mn>9</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>5</mn></mrow></msup></math>,
  with a standard deviation of <math
  display="inline"><mo>∼</mo><mn>2</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup></math>.
  To demonstrate the modularity of the framework, we further combine
  NRSurE_q4NoSpin_22 with effective-one-body models SEOBNRv5HM and
  TEOBResumS-Dali in their nonspinning limits, yielding eccentric
  waveforms with median mismatches of <math
  display="inline"><mo>∼</mo><mn>2</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup></math>
  and <math
  display="inline"><mo>∼</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></math>,
  respectively, with standard deviation of <math
  display="inline"><mo>∼</mo><mn>2</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></math>
  and <math
  display="inline"><mo>∼</mo><mn>2</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>,
  respectively. Finally, we provide both a surrogate model,
  gwEccEvolve_q4NoSpin_Sur, and an analytical model, gwEccEvNSv2, for
  the eccentricity evolution up to <math
  display="inline"><mn>2</mn><mi>M</mi></math> before merger, based on
  eccentricity definitions derived from the universal modulation
  functions. The gwNRHME framework is publicly available through the
  gwModels package, and the resulting waveform models will be released
  via the gwsurrogate package.
---
