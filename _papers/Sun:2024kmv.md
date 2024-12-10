---
title: "Optimizing post-Newtonian parameters and fixing the BMS frame for numerical-relativity waveform hybridizations"
authors:
  - "Sun, Dongze"
  - "Boyle, Michael"
  - "Mitman, Keefe"
  - "Scheel, Mark A."
  - "Stein, Leo C."
  - "Teukolsky, Saul A."
  - "Varma, Vijay"
jref: "Phys.Rev.D 110, 104076 (2024)"
doi: "10.1103/PhysRevD.110.104076"
date: 2024-03-15
arxiv: "2403.10278"
abstract: |
  Numerical relativity (NR) simulations of binary black holes provide
  precise waveforms, but are typically too computationally expensive
  to produce waveforms with enough orbits to cover the whole frequency
  band of gravitational-wave observatories. Accordingly, it is
  important to be able to hybridize NR waveforms with analytic, post-
  Newtonian (PN) waveforms, which are accurate during the early
  inspiral phase. We show that to build such hybrids, it is crucial to
  both fix the Bondi-Metzner-Sachs (BMS) frame of the NR waveforms to
  match that of PN theory, and optimize over the PN parameters to
  mitigate the error caused by the discrepancy between NR and PN
  parameters. We test such a hybridization procedure including all
  spin-weighted spherical harmonic modes with <math
  display="inline"><mrow><mo stretchy="false">|</mo><mi>m</mi><mo
  stretchy="false">|</mo><mo>≤</mo><mo>ℓ</mo></mrow></math> for <math
  display="inline"><mo>ℓ</mo><mo>≤</mo><mn>8</mn></math>, using 29 NR
  waveforms with mass ratios <math
  display="inline"><mi>q</mi><mo>≤</mo><mn>10</mn></math> and spin
  magnitudes <math display="inline"><mrow><mo
  stretchy="false">|</mo><msub><mrow><mi>χ</mi></mrow><mrow><mn>1</mn></mrow></msub><mo
  stretchy="false">|</mo><mo>,</mo><mo
  stretchy="false">|</mo><msub><mrow><mi>χ</mi></mrow><mrow><mn>2</mn></mrow></msub><mo
  stretchy="false">|</mo><mo>≤</mo><mn>0.8</mn></mrow></math>. We find
  that for spin-aligned systems, the PN and NR waveforms agree very
  well. The difference is limited by the small nonzero orbital
  eccentricity of the NR waveforms, or equivalently by the lack of
  eccentric terms in the PN waveforms. To maintain full accuracy of
  the simulations, the matching window for spin-aligned systems should
  be at least 5 orbits long and end at least 15 orbits before merger.
  For precessing systems, the errors are larger than for spin-aligned
  cases. The errors are likely limited by the absence of precession-
  related spin-spin PN terms. Using <math
  display="inline"><msup><mn>10</mn><mn>5</mn></msup><mi>M</mi></math>
  long NR waveforms, we find that there is no optimal choice of the
  matching window within this time span, because the hybridization
  result for precessing cases is always better if using earlier or
  longer matching windows. We provide the mean orbital frequency of
  the smallest acceptable matching window as a function of the target
  error between the PN and NR waveforms and the black hole spins.
---
