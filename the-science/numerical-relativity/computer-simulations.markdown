---
layout: post
title: Computer Simulations
joomla_id: 40
joomla_url: computer-simulations
date: 2013-04-15 06:57:49.000000000 +00:00
---

## Giving the Problem to a Computer, to Work Out the Details

To take another example that might be familiar from high school —
Physics class, this time — we look at the motion of an apple falling
from a tree. First, imagine that the apple is set moving, but there is
no gravity pulling it down. Newton says that its velocity would be a
constant (if we ignore air resistance). Now we need to think carefully
about what this means for the position of the apple at different
instants of time. Velocity tells us how far something will move in a
given amount of time. If we take some length of time, then the
distance the apple will move in that length of time is just the
velocity multiplied by the time:

**distance = velocity × time**.
{: .equation }

This is a familiar formula, that we might use to figure out how far we can drive in a given amount of time, for example. But the formula assumes that the velocity is constant. To include gravity, we need to account for the changing velocity, which means that the formula above doesn't apply. Fortunately, there is a very similar formula for the accelerated case. To make it a little more clear, we just rewrite the formula above as


**change in position = velocity × time**.
{: .equation }

Acceleration tells us how much the velocity changes in a given amount
of time. By analogy, then, we can write

**change in velocity = acceleration × time**.
{: .equation }

Now, because the acceleration is constant, there is a trick we can use
to find the distance the apple falls in this amount of time: we need
to use the average velocity. If the initial velocity was zero, and the
final velocity is (**acceleration × time**), then the average velocity
is (**½ × acceleration × time**), so

**change in position = (½ × acceleration × time) × time**.
{: .equation }

In some sense, we have now solved this problem once and for all. Given
a starting point, this formula shows us where the apple will be at any
later time. We can show what the apple's path looks like: {First
animation, showing the apple smoothly accelerating.}

### Putting It On a Computer

This classic example from basic Physics is instructive in its own
right. However, not all problems are quite so easy to solve. Imagine
the we drop the apple a long distance from the Earth, and watch as it
falls very far. We would see the force of gravity on the apple change,
since gravity is stronger, the closer the apple comes to Earth. In
this case, it would be much more difficult to write down a formula for
the position of the apple, like the last one above. There are, in
fact, tricks to figure out this problem, but suppose we are lazy, and
just want a computer to do it for us. All we could tell the computer
for sure would be the rule

**change in velocity = acceleration × time**.
{: .equation }

Here, the acceleration depends on the apple's position, and — hence —
on time. Notice that if the amount of time is very small, the change
in velocity will be correspondingly very small, so the velocity would
be approximately constant during that time period. In that case, we
can use the rule that says

**change in position = velocity × time**.
{: .equation }

The computer could start out at the initial velocity and the initial
position, where it knows the acceleration. It could then move a tiny
amount according to rule 2. Then, it could adjust the velocity
according to rule 1, using the new position, and the new
acceleration. Then repeat, over and over. This is just the same trick
that we mentioned in the section on geodesics. If the path of the
apple is smooth (which it is) we can just take many tiny, tiny steps,
and end up at the right point.

There is just one problem with using this technique on a computer. If
we take a large step, the velocity will be far from constant, so we
will introduce some error by making this approximation. The larger the
step is, the larger the error will be. To get exactly the right path,
we need to take an infinite number of infinitely small
steps. Computers may be much faster than humans at figuring these
things out, but they're not infinitely fast. That means the computer's
version of the path won't quite be the right one. The smaller the
steps, the closer it will be. On the other hand, the smaller the
steps, the longer it will take the computer to finish. This will
always be a trade-off when giving this sort of problem to a computer.

We can try out this method. Click on the animation below to watch as
the apple moves in discrete steps. As the computer computes where to
put the apple, we can see the size of its errors by comparing to the
correct solution, shown by the faint apples in the background. Move
the slider around to adjust the size of the time steps. Note that
making the time steps smaller brings the apples closer and closer to
the correct solution. {Second, interactive animation, showing the
apple moving in discrete steps.}

### Simulating Relativity

Relativity provides us with perfect examples of problems that really
are too difficult (as far as we can tell) to figure out with any
clever tricks. In this case, the quantities in which we are interested
are not the position or velocity of an apple, but the size of the
numbers in the metric. For example, at a given point in space, the
metric component $$g_{xx}$$ will have a certain value. This value will
change in time, just as the apple's position changes in time. Of
course, the problem is not nearly so simple. At a given point in
space, we have ten metric components, which is like having ten apples
at each point in space. We also have many, many points in space, which
leaves us with all ten components at each point in space — like having
ten apples at every point in space, and trying to keep track of all of
them. Each of these components has an effect on those near it. Using
Einstein's Equations, we can take all these complications (and many
more), and leave them to a computer to figure them out.
