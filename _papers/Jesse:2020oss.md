---
title: "Axisymmetric hydrodynamics in numerical relativity using a multipatch method"
authors:
  - "Jesse, Jerred"
  - "Duez, Matthew D."
  - "Foucart, Francois"
  - "Haddadi, Milad"
  - "Knight, Alexander L."
  - "Cadenhead, Courtney L."
  - "Hebert, Francois"
  - "Kidder, Lawrence E."
  - "Pfeiffer, Harald P."
  - "Scheel, Mark A."
jref: "Class.Quant.Grav. 37, 235010 (2020)"
doi: "10.1088/1361-6382/abbc8b"
date: 2020-05-04
arxiv: "2005.01848"
used_spec: true
abstract: |
  We describe a method of implementing the axisymmetric evolution of
  general-relativistic hydrodynamics and magnetohydrodynamics through
  modification of a multipatch grid scheme. In order to ease the
  computational requirements required to evolve the post-merger phase
  of systems involving binary compact massive objects in numerical
  relativity, it is often beneficial to take advantage of these
  system’s tendency to rapidly settle into states that are nearly
  axisymmetric, allowing for 2D evolution of secular timescales. We
  implement this scheme in the spectral Einstein code and show the
  results of application of this method to four test systems including
  viscosity, magnetic fields, and neutrino radiation transport. Our
  results show that this method can be used to quickly allow already
  existing 3D infrastructure that makes use of local coordinate system
  transformations to be made to run in axisymmetric 2D with the
  flexible grid creation capabilities of multipatch methods. Our code
  tests include a simple model of a binary neutron star postmerger
  remnant, for which we confirm the formation of a massive torus which
  is a promising source of post-merger ejecta.
---
