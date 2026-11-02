---
---

# Getting gravitational waveforms right from the start

Gravitational waves travel hundreds of millions to billions of light-years
before reaching our detectors. Numerical simulations of merging black holes,
however, cover only a finite region around them. To predict the signal
far away, we hand data from the simulation to a second calculation that carries
the radiation all the way to infinity.

But the simulation alone cannot get this calculation started: it needs the
radiation everywhere from the edge of the simulation out to infinity, at the
moment the simulation begins. How can we reconstruct data that the simulation
cannot provide? Our
[new Letter](https://arxiv.org/abs/2610.30263) and
[companion study](https://arxiv.org/abs/2610.30268), led by
[Guido Da Re]({{ site.baseurl }}{% link about-sxs/people.markdown %}), address
this longstanding obstacle to producing accurate gravitational waveforms at
infinity.

This second calculation is called Cauchy-characteristic evolution (CCE). It
solves Einstein's equations along surfaces traced out by outgoing light rays,
using coordinates that bring infinity onto a finite computational grid. CCE is
the more complete method: the simpler alternative, extrapolating waveforms
measured at several distances, does not correctly recover every part of the
signal. It struggles, for example, with gravitational-wave memory, a permanent
change in the separation of freely falling objects after a wave passes.

{% include image.html class="right"
   url="/images/posts/cce-initial-data/schematic.png"
   description="Figure 1: Connecting a black-hole simulation to infinity. The
     original simulation (left) passes data through a sphere surrounding the
     black holes to the characteristic evolution (right), which carries the
     radiation outward along light rays. The characteristic evolution also
     needs its own initial data (orange), including outgoing waves (blue) and
     radiation scattered back inward (green). These must be reconstructed
     using information from the original simulation at the red point."
%}

The initial radiation field that CCE needs includes both outgoing waves and
radiation scattered back inward by spacetime curvature. This scattered
radiation carries information about the system's past. The key insight is that
the initial radiation field and the coordinates used to describe it must be
chosen together. Earlier approaches prescribed the coordinates separately,
introducing unintended radiation into the initial data.

By providing inconsistent initial data, these approaches could even create
gravitational waves around a single stationary black hole that should not
radiate at all. In binary simulations, the artificial radiation contaminates the
signal for several wave cycles. Our method instead derives the coordinates from
the radiation field itself, which we reconstruct from the original simulation's
data while retaining the contribution from waves scattered back inward.

<br style="clear:both">

{% include image.html class=""
   url="/images/posts/cce-initial-data/waveform.png"
   description="Figure 2: Recovering the waveform from the start. In the upper
     panel, the new initialization (green) closely follows the post-Newtonian
     prediction (black circles), while the previous initialization (orange,
     dashed) produces artificial oscillations. The extrapolated waveform is
     shown in blue. Lighter and darker curves correspond to nearer and farther
     outer boundaries; moving the boundary outward reduces the small remaining
     wiggle in the new waveform. The lower panel shows the wave and its
     amplitude, with a box marking the region enlarged above."
%}

We implemented the method in [SpECTRE](https://spectre-code.org) and tested it
on black-hole simulations produced with the
[Spectral Einstein Code]({{ site.baseurl }}{% link for-researchers/spec.md %})
(SpEC). Figure 2 shows an equal-mass, nonspinning binary. With the previous
initialization, the amplitude of the waveform's dominant component oscillates
artificially by about 10% for several wave cycles. With the new initial data,
this oscillation disappears, and from the very first cycle the waveform follows
the post-Newtonian prediction, an analytic approximation valid while the black
holes are far apart. The small oscillations that remain come from the original
simulation's outer boundary.

The improvement also extends to faint signals long after merger. After a
head-on black-hole collision, for example, the radiation does not stop when the
final black hole settles down: a weak tail remains, decaying slowly as a power
law. With the previous initialization, this tail was buried under artificial
radiation. The new initial data recover the expected decay, as shown in Figure 8
of the companion study.

These improvements can be applied to existing simulations with suitable stored
boundary data, without repeating their expensive spacetime evolutions. The
method does not depend on the particular approach used to solve Einstein's
equations in the original simulation, opening a path to recovering accurate CCE
waveforms from the present simulations archives.

This work lays the foundation for improved waveform catalogs
based on CCE. These catalogs will support more accurate models for interpreting
gravitational-wave observations and for using them to study black-hole
populations, test general relativity, and measure cosmic expansion.
