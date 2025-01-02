---
title: "Gravitational wave surrogate model for spinning, intermediate mass ratio binaries based on perturbation theory and numerical relativity"
authors:
  - "Rink, Katie"
  - "Bachhar, Ritesh"
  - "Islam, Tousif"
  - "Rifat, Nur E.M."
  - "Gonzalez-Quesada, Kevin"
  - "Field, Scott E."
  - "Khanna, Gaurav"
  - "Hughes, Scott A."
  - "Varma, Vijay"
jref: "Phys.Rev.D 110, 124069 (2024)"
doi: "10.1103/PhysRevD.110.124069"
date: 2024-07-25
arxiv: "2407.18319"
abstract: |
  We present BHPTNRSur2dq1e3, a reduced order surrogate model of
  gravitational waves emitted from binary black hole (BBH) systems in
  the comparable to large mass ratio regime with aligned spin (<math
  display="inline"><msub><mi>χ</mi><mn>1</mn></msub></math>) on the
  heavier mass (<math
  display="inline"><msub><mi>m</mi><mn>1</mn></msub></math>). We
  trained this model on waveform data generated from point particle
  black hole perturbation theory (ppBHPT) with mass ratios varying
  from <math
  display="inline"><mn>3</mn><mo>≤</mo><mi>q</mi><mo>≤</mo><mn>1000</mn></math>
  and spins from <math
  display="inline"><mo>-</mo><mn>0.8</mn><mo>≤</mo><msub><mi>χ</mi><mn>1</mn></msub><mo>≤</mo><mn>0.8</mn></math>.
  The waveforms are 13,500 <math
  display="inline"><msub><mi>m</mi><mn>1</mn></msub></math> long and
  include all <math
  display="inline"><mo>ℓ</mo><mo>≤</mo><mn>4</mn></math> spin-weighted
  spherical harmonic modes except the (4,1) and <math
  display="inline"><mi>m</mi><mo>=</mo><mn>0</mn></math> modes. We
  find that, for binaries with <math
  display="inline"><msub><mi>χ</mi><mn>1</mn></msub><mo>≲</mo><mo>-</mo><mn>0.5</mn></math>,
  retrograde quasinormal modes are significantly excited, thereby
  complicating the modeling process. To overcome this issue, we
  introduce a domain decomposition approach to model the inspiral and
  merger-ringdown portion of the signal separately. The resulting
  model can faithfully reproduce ppBHPT waveforms with a median time-
  domain mismatch error of <math
  display="inline"><mn>8</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>5</mn></mrow></msup></math>.
  We then calibrate our model with numerical relativity (NR) data in
  the comparable mass regime (<math
  display="inline"><mn>3</mn><mo>≤</mo><mi>q</mi><mo>≤</mo><mn>10</mn></math>).
  By comparing with spin-aligned BBH NR simulations at <math
  display="inline"><mi>q</mi><mo>=</mo><mn>15</mn></math>, we find
  that the dominant quadrupolar (subdominant) modes agree to better
  than <math
  display="inline"><mo>≈</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></math>
  (<math
  display="inline"><mo>≈</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>)
  when using a time-domain mismatch error, where the largest source of
  calibration error comes from the transition-to-plunge and ringdown
  approximations of perturbation theory. Mismatch errors are below
  <math
  display="inline"><mo>≈</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>
  for systems with mass ratios between <math
  display="inline"><mn>6</mn><mo>≤</mo><mi>q</mi><mo>≤</mo><mn>15</mn></math>
  and typically get smaller at larger mass ratio. Our two models—both
  the ppBHPT waveform model and the NR-calibrated ppBHPT model—will be
  publicly available through gwsurrogate and the black hole
  perturbation toolkit packages.
---
