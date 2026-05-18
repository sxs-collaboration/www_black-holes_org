---
title: "Axisymmetric hydrodynamics in numerical relativity: treating coordinate singularity, artificial heating and modeling MHD instabilities"
authors:
  - "Chawhan, Pavan"
  - "Duez, Matthew D."
  - "Foucart, Francois"
  - "Cheong, Patrick Chi-Kit"
  - "Muhammed, Nishad"
jref: "Class.Quant.Grav. 43, 095026 (2026)"
doi: "10.1088/1361-6382/ae62ee"
date: 2025-10-15
arxiv: "2510.14127"
insp_recid: 3070465
used_spec: true
used_spectre:
abstract: |
  Two-dimensional axisymmetric simulations of binary neutron star
  (BNS) merger remnant are a cheap alternative to 3D simulations. To
  maintain realism for secular timescales, simulations must avoid
  accumulated errors from drifts in conserved quantities and
  artificial heating, and they must model turbulent transport in a way
  that remains plausible throughout the evolution. It is also crucial
  to avoid numerical artifacts due to the polar coordinate axis
  singularity. Methods that behave well near the axis often break
  flux-conservative form of the hydrodynamic equations, resulting in
  significant drifts in conserved quantities. We present a flux-
  conservative scheme that maintains smoothness near the axis without
  sacrificing conservative formulation of the equations or incurring
  drifts in conserved global quantities. We compare the numerical
  performance of different treatments of the hydrodynamic equations
  when evolving a hypermassive neutron star resembling the remnant of
  a BNS merger. These simulations demonstrate that the new scheme
  combines the axis smoothness of non-conservative methods with the
  mass and angular momentum conservation of other conservative methods
  on \(\sim 10^2\) ms timescales of viscous and neutrino-driven
  evolution. Because fluid profiles remain smooth in the remnant
  interior, it is possible to remove artificial heating by evolving
  the entropy density. We show how physical heating and cooling terms
  can be easily calculated from source terms of the conservative
  evolution variables and demonstrate our implementation. Finally, we
  discuss and implement improvements to the effective viscosity scheme
  to better model the effect of magnetohydrodynamic instabilities as
  the remnant evolves.
---
