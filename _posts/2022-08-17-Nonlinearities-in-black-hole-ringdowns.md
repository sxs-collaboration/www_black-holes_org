---
---

# Nonlinearities in black hole ringdowns

With our [latest preprint
[arXiv:2208.07380]](https://arxiv.org/abs/2208.07380) (led by Caltech
grad student Keefe Mitman), SXS simulations have conclusively shown
the presence of nonlinearities in black hole ringdowns. What does it
all mean?

This paper is about modeling the ringdown portion of gravitational
waves (GWs) from black holes. After two black holes merge, the
highly-distorted remnant BH "rings down" to the stationary Kerr
solution. During this time, the GWs are approximately a sum of damped
sinusoids (blue arrow in this figure).

{% include image.html class=""
   url="/images/posts/nonlinear-ringdown/IMR-annotated.jpeg"
   description="The inspiral, merger, and ringdown of GW150914
   [Phys. Rev. Lett. 116, 061102 (2016)]."
%}

The damped sinusoid model comes from linear perturbation theory—assume
we can write spacetime as the nonlinear Kerr solution, plus a small
correction that satisfies a *linear* equation. We physicists love
perturbation theory! But usually we need to go to 2nd and higher
order.

In the standard model, people have gone up to 10th order (5 loops). In
post-Newtonian theory (used for the inspiral gravitational wave),
people are working on 4.5PN \\((1/c^9)\\). So what about ringdown?

{% include image.html class="right-third"
   url="/images/posts/nonlinear-ringdown/loop-diagrams.png"
   description="An example of loop diagrams in QFT. More loops is
   higher order in perturbation theory."
%}

Almost everybody still uses linear theory for ringdown (there's been a
little work on how to do second order). In fact there's been claims
that you can fit even the peak—when nonlinearities should be
largest—by just adding more "overtones" (linear solutions that decay
faster).

An [earlier SXS paper](https://arxiv.org/abs/2110.15922) even fit more
than 100 modes at the same time!

{% include image.html class="left"
   url="/images/posts/nonlinear-ringdown/7-overtones.jpeg"
   description="Fitting ringdown with many overtones, but still within
   linear theory [Phys. Rev. X 9, 041060 (2019)]."
%}

{% include image.html class="right"
   url="/images/posts/nonlinear-ringdown/100-modes.jpeg"
   description="The 'greedy algorithm' of [Phys. Rev. D 105, 104015
   (2022)] happily finds 100 modes to model."
%}

<br style="clear:both">

Ok, that's enough background, on to our new paper. We went looking for
a quadratic nonlinearity in ringdown, and it's there! The most
important one is the dominant linear (2,2,0) mode interacting with
itself, sourcing a response in the (4,4) mode (and others).

{% include image.html class=""
   url="/images/posts/nonlinear-ringdown/nonlinearity-main.jpeg"
   description="Fig. 1 from our new preprint, showing quadratic
   nonlinearity at various times after merger."
%}

The frequency is known from theory; we fit the amplitudes across a wide range of simulations, and find a parabola—it's really a quadratic nonlinearity (top panels).

Compare that against two different linear modes (bottom panels), no such relation.

Of course we did a bunch of checks. Are *we* overfitting? We compared
the quadratic model to a linear model with the same number of
parameters, and the quadratic one fits better (the residual and
"mismatch" are smaller). 

It's really worth pointing out that this quadratic mode decays slower
than the first linear overtone. AND the amplitude is basically the
same at the peak! Both of these features can be seen in the first
figure here:

{% include image.html class="left"
   url="/images/posts/nonlinear-ringdown/nonlin-vs-lin-1.jpeg"
   description="Comparison of nonlinear vs. linear fits. Nonlinear is
   better!"
%}

{% include image.html class="right"
   url="/images/posts/nonlinear-ringdown/nonlin-vs-lin-2.jpeg"
   description="Performance of fit as a function of start time.  The
   fits are stable, and far away from our estimated numerical error."
%}

<br style="clear:both">

In the second figure, you can see that the amplitudes are robust as we
vary the time when we start the fits, which makes us confident in our
model.

Also, we can let the frequency of our extra mode be a variable, and
see which frequency the data prefer. Turns out it's the frequency
predicted by second order perturbation theory, *not* a higher overtone
from linear theory.

{% include image.html class=""
   url="/images/posts/nonlinear-ringdown/free-freq.png"
   description="Quality of fit when the extra frequency is not
   predetermined.  The preferred frequency is close to that due to
   nonlinearity (green X), rather than a higher overtone (red
   circle)."
%}

The amplitude of the nonlinearity being similar to that of a linear
overtone might make you worry about the validity of perturbation
theory. We need a hierarchy, that 1st order is more important than 2nd
order is more important than 3rd order etc... But we don't seem to
have that here. Clearly more work to do!

Well, you're basically up to speed on what we did in the paper. If you
want all the technical details, it's an easy read—only 5 pages! Check
it out at [[arXiv:2208.07380](https://arxiv.org/abs/2208.07380)]. For
completeness, some of our colleagues (Mark Cheung et al.) have [their
own paper](https://arxiv.org/abs/2208.07374) out today with consistent
results, and some of our coauthors (Macarena Lagos and Lam Hui) have a
[longer theory paper](https://arxiv.org/abs/2208.07379) trying to
model some of these results with pencil and paper.

Special thanks to Max Isi for organizing a workshop that fired up some
of our investigations, and the Benasque science center and the NSF for
fostering some of our collaborations. There is still a lot more to
learn! We have like 3 more paper ideas based on this stuff. Stay
tuned!
