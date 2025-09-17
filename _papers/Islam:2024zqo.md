---
title: "Adding higher-order spherical harmonics in nonspinning eccentric binary black hole merger waveform models"
authors:
  - "Islam, Tousif"
  - "Khanna, Gaurav"
  - "Field, Scott E."
jref: "Phys.Rev.D 111, 124023 (2025)"
doi: "10.1103/63d1-hh8k"
date: 2024-08-05
arxiv: "2408.02762"
insp_recid: 2815344
used_spec: true
used_spectre:
abstract: |
  gwnrhme is a recently developed framework that seamlessly converts a
  multimodal (i.e., with several spherical harmonic modes)
  quasicircular waveform into a multimodal eccentric waveform if the
  quadrupolar eccentric waveform is known. Here, we employ the gwnrhme
  framework to combine a multimodal quasicircular numerical relativity
  surrogate waveform model nrhybsur3dq8 and quadrupolar nonspinning
  post-Newtonian eccentric waveform model eccentricimr to construct
  multimodal nonspinning eccentric model nrhybsur3dq8-gwnrhme. Using a
  total of 35 eccentric numerical relativity (NR) simulations obtained
  from the SXS and RIT catalogs, we demonstrate that
  nrhybsur3dq8-gwnrhme model predictions agree well with NR (with
  typical relative <math
  display="inline"><msub><mi>L</mi><mn>2</mn></msub></math> errors of
  <math display="inline"><mo>∼</mo><mn>0.01</mn></math> for the
  dominant quadrupolar mode) for mass ratios <math
  display="inline"><mn>1</mn><mo>≤</mo><mi>q</mi><mo>≤</mo><mn>4</mn></math>
  and eccentricities up to <math
  display="inline"><mo>∼</mo><mn>0.2</mn></math> measured about 10
  cycles before the merger. Our frequency-domain mismatches
  (calculated assuming advanced LIGO design sensitivity curve) are
  mostly below 0.01. To demonstrate the modularity of the gwnrhme
  framework, we further combine eccentricimr with the
  bhptnrsur1dq1e4bhptnrsur1dq1e4 model and develop a nonspinning
  eccentric model named bhptnrsur1dq1e4-gwnrhme. Finally, we develop a
  different variant of these models by replacing eccentricimr with
  eccentrictd. Both the gwnrhme framework and associated models are
  available through the gwmodels package.
---
