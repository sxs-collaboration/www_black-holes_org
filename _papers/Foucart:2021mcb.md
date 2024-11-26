---
title: "Implementation of Monte Carlo Transport in the General Relativistic SpEC Code"
authors:
  - "Foucart, Francois"
  - "Duez, Matthew D."
  - "Hebert, Francois"
  - "Kidder, Lawrence E."
  - "Kovarik, Phillip"
  - "Pfeiffer, Harald P."
  - "Scheel, Mark A."
jref: "Astrophys.J. 920, 82 (2021)"
doi: "10.3847/1538-4357/ac1737"
date: 2021-03-30
arxiv: "2103.16588"
used_spec: true
abstract: |
  Neutrino transport and neutrino−matter interactions are known to
  play an important role in the evolution of neutron star mergers and
  of their post-merger remnants. Neutrinos cool remnants, drive post-
  merger winds, and deposit energy in the low-density polar regions
  where relativistic jets may eventually form. Neutrinos also modify
  the composition of the ejected material, impacting the outcome of
  nucleosynthesis in merger outflows and the properties of the
  optical/infrared transients that they power (kilonovae). So far,
  merger simulations have largely relied on approximate treatments of
  the neutrinos (leakage, moments) that simplify the equations of
  radiation transport in a way that makes simulations more affordable
  but also introduces unquantifiable errors in the results. To improve
  on these methods, we recently published a first simulation of
  neutron star mergers using a low-cost Monte Carlo algorithm for
  neutrino radiation transport. Our transport code limits costs in
  optically thick regions by placing a hard ceiling on the value of
  the absorption opacity of the fluid, yet all approximations made
  within the code are designed to vanish in the limit of infinite
  numerical resolution. We provide here an in-depth description of
  this algorithm, of its implementation in the SpEC merger code, and
  of the expected impact of our approximations in optically thick
  regions. We argue that the last is a subdominant source of error at
  the accuracy reached by current simulations and for the interactions
  currently included in our code. We also provide tests of the most
  important features of this code.
---
