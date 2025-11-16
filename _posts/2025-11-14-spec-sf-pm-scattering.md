---
---

# Probing perturbative scattering with SpEC

How much information can we gain by pushing numerical relativity to its limit by simulating black hole scattering encounters when one is much larger than the other or when they are far apart and only weakly interacting?  Our [latest preprint](https://arxiv.org/abs/2511.10196) (led by [Oliver Long](https://oliverlong.info/)) explores these extreme regions of the black-hole scattering parameter space using simulations generated using the [Spectral Einstein Code]({{ site.baseurl }}{% link for-researchers/spec.md %}) (SpEC).

{% include image.html class="right"
   url="/images/posts/spec-sf-pm-scattering/SFAvgFits.png"
   description="Figure 1: A modified version of Figure 3 from the paper showing how the extracted self-force agrees with the SpEC results. The top panel shows the scattering angle against symmetric mass ratio and the bottom shows the difference between the self-force extractions and the SpEC values."
%}

First, we use simulations from our [previous paper](https://arxiv.org/abs/2507.08071) to explore black hole systems with mass ratios up to 1:10. By fitting a simple polynomial to the scattering angle from the NR simulations we can extract the self-force, which measures how much the small body's mass affects its own orbit. As self-force formalism expands in the small mass ratio of the system, we expect it to be more accurate for larger differences in the masses of the two black holes. We find that we can reliably extract up to second-order self-force effects, which corresponds to the term proportional to the square of the symmetric mass ratio in the self-force expansion. Figure 1 shows that with this information we can perfectly recover the scattering angles to within the numerical relativity errors, even at equal mass where the expansion should break down completely!

{% include image.html class="left"
   url="/images/posts/spec-sf-pm-scattering/PMComp.png"
   description="Figure 2: A modified version of Figure 5 from the paper showing the agreement between the various orders of the post-Minkowskian (PM) expansion and the SpEC results. The top panel shows the scattering angle against impact parameter and the bottom shows the difference between the post-Minkowskian values and the SpEC results. The inset is a zoom in on the weakest-field data points."
%}

Next, we turn to the weak-field case where the black holes are barely interacting. We generated 9 new simulations where the black holes were further apart than ever simulated before. We then compared these results to those of the post-Minkowskian formalism, where the trajectories of the black holes are calculated as deviations from a straight line. These calculations are very interesting as they apply highly advanced methods from scattering amplitudes in particle physics to the general relativistic problem. The latest results even made it onto the cover of [Nature](https://www.nature.com/nature/volumes/641/issues/8063)! Figure 2 shows that when we get into the weak-field, the post-Minkowskian calculations fall within the errors of the numerical relativity results which provides strong evidence that both approaches give the correct answer!

Overall, this paper highlights the power of using numerical relativity simulations as a tool to both validate and inform perturbative methods in the study of binary-black-hole dynamics and will lead to many exciting applications in the future!