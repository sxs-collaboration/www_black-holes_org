---
title: Why Numerical Relativity?
subtitle: Calculating Physics
joomla_id: 39
joomla_url: why-numerical-relativity
date: 2013-04-15 06:52:55.000000000 +00:00
paginate_from_menu: true
---

Einstein gave us a beautiful, and — in some sense — very elegant
description of physics with his equation
\\[
G = 8πT.
\\]
This basic equation encodes all of gravity; it forms the most
essential piece of the puzzle in any understanding of the physical
world. In principle, if we know everything on both sides of this
equation at one moment in time, we can use it figure out everything at
*all* moments in time. That is, we can figure out what the shape of
spacetime is, where all the matter is, and where it is
going. Unfortunately, this elegant form of the equation is almost
completely useless for doing calculations. In order to accomplish
anything, a physicist intending to use Einstein's Equations must begin
a very complicated analysis, involving huge amounts of algebra and
calculus.

### The Difficulties of Solving Einstein's Equations

For most problems, physicists need to use the same equation above in a
fuller form. There are ten distinct equations that come out of
this. By using a few abbreviations, we can make things look
comparatively nice, and fit this more full form on one page. (See the
box below.) Conceptually, the equations just describe the change in
the metric from point to point. They do it in a pretty complicated
way, though. Unfortunately, this is how Einstein's equations must be
used if we want to tackle real-world problems and figure out actual
answers with them.

To write the *easy* form of Einstein's equations, we first define a
new set of numbers:
<div>\[
\Gamma^\alpha_{\beta\gamma} = \frac{1}{2}\sum_{\delta =x,y,z,t}g^{\alpha \delta }\biggl(\frac{\partial g_{\delta\beta}}{\partial x^{\gamma}} + \frac{\partial g_{\delta\gamma}}{\partial x^{\beta}}-\frac{\partial g_{\beta\gamma}}{\partial x^{\delta}}\biggr)
\]</div>
The Greek letters $$\alpha$$, $$\beta$$, $$\gamma$$, and $$\delta$$ can each be replaced by any of the letters $$x$$, $$y$$, $$z$$, or $$t$$. The $$\Sigma$$ symbol is a sum. The symbol $$g^{\alpha \delta }$$ is essentially the same thing as the metric, $$g_{\alpha \delta }$$, but with slightly different numbers. Terms like $$\frac{\partial g_{\delta\beta}}{\partial x^{\gamma}}$$ represent the change in the metric from point to point along the lines of our coordinate grid. With this definition, Einstein's equations become
<div>\begin{align}
8πT_{\alpha\beta} = & \sum_{\delta} \Bigg[\frac{\partial\Gamma^\delta_{\alpha\beta}}{\partial x^\delta} - \frac{\partial\Gamma^\delta_{\delta\beta}}{\partial x^\alpha} + \sum_{\gamma} (\Gamma^\delta_{\alpha\beta} \Gamma^\gamma_{\delta\gamma} - \Gamma^\delta_{\gamma\beta} \Gamma^\gamma_{\delta\alpha})\Bigg] \\
& - \frac{1}{2} g_{\alpha\beta} \sum_{\delta}\sum_{\gamma} \Bigg\{g^{\delta\gamma}\sum_{\mu} \Bigg[ \frac{\partial\Gamma^\mu_{\delta\gamma}}{\partial x^\mu} - \frac{\partial\Gamma^\mu_{\mu\gamma}}{\partial x^\delta} + \sum_{\gamma} (\Gamma^\mu_{\delta\gamma} \Gamma^\nu_{\mu\nu} - \Gamma^\mu_{\nu\gamma} \Gamma^\nu_{\mu\delta})\Bigg] \Bigg\}
\end{align}</div>
Since the Greek letters are standing in for real letters, there are
actually sixteen copies of these equations! Granted, six of those are
unnecessary, but that's still a lot of equations. And, we're using
abbreviations. To write all of these ten equations out in terms of the
metric alone - without any abbreviations - would take roughly a
hundred pages! If this doesn't seem very "easy" to you, you are not
alone.

Now, in some situations, these complicated equations can be
simplified. For instance, if we are looking at empty space with no
matter in it, the Stress-Energy tensor (the $$T$$ above) disappears,
so one side of Einstein's equations is just zero. If the Universe is
the same in every direction, no matter which way you look, all but two
of Einstein's equations disappear. In many interesting physical
situations, these types of simplifications are good enough to describe
the real Universe quite well. These tricks allow us to understand what
must have happened following the Big Bang.

The space around a quiet, non-spinning Black Hole is simple enough
that it was first analyzed and understood by a German soldier serving
on the Eastern front during World War I, just months after Einstein
introduced his equations to the world. Conditions were grim; the
soldier died shortly after writing to Einstein describing his
discovery. Nonetheless, he was able to solve Einstein's Equations in
these circumstances, using just pencil and paper.

If gravity is weak, most of the terms in Einstein's equations are
quite small, and so can be ignored. This — along with the knowledge of
a few more tricks — allows us to analyze gravitational waves with
Einstein's equations. The analysis is not perfect, since it is only an
approximation, but it is a very precise approximation, and the errors
from the perfect solution are tiny.

Of course, not all of Nature is quite so simple. If we want to know
what Einstein's equations say about two black holes with different
masses falling into each other, for example, we have to use every one
of the terms in all ten of the equations. There are no simplifications
that Nature will respect in this case. In this state of affairs,
Relativity as a tool for understanding interesting physics seems
hopelessly lost. There are too many equations, with far too many
terms, for any human to even keep track of — never mind solve.

### The Initial-Value Formulation and Computers to the Rescue

In their form above, Einstein's equations have to be solved everywhere
throughout spacetime, all at once. Thankfully, methods have been found
which allow us to just solve on one slice of space (no time), and them
step forward in time from there.

### The Achievements Possible with Numerical Relativity

Templates for GW observatories make these observations possible. New
physics, bringing us greater understanding of the implications of
Einstein's equations.
