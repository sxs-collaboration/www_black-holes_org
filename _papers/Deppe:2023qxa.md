---
title: "A positivity-preserving adaptive-order finite-difference scheme for GRMHD"
authors:
  - "Deppe, Nils"
  - "Kidder, Lawrence E."
  - "Teukolsky, Saul A."
  - "Bonilla, Marceline S."
  - "Hébert, François"
  - "Kim, Yoonsoo"
  - "Scheel, Mark A."
  - "Throwe, William"
  - "Vu, Nils L."
jref: "Class.Quant.Grav. 40, 245014 (2023)"
doi: "10.1088/1361-6382/ad08f7"
date: 2023-06-07
arxiv: "2306.04755"
abstract: |
  We present an adaptive-order positivity-preserving conservative
  finite-difference scheme that allows a high-order solution away from
  shocks and discontinuities while guaranteeing positivity and
  robustness at discontinuities. This is achieved by monitoring the
  relative power in the highest mode of the reconstructed polynomial
  and reducing the order when the polynomial series no longer
  converges. Our approach is similar to the multidimensional optimal
  order detection strategy, but differs in several ways. The approach
  is a priori and so does not require retaking a time step. It can
  also readily be combined with positivity-preserving flux limiters
  that have gained significant traction in computational astrophysics
  and numerical relativity. This combination ultimately guarantees a
  physical solution both during reconstruction and time stepping. We
  demonstrate the capabilities of the method using a standard suite of
  very challenging 1d, 2d, and 3d general relativistic
  magnetohydrodynamics test problems.
---
