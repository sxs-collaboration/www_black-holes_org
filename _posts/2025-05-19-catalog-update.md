---
---

# Major SXS catalog update

We are excited to release a major update to our [catalog of binary black hole
simulations, available here](https://arxiv.org/abs/2505.13378).  Such
simulations are key to [LIGO/Virgo/KAGRA]({{ site.baseurl }}{% link
the-science/gravitational-wave-astronomy/a-totally-new-kind-of-observatory.markdown
%}) being able to extract science from their [gravitational wave]({{
site.baseurl }}{% link
the-science/gravitational-wave-astronomy/gravitational-waves.md %}) detections.
This catalog update comes six years after our [last
catalog](https://arxiv.org/abs/1904.04831), with too many improvements to list
here. Our catalog now has 3,756 simulations, the largest and most accurate
[numerical relativity]({{ site.baseurl }}{% link
the-science/numerical-relativity/index.md %}) catalog to date.  This data is
freely available via [our data server
(https://data.black-holes.org/)](https://data.black-holes.org/) and through the
[`sxs` package for `python`](https://sxs.readthedocs.io/). Here's a sampling of
some more extreme systems in our catalog, showcasing a lot of the physics we can
capture:

{% include image.html
   url="/images/posts/catalog-update/showoff.png"
   description="Figure 1 from our new catalog paper. We accurately capture
     precession, memory, eccentricity, and high mass ratio systems. For full
     details, see the paper."
%}


The median simulation length is 22 orbits, while the longest is 148 orbits.
Here's a visual overview of the before and after of our parameter-space
coverage:

{% include image.html
   url="/images/posts/catalog-update/corner_q_chieff_chi11perp_chi12perp_paper_before_after.gif"
   description="Parameter space coverage before and after our catalog update;
   see Fig. 2 from our new paper."
%}

{% include image.html class="right"
   url="/images/posts/catalog-update/Lev_comparison_per_ell_paper.png"
   description="Figure 7 from our new paper, showing how well different angular
   harmonics converge."
%}

Our spectral methods continue to be highly efficient---over 1,000 times more
efficient than finite-difference methods of comparable accuracy.  We always
provide multiple resolutions, so anyone can verify our numerical
convergence. Eight pages of the new paper are dedicated to studying the quality
of our waveforms! For example, one of our plots (at right) shows how well
different angular harmonics are converging (we provide all the way up to
\\(\\ell = 8 \\)). Our median waveform difference between resolutions is
\\(4\times 10^{-4}\\).

Over the years, we made many improvements to [the Spectral Einstein Code
(SpEC)]({{ site.baseurl }}{% link for-researchers/spec.md %}) that performed all
these simulations (Sec. 3 discusses our methods and some of these
improvements). More recent simulations are more accurate than older ones, and
some old simulations had issues that were only uncovered recently. Therefore
we now deprecate simulations if we need (though the old data remains
available, by passing an argument in the `sxs` package). Out of the 2,018
simulations in the last catalog paper, we deprecated 282. We added 2,020
new non-deprecated simulations (and even uploaded another 112 new but deprecated
simulations).  Because we generated so much data, we needed a new waveform
format, which is typically 6 times more compressed than before. The new format
is handled seamlessly by the `sxs` package, which also fetches and caches
waveforms (and other data) as needed.

Six years is a long time, so there are too many details to summarize here. You
can read about all of them in the [new SXS catalog
paper](https://arxiv.org/abs/2505.13378). We have already been doing a [ton of
science]({{ site.baseurl }}{% link for-researchers/spec.md %}#Publications) with
this data. We make it publicly available so everyone has high-quality binary
black hole simulation data at their fingertips for their research! Of course,
we're not done yet---there's a lot more work to do: higher mass ratios, higher
eccentricity, and meeting the accuracy requirements of next-generation
detectors. Stay tuned for the next version of our catalog!
