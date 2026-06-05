---
title: "A Note on QR-Based Model Reduction: Algorithm, Software, and Gravitational Wave Applications"
authors:
  - "Antil, Harbir"
  - "Chen, Dangxing"
  - "Field, Scott E."
jref: "Comput.Sci.Eng. 20,  (2018)"
doi: "10.1109/MCSE.2018.042781323"
date: 2018-05-16
arxiv: "1805.06124"
insp_recid: 1673395
used_spec:
used_spectre:
abstract: |
  While the proper orthogonal decomposition (POD) is optimal under
  certain norms, its also expensive to compute. For large matrix
  sizes, the QR decomposition provides a tractable alternative. Under
  the assumption that it is a rank-revealing QR (RRQR), the
  approximation error incurred is similar to the POD error;
  furthermore, the authors show the existence of an RRQR with exactly
  the same error estimate as POD. To numerically realize an RRQR
  decomposition, they discuss the (iterative) modified Gram Schmidt
  with pivoting and reduced basis methods. They show that these two
  seemingly different approaches are equivalent. They then describe an
  MPI/OpenMP parallel code that implements one of the QR-based model
  reduction algorithms analyzed, and document the codes scalability
  for large problems, such as gravitational waves, and demonstrate
  excellent scalability up to 32,768 cores and, for complex dense
  matrices, as large as 10,000x3,276,800.
---
