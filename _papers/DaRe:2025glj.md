---
title: "Modeling the BMS transformation induced by a binary black hole merger"
authors:
  - "Da Re, Guido"
  - "Mitman, Keefe"
  - "Stein, Leo C."
  - "Scheel, Mark A."
  - "Teukolsky, Saul A."
  - "Sun, Dongze"
  - "Boyle, Michael"
  - "Deppe, Nils"
  - "Field, Scott E."
  - "Kidder, Lawrence E."
  - "Moxon, Jordan"
  - "Nelli, Kyle C."
  - "Throwe, William"
  - "Varma, Vijay"
  - "Vu, Nils L."
jref: "Phys.Rev.D 111, 124019 (2025)"
doi: "10.1103/PhysRevD.111.124019"
date: 2025-03-12
arxiv: "2503.09569"
insp_recid: 2899400
used_spec: true
used_spectre: true
abstract: |
  Understanding the characteristics of the remnant black hole formed
  in a binary black hole merger is crucial for conducting
  gravitational wave astronomy. Typically, models of remnant black
  holes provide information about their mass, spin, and kick velocity.
  However, other information related to the supertranslation
  symmetries of the BMS group, such as the memory effect, is also
  important for characterizing the final state of the system. In this
  work, we build a model of the BMS transformation that maps a binary
  black hole’s inspiral frame to the remnant black hole’s canonical
  rest frame. Training data for this model are created using high-
  precision numerical relativity simulations of quasicircular systems
  with mass ratios <math
  display="inline"><mi>q</mi><mo>≤</mo><mn>8</mn></math> and spins
  parallel to the orbital angular momentum with magnitudes <math
  display="inline"><mrow><msub><mrow><mi>χ</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></math>,
  <math
  display="inline"><mrow><msub><mrow><mi>χ</mi></mrow><mrow><mn>2</mn></mrow></msub><mo
  stretchy="false">≤</mo><mn>0.8</mn></mrow></math>. We use Gaussian
  process regression to model the BMS transformations over the three-
  dimensional parameter space <math display="inline"><mo
  stretchy="false">(</mo><mi>q</mi><mo>,</mo><msubsup><mi>χ</mi><mn>1</mn><mi>z</mi></msubsup><mo>,</mo><msubsup><mi>χ</mi><mn>2</mn><mi>z</mi></msubsup><mo
  stretchy="false">)</mo></math>. The physics captured by this model
  is strictly nonperturbative and cannot be obtained from post-
  Newtonian approximations alone, as it requires knowledge of the
  strong nonlinear effects that are sourced during the merger. Apart
  from providing the first model of the supertranslation induced by a
  binary black hole merger, we also find that the kick velocities
  predicted using Cauchy-characteristic evolution waveforms are, on
  average, <math
  display="inline"><mo>∼</mo><mn>5</mn><mo>%</mo></math> larger than
  the ones obtained from extrapolated waveforms. Our work has broad
  implications for improving gravitational wave models and studying
  the large-scale impact of memory, such as on the cosmological
  background. The fits produced in this work are available through the
  python package surfinbh under the name nrsur3dq8bmsremnant.
---
