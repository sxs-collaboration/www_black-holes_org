---
title: "Eccentricity reduction for quasicircular binary evolutions"
authors:
  - "Habib, Sarah"
  - "Scheel, Mark A."
  - "Teukolsky, Saul A."
jref: "Phys.Rev.D 111, 084059 (2025)"
doi: "10.1103/PhysRevD.111.084059"
date: 2024-10-07
arxiv: "2410.05531"
insp_recid: 2838419
used_spec: true
used_spectre:
abstract: |
  Simulation of quasicircular compact binaries is a major goal in
  numerical relativity, as they are expected to constitute most
  gravitational wave observations. However, given that orbital
  eccentricity is not well defined in general relativity, providing
  initial data for such binaries is a challenge for numerical
  simulations. Most numerical relativity codes obtain initial
  conditions for low-eccentricity binary simulations by iterating over
  a sequence of short simulations—measuring eccentricity mid-evolution
  and correcting the initial data parameters accordingly. Eccentricity
  measurement depends on a numerically challenging nonlinear fit to an
  estimator model, and the resulting eccentricity estimate is
  extremely sensitive to small changes in how the fit is performed. We
  have developed an improved algorithm that produces more consistent
  measurements of eccentricity relative to the time window chosen for
  fitting. The primary innovations are the use of the nonlinear
  optimization algorithm, variable projection, in place of more
  conventional routines, an initial fit parameter guess taken from the
  trajectory frequency spectrum, and additional frequency processing
  of the trajectory data prior to fitting.
---
