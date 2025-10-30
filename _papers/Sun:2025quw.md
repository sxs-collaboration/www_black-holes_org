---
title: "Gauge Boundary conditions to mitigate CoM drift in BBH simulations"
authors:
  - "Sun, Dongze"
  - "Ma, Sizheng"
  - "Scheel, Mark A."
  - "Teukolsky, Saul A."
jref:
doi:
date: 2025-10-29
arxiv: "2510.25465"
insp_recid: 3074809
used_spec:
used_spectre:
abstract: |
  Long-term numerical relativity (NR) simulations of binary black hole
  (BBH) systems in the Spectral Einstein Code (SpEC) code exhibit an
  unexpected exponential drift of the center-of-mass (CoM) away from
  the simulation's origin. In our work, we analyze this phenomenon and
  demonstrate that it is not a physical effect but rather a
  manifestation of a gauge artifact. The origin of this drift is the
  reflection of the gauge waves off the outer boundary of the
  computational domain. These reflections are introduced by
  inaccuracies in the gauge boundary condition, specifically, the
  application of the Sommerfeld condition to the time derivative of
  the gauge fields. Such an approach fails to completely suppress or
  correctly absorb the outgoing modes, thereby generating artificial
  feedback into the simulation. To mitigate this problem, we introduce
  a modified boundary condition that incorporates an explicit CoM
  correction source term designed to counteract the CoM motion. Our
  numerical experiments, performed with the SpEC code, reveal that
  this new boundary treatment reduces the CoM drift by several orders
  of magnitude compared to the standard implementation, and does not
  introduce any unwanted physical artifacts.
---
