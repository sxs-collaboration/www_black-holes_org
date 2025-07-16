---
---

# Binary black hole scattering with SpEC

What happens when high-velocity black holes hurtle past each other in a close encounter, deflecting through spacetime but never merging? Our [latest preprint](https://arxiv.org/abs/2507.08071) (led by [Oliver Long](https://oliverlong.info/)) presents the first simulations of black-hole scattering generated using [the Spectral Einstein Code (SpEC)]({{ site.baseurl }}{% link for-researchers/spec.md %}).

{% include image.html class="right"
   url="/images/posts/spec-scattering/Trajectories.png"
   description="Figure 1: A modified version of Figure 1 from the paper showing
      trajectories of unbound binary black hole systems including 
      equal mass, non-spinning (upper left), unequal masses (upper
      right), aligned spin (lower left), and anti-aligned spin 
      (lower right)." 
%}

We simulated 60 unbound binary black hole encounters, covering systems with spinning black holes and mass ratios up to 10. A few examples of these trajectories are shown in Figure 1.

How do the SpEC results compare with those from other codes? Figure 5 in the paper shows a comparison between SpEC and the Einstein Toolkit (ETK) for a set of equal mass, non-spinning systems. Both codes agree to less than a percent!

We also explored systems with broken symmetry. The first has black holes with spin in opposite directions. Here, for the first time, we measure the tiny difference in scattering angle of each black hole—only 0.1°! Another type of system we looked at was when the black holes have different masses. Again, we measure a difference in the scattering angle of approximately 1°. The results from both of these sets of simulations are shown below.

We also compared our Numerical Relativity results with predictions from effective-one-body models. In general, the models agree with the scattering angles generated with SpEC, with Figure 6 in the paper showing that most models differing by less than 3% in the very strong field!

{% include image.html
   url="/images/posts/spec-scattering/AsymAngles.png"
   description="Figure 2: A modified, combined version of Figures 5 and 11 
      from the paper showing scattering angle results for 
      anti-aligned spin (left) and unequal masses (right). The 
      top panels show the scattering angle result for the individual
      black holes. The lower panels show the difference between the 
      scattering angles of each black hole." 
%}