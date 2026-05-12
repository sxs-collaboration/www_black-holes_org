---
title: "Time-Dilation Methods for Extreme Multiscale Timestepping Problems"
authors:
  - "Hopkins, Philip F."
  - "Most, Elias R."
jref:
doi: "10.33232/001c.161464"
date: 2025-10-10
arxiv: "2510.09756"
insp_recid: 3068564
used_spec:
used_spectre:
abstract: |
  Many astrophysical simulations involve extreme dynamic range of
  timescales around 'special points' in the domain (e.g. black holes,
  stars, planets, disks, galaxies, shocks, mixing interfaces), where
  processes on small scales couple strongly to those on large scales.
  Adaptive resolution, multi-physics, and hybrid numerical methods
  have enabled tremendous progress on the spatial, physics, and
  numerical challenges involved. But often the limiter for following
  the long timescales of global evolution is the extremely short
  numerical timestep required in some subdomains (which leads to their
  dominating simulation costs). Recently several approaches have been
  developed for tackling this in problems where the short timescale
  solution is sampled and then projected as an effective subgrid model
  over longer timescales (e.g. 'zooming in and out'). We generalize
  these to a family of models where time evolution is modulated by a
  variable but continuous in space-and-time dilation/stretch factor
  $a({\bf x},\,t)$. This extends previous well-studied approaches
  (including reduced-speed-of-light and binary orbital dynamics
  methods), and ensures that the system comes to correct local steady-
  state solutions, and derive criteria that the dilation
  factor/timesteps/resolution must obey to ensure good behavior. We
  present a variety of generalizations to different physics or
  coupling scales. Compared to previous approaches, this method makes
  it possible to avoid imprinting arbitrary scales where there is no
  clear scale-separation, and couples well to Lagrangian or Eulerian
  methods. It is flexible and easily-implemented and we demonstrate
  its validity (and limitations) in test problems. We discuss the
  relationship between these methods and physical time dilation in
  GRMHD. We demonstrate how this can be used to obtain effective
  speedup factors exceeding $\gtrsim 10^{4}$ in multiphysics
  simulations.
---
