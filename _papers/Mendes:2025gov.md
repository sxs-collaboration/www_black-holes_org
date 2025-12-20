---
title: "Parameter control for binary black hole initial data"
authors:
  - "Mendes, Iago B."
  - "Vu, Nils L."
  - "Long, Oliver"
  - "Pfeiffer, Harald P."
  - "Owen, Robert"
jref: "Phys.Rev.D 112, 124049 (2025)"
doi: "10.1103/zh31-bbtm"
date: 2025-09-08
arxiv: "2509.07291"
insp_recid: 2968087
used_spec: true
used_spectre: true
abstract: |
  When numerically solving Einstein’s equations for binary black holes
  (BBH), we must find initial data on a three-dimensional spatial
  slice by solving constraint equations. The construction of initial
  data is a multistep process, in which one first chooses freely
  specifiable data that define a conformal background and impose
  boundary conditions. Then, one numerically solves elliptic equations
  and calculates physical properties such as horizon masses, spins,
  and asymptotic quantities from the solution. To achieve desired
  properties, one adjusts the free data in an iterative “control”
  loop. Previous methods for these iterative adjustments rely on
  Newtonian approximations and do not allow the direct control of
  total energy and angular momentum of the system, which becomes
  particularly important in the study of hyperbolic encounters of
  black holes. Using the spectre code, we present a novel parameter
  control procedure that benefits from Broyden’s method in all
  controlled quantities. We use this control scheme to minimize drifts
  in bound orbits and to enable the construction of hyperbolic
  encounters. We see that the activation of off-diagonal terms in the
  control Jacobian gives us better efficiency when compared to the
  simpler implementation in the Spectral Einstein Code. We demonstrate
  robustness of the method across extreme configurations, including
  spin magnitudes up to <math
  display="inline"><mrow><mi>χ</mi><mo>=</mo><mn>0.9999</mn></mrow></math>,
  mass ratios up to <math
  display="inline"><mi>q</mi><mo>=</mo><mn>50</mn></math>, and initial
  separations up to <math
  display="inline"><msub><mi>D</mi><mn>0</mn></msub><mo>=</mo><mn>1000</mn><mi>M</mi></math>.
  Given the open-source nature of spectre, this is the first time a
  parameter control scheme for constructing bound and unbound BBH
  initial data is available to the numerical-relativity community.
---
