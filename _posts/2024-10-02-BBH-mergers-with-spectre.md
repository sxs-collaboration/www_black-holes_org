---
---

# First binary black hole inspiral, merger, ringdown with SpECTRE

We now have the first complete binary black hole inspiral, merger, &
ringdown using our next-generation code SpECTRE!  [Our preprint
[arXiv:2410.00265]](https://arxiv.org/abs/2410.00265) presenting this
first complete BBH simulation was led by Kyle Nelli (grad student at
Caltech) and Geoffrey Lovelace (professor at CSU Fullerton).

{% include image.html class=""
   url="/images/posts/first-spectre-BBH/splash.jpeg"
   description="Top left: A visualization of the computational domain
   and two distorted apparent horizons. Top right: Top-down tracks of
   the centers of two apparent horizons, spiraling inward as two black
   holes lose energy by emitting gravitational waves. Bottom: The
   gravitational-wave strain (in two polarizations) as a function of
   time, showing the characteristic chirp signal."
%}

These are the first gravitational waveforms from a binary black hole
merger using discontinuous Galerkin methods; done in [our open-source
SpECTRE NR code](https://spectre-code.org/). Our previous code, SpEC,
uses spectral methods. The difference?

{% include image.html class="right"
   url="/images/posts/first-spectre-BBH/DG.jpg"
   description="A graphical depiction of two neighboring DG elements,
   showing an allowed discontinuity at their interface, and a flux
   between them."
%}

Spectral methods are very efficient for modeling BBH spacetimes
because the spacetime metric is smooth. But we also need to be able to
parallelize our problem so it can run on larger supercomputers. That’s
where discontinuous Galerkin shines.

The discontinuous Galerkin method lets us to break our computational
domain into smaller chunks that can each be worked on
independently. When a problem is smooth, DG converges exponentially
like spectral. With discontinuities, DG acts like finite element.

<br clear="all">

{% include image.html class="left"
   url="/images/posts/first-spectre-BBH/domain-inspiral.jpg"
   description="The subdomain decomposition for the inspiral problem."
%}

{% include image.html class="right"
   url="/images/posts/first-spectre-BBH/domain-ringdown.jpg"
   description="The subdomain decomposition for the ringdown problem."
%}

In our paper we simulated an equal mass non-spinning BBH through 18
orbits of insprial, merger, and ringdown. We show that our simulations
are correct by running at multiple resolutions and demonstrating that
the gravitational waves approach the same answer. Convergence!


{% include image.html class="left"
   url="/images/posts/first-spectre-BBH/convergence1.jpg"
   description="A gravitational waveform; its magnitude; the
   fractional difference in amplitude between three successive
   resolutions, demonstrating convergence; and the difference in phase
   between three successive resolutions."
%}

{% include image.html class="right"
   url="/images/posts/first-spectre-BBH/convergence2.jpg"
   description="The constraint energy for three different resolutions,
   demonstrating convergence."
%}

<br clear="all">

The gravitational waves are extracted with Cauchy-Characteristic
Evolution (CCE) in which the metric is actually evolved all the way
out to future null infinity!


{% include image.html class="right"
   url="/images/posts/first-spectre-BBH/CCE.jpg"
   description="A conformal(ish) diagram with a null foliation
   extending out to future null infinity. In the bulk are two purple
   lines spiraling around each other, suggesting a pair of
   inspiralling black holes."
%}

For future work, we plan on optimizing our code, enabling adaptive
mesh refinement, and pushing the parameter space of simulations we can
do with SpECTRE.

If you want to help out, remember that [SpECTRE is open
source](https://spectre-code.org/)! For all the details, read [our
preprint [arXiv:2410.00265]](https://arxiv.org/abs/2410.00265).
