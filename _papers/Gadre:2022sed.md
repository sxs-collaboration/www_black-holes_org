---
title: "Fully precessing higher-mode surrogate model of effective-one-body waveforms"
authors:
  - "Gadre, Bhooshan"
  - "Pürrer, Michael"
  - "Field, Scott E."
  - "Ossokine, Serguei"
  - "Varma, Vijay"
jref: "Phys.Rev.D 110, 124038 (2024)"
doi: "10.1103/PhysRevD.110.124038"
date: 2022-03-01
arxiv: "2203.00381"
abstract: |
  We present a surrogate model of SEOBNRv4PHM, a fully precessing
  time-domain effective-one-body waveform model including subdominant
  modes. We follow an approach similar to that used to build recent
  numerical relativity surrogate models. Our surrogate is 5000 M in
  duration, covers mass ratios up to <math
  display="inline"><mrow><mn>1</mn><mo>∶</mo><mn>20</mn></mrow></math>
  and dimensionless spin magnitudes up to 0.8. Validating the
  surrogate against an independent test set, we find that the median
  mismatch error is less than <math
  display="inline"><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></math>,
  which is typically smaller than the modeling error of SEOBNRv4PHM
  itself. At high total mass, a few percent of configurations can
  exceed mismatches of <math
  display="inline"><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>
  if they are highly precessing and exceed a mass ratio of <math
  display="inline"><mrow><mn>1</mn><mo>∶</mo><mn>4</mn></mrow></math>.
  This surrogate is nearly 2 orders of magnitude faster than the
  underlying time-domain SEOBNRv4PHM model and can be evaluated in
  <math
  display="inline"><mo>∼</mo><mn>50</mn><mtext> </mtext><mtext> </mtext><mi>ms</mi></math>.
  Bayesian inference analyses with SEOBNRv4PHM are typically very
  computationally demanding and can take from weeks to months to
  complete. The 2 order of magnitude speedup attained by our surrogate
  model enables practical parameter estimation analyses with this
  waveform family. This is crucial because Bayesian inference allows
  us to recover the masses and spins of binary black hole mergers
  given a model of the emitted gravitational waveform along with a
  description of the noise.
---
