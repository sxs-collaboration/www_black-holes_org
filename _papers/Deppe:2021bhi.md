---
title: "Simulating magnetized neutron stars with discontinuous Galerkin methods"
authors:
  - "Deppe, Nils"
  - "Hébert, François"
  - "Kidder, Lawrence E."
  - "Throwe, William"
  - "Anantpurkar, Isha"
  - "Armaza, Cristóbal"
  - "Bonilla, Gabriel S."
  - "Boyle, Michael"
  - "Chaudhary, Himanshu"
  - "Duez, Matthew D."
  - "Vu, Nils L."
  - "Foucart, Francois"
  - "Giesler, Matthew"
  - "Guo, Jason S."
  - "Kim, Yoonsoo"
  - "Kumar, Prayush"
  - "Legred, Isaac"
  - "Li, Dongjun"
  - "Lovelace, Geoffrey"
  - "Ma, Sizheng"
  - "Macedo, Alexandra"
  - "Melchor, Denyz"
  - "Morales, Marlo"
  - "Moxon, Jordan"
  - "Nelli, Kyle C."
  - "O'Shea, Eamonn"
  - "Pfeiffer, Harald P."
  - "Ramirez, Teresita"
  - "Rüter, Hannes R."
  - "Sanchez, Jennifer"
  - "Scheel, Mark A."
  - "Thomas, Sierra"
  - "Vieira, Daniel"
  - "Wittek, Nikolas A."
  - "Wlodarczyk, Tom"
  - "Teukolsky, Saul A."
jref: "Phys.Rev.D 105, 123031 (2022)"
doi: "10.1103/PhysRevD.105.123031"
date: 2021-09-24
arxiv: "2109.12033"
abstract: |
  Discontinuous Galerkin methods are popular because they can achieve
  high order where the solution is smooth, because they can capture
  shocks while needing only nearest-neighbor communication, and
  because they are relatively easy to formulate on complex meshes. We
  perform a detailed comparison of various limiting strategies
  presented in the literature applied to the equations of general
  relativistic magnetohydrodynamics. We compare the standard Lambda Pi^N
  limiter, the
  hierarchical limiter of Krivodonova, the simple WENO limiter, the
  HWENO limiter, and a discontinuous Galerkin-finite-difference hybrid
  method. The ultimate goal is to understand what limiting strategies
  are able to robustly simulate magnetized Tolman-Oppenheimer-Volkoff
  stars without any fine-tuning of parameters. Among the limiters
  explored here, the only limiting strategy we can endorse is a
  discontinuous Galerkin-finite-difference hybrid method.
---
