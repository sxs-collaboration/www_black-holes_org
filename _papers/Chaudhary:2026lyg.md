---
title: "Finding black hole spins efficiently during a numerical binary evolution"
authors:
  - "Chaudhary, Himanshu"
  - "Owen, Rob"
  - "Scheel, Mark A."
  - "Teukolsky, Saul A."
jref:
doi:
date: 2026-08-12
arxiv: "2608.12211"
insp_recid: 3190436
used_spec: true
used_spectre:
abstract: |
  The dynamics of a binary black hole system depend on its masses and
  spins. For a binary at finite separation, it is not possible to
  define these quantities in an unambiguous way; however, there are
  several reasonable definitions that reduce to the expected values in
  the limit of infinite separation. Approximate Killing vector (AKV)
  spin is one of the spin definitions used in the numerical relativity
  code SpEC. AKV spin requires finding approximate Killing vectors on
  an apparent horizon, which reduces to a generalized eigenvalue
  problem of size \(\mathcal{O}(L^2)\), and a direct solve has time
  complexity \(\mathcal{O}(L^6)\), where \(L\) is the highest
  spherical harmonic mode used to represent the apparent horizon. This
  scaling means that the cost of computing AKV spins increases rapidly
  as we simulate systems at higher resolutions, especially those with
  high spin or mass ratios. We describe a new algorithm for computing
  AKV spins that is much faster than the current algorithm.
---
