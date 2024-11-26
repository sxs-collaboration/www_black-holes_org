---
title: "Laying the foundation of the effective-one-body waveform models SEOBNRv5: Improved accuracy and efficiency for spinning nonprecessing binary black holes"
authors:
  - "Pompili, Lorenzo"
  - "Buonanno, Alessandra"
  - "Estellés, Héctor"
  - "Khalil, Mohammed"
  - "van de Meent, Maarten"
  - "Mihaylov, Deyan P."
  - "Ossokine, Serguei"
  - "Pürrer, Michael"
  - "Ramos-Buades, Antoni"
  - "Mehta, Ajit Kumar"
  - "Cotesta, Roberto"
  - "Marsat, Sylvain"
  - "Boyle, Michael"
  - "Kidder, Lawrence E."
  - "Pfeiffer, Harald P."
  - "Scheel, Mark A."
  - "Rüter, Hannes R."
  - "Vu, Nils"
  - "Dudi, Reetika"
  - "Ma, Sizheng"
  - "Mitman, Keefe"
  - "Melchor, Denyz"
  - "Thomas, Sierra"
  - "Sanchez, Jennifer"
jref: "Phys.Rev.D 108, 124035 (2023)"
doi: "10.1103/PhysRevD.108.124035"
date: 2023-03-31
arxiv: "2303.18039"
used_spec: true
abstract: |
  We present SEOBNRv5HM, a more accurate and faster inspiral-merger-
  ringdown gravitational waveform model for quasicircular, spinning,
  nonprecessing binary black holes within the effective-one-body (EOB)
  formalism. Compared to its predecessor, SEOBNRv4HM, the waveform
  model (i) incorporates recent high-order post-Newtonian results in
  the inspiral, with improved resummations, (ii) includes the
  gravitational modes <math display="inline"><mo
  stretchy="false">(</mo><mo>ℓ</mo><mo>,</mo><mo
  stretchy="false">|</mo><mi>m</mi><mo stretchy="false">|</mo><mo
  stretchy="false">)</mo><mo>=</mo><mo
  stretchy="false">(</mo><mn>3</mn><mo>,</mo><mn>2</mn><mo
  stretchy="false">)</mo><mo>,</mo><mo
  stretchy="false">(</mo><mn>4</mn><mo>,</mo><mn>3</mn><mo
  stretchy="false">)</mo></math>, in addition to the (2,2), (3,3),
  (2,1), (4,4), (5,5) modes already implemented in SEOBNRv4HM,
  (iii) is calibrated to larger mass ratios and spins using a catalog
  of 442 numerical-relativity (NR) simulations and 13 additional
  waveforms from black-hole perturbation theory, and (iv) incorporates
  information from second-order gravitational self-force in the
  nonspinning modes and radiation-reaction force. Computing the
  unfaithfulness against NR simulations, we find that for the dominant
  (2,2) mode the maximum unfaithfulness in the total mass range <math 
  display="inline"><mrow><mn>10</mn><mi>–</mi><mn>300</mn><msub><mrow>
  <mi>M</mi></mrow><mrow><mo
  stretchy="false">⊙</mo></mrow></msub></mrow></math> is below <math d
  isplay="inline"><msup><mn>10</mn><mrow><mo>-
  </mo><mn>3</mn></mrow></msup></math> for 90% of the cases (38% for
  SEOBNRv4HM). When including all modes up to <math
  display="inline"><mo>ℓ</mo><mo>=</mo><mn>5</mn></math> we find 98%
  (49%) of the cases with unfaithfulness below <math display="inline">
  <msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>
  (<math display="inline"><msup><mn>10</mn><mrow><mo>-
  </mo><mn>3</mn></mrow></msup></math>), while these numbers reduce to
  88% (5%) when using SEOBNRv4HM. Furthermore, the model shows
  improved agreement with NR in other dynamical quantities (e.g., the
  angular momentum flux and binding energy), providing a powerful
  check of its physical robustness. We implemented the waveform model
  in a high-performance python package (pyseobnr), which leads to
  evaluation times faster than SEOBNRv4HM by a factor of 10 to 50,
  depending on the configuration, and provides the flexibility to
  easily include spin-precession and eccentric effects, thus making it
  the starting point for a new generation of EOBNR waveform models
  (SEOBNRv5) to be employed for upcoming observing runs of the LIGO-
  Virgo-KAGRA detectors.
---
