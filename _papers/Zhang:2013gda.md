---
title: "Joint approach for reducing eccentricity and spurious gravitational radiation in binary black hole initial data construction"
authors:
  - "Fan Zhang"
  - "Béla Szilágyi"
jref: "Phys. Rev. D 88, 084033 (2013)"
doi: "10.1103/PhysRevD.88.084033"
date: 2013-10-22
arxiv: "1309.1141"
used_spec: true
insp_recid: 1252712
abstract: |
  At the beginning of binary black hole simulations, there is a pulse
  of spurious radiation (or junk radiation) resulting from the initial
  data not matching astrophysical quasi-equilibrium inspiral
  exactly. One traditionally waits for the junk radiation to exit the
  computational domain before taking physical readings, at the expense
  of throwing away a segment of the evolution, and with the hope that
  junk radiation exits cleanly. We argue that this hope does not
  necessarily pan out as junk radiation could excite long-lived
  constraint violation. Another complication with the initial data is
  that it contains orbital eccentricity that needs to be removed,
  usually by evolving the early part of the inspiral multiple times
  with gradually improved input parameters. We show that this
  procedure is also adversely impacted by junk radiation. In this
  paper, we do not attempt to eliminate junk radiation directly, but
  instead tackle the much simpler problem of ameliorating its
  long-lasting effects. We report on the success of a method that
  achieves this goal by combining the removal of junk radiation and
  eccentricity into a single "joint-elimination" procedure. This
  approach has the following benefits: (1) We do not have to contend
  with the influence of junk radiation on eccentricity measurements
  for later iterations of the eccentricity reduction procedure. (2) We
  re-enforce constraints periodically by invoking the initial data
  solver, removing the constraint violation excited by junk radiation
  previously. (3) The wasted simulation segment associated with the
  junk radiation's evolution is absorbed into the eccentricity
  reduction iterations. Furthermore, (1) and (2) together allow us to
  carry out our joint-elimination procedure at low resolution, even
  when the subsequent "production run" is intended as a high
  resolution simulation.
---
