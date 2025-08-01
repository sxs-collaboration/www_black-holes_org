---
title: "Assessing the difficulty of capturing the distribution function of neutrinos in neutron star merger simulations"
authors: "Foucart, Francois"
jref: "Phys.Rev.D 112, 023046 (2025)"
doi: "10.1103/gkk5-6wmh"
date: 2025-04-30
arxiv: "2504.21822"
insp_recid: 2916972
used_spec: true
used_spectre:
abstract: |
  The collision of two neutron stars is a rich source of information
  about nuclear physics. In particular, the kilonova signal following
  a merger can help us elucidate the role of neutron stars in
  nucleosynthesis, and informs us about the properties of matter above
  nuclear saturation. Approximate modeling of neutrinos remains an
  important limitation to our ability to make predictions for these
  observables. Part of the problem is the fermionic nature of
  neutrinos. By the exclusion principle, the expected value <math
  display="inline"><msub><mi>f</mi><mi>ν</mi></msub></math> for the
  number of neutrinos in a quantum state is at most 1. Any process
  producing neutrinos is suppressed by a blocking factor <math
  display="inline"><mo
  stretchy="false">(</mo><mn>1</mn><mo>-</mo><msub><mi>f</mi><mi>ν</mi></msub><mo
  stretchy="false">)</mo></math>. Recent simulations focused on
  neutrino physics mostly use a gray two-moment scheme to evolve
  neutrinos. This evolves integrals of <math
  display="inline"><msub><mi>f</mi><mi>ν</mi></msub></math> over
  momentum space, preventing direct calculations of blocking factors.
  Monte Carlo methods may be an attractive alternative, providing
  access to the full distribution of neutrinos. Their current
  implementation is, however, inadequate to estimate <math
  display="inline"><msub><mi>f</mi><mi>ν</mi></msub></math>: in our
  most recent simulations, a single Monte Carlo packet causes, in the
  worst cases, estimates of <math
  display="inline"><msub><mi>f</mi><mi>ν</mi></msub></math> to jump
  from <math
  display="inline"><msub><mi>f</mi><mi>ν</mi></msub><mo>=</mo><mn>0</mn></math>
  to <math
  display="inline"><msub><mi>f</mi><mi>ν</mi></msub><mo>∼</mo><msup><mn>10</mn><mn>5</mn></msup></math>.
  While this is concerning, this brazen violation of the fermionic
  nature of neutrinos has been largely inconsequential, as the
  interactions used in simulations avoid direct calculations of <math
  display="inline"><msub><mi>f</mi><mi>ν</mi></msub></math>. We are,
  however, reaching a level of modeling at which this problem can no
  longer be ignored. Here, we discuss the relatively simple origin of
  this issue. We then show that very rough estimates of <math
  display="inline"><msub><mi>f</mi><mi>ν</mi></msub></math> can in
  theory be obtained in merger simulations, but that they will require
  a combination of unintuitive weighting schemes for Monte Carlo
  packets and smoothing of the neutrino distribution at coarser
  resolution than what the merger simulation uses.
---
