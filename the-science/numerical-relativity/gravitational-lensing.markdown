---
title: Gravitational Lensing
joomla_id: 176
joomla_url: lensing
date: 2014-11-05 14:50:52.000000000 +00:00
paginate_from_menu: true
---

{% include image.html class="small-right"
   url="/images/lensing/LightDeflection.jpg"
   description="Light deflection"
%}

An interesting prediction of general relativity is that light does not
just travel in a straight line, but its path is bent by
gravity. Gravitational lensing is the name for the bending of light by
gravity, as the source of gravity (e.g. a galaxy) acts as a physical
lens which bends the light. There is ample observational evidence of
these deflections of light by massive bodies, including measuring the
deflection of starlight passing near the Sun. However, the largest
observed deflection of light is only very slight, around 11 arc
seconds or 0.003 degrees.

The SXS Lensing group is interested in much more eXtreme deflections
of light. Near black holes, the most compact objects in the universe,
light can be so strongly bent by gravity that it can orbit many times
around the black hole before making it to your eye. In theory, there
is no limit to the number of times a light ray can orbit the black
hole. Even though black holes emit no light themselves, their effect
on light passing nearby leads to some stunning visual and mathematical
results!

## Single black hole

{% include image.html class="captionless left"
   url="/images/lensing/ParaFlat.png"
   description="Milky Way - Star rendering code"
%}

We have written code to produce images of stars from a star catalog,
such as the [2MASS catalog](http://www.ipac.caltech.edu/2mass/). We
take each star's location and its [magnitude in different color
bands](http://en.wikipedia.org/wiki/Photometric_system) from the
catalog. To generate the image, we need to know from where light
enters each pixel of the camera as well as the redshift of the
light. More details are provided in [our
paper](http://arxiv.org/abs/1410.7775). This is an image showing the
Milky Way using our star rendering code.

With our camera pointing in the same direction as the previous image,
we now see how a black hole affects light from these stars.  The first
feature that pops out is a large circular shadow in the center of the
image.  This is called the shadow of the black hole, because it is a
region where the black hole prevents light from reaching the camera,
such that the black hole is casting a shadow on the image.

Near the borders of the image, light from the stars is slightly
deflected. Notice the dark patches where there aren't many stars in
the lower right portion of the original image. These appear to be
located near the lower right corner of the image now, due to the
gravity of the black hole. This is analogous to the light being
deflected around the sun, making a star's apparent position somewhere
else, as depicted earlier.

{% include image.html class="captionless right"
   url="/images/lensing/ParaSchwarzschild.png"
   description="black hole affects light from stars"
%}

Light passing closer to the shadow is being deflected even more by the
black hole.  There is a large ring structure around the shadow called
an [Einstein ring](http://en.wikipedia.org/wiki/Einstein_ring).  This
is where light from directly on the opposite side of the black hole is
deflected around the hole on its way to the camera.  It makes a ring
due to the symmetry, but we even see such a ring in cases where the
black hole has spin.  Roughly in the center of the original image,
there is a bright blue star near an orange one.  This is almost
directly behind the black hole, so it is very close to the Einstein
ring.  You may have noticed that we can see two images of both of
these stars, one at about 1:30 inside the Einstein ring, and one at
about 7:30 on the outside of the ring.  In fact, inside the Einstein
ring, we can see an image of the rest of the galaxy!  Light from
behind the camera, for example, can take a path halfway around the
black hole on the way to the camera.

Although it is hard to see, very close to the shadow there is a bright
ring.  This is actually the second Einstein ring, corresponding to
light from directly behind the camera.  In fact, there are an infinite
number of these Einstein rings in theory, but we can only resolve two
of them in this particular image.

## Binary black hole

While lensing by a single black hole has been studied for quite a long
time, no one had previously known what astrophysically interesting
binary black holes would actually look like.  The problem is
complicated significantly by having to solve what happens to two black
holes orbiting each other.  The SXS collaboration uses the Spectral
Einstein Code (SpEC) to simulate these kinds of compact object
mergers, be it with black holes or neutron stars with high accuracy.
With SpEC, the SXS Lensing group is in a unique position to explore
what a binary black hole merger would look like.

In the following video, we see the last three orbits of a three to one
mass ratio binary with arbitrarily chosen spins on both black holes.
The details of this merger can be found in [Taylor *et
al.*](http://journals.aps.org/prd/abstract/10.1103/PhysRevD.88.124010)
as case 4.  The stars used are the same as the ones used in the single
black hole image above.  The camera is located above the orbital plane
of the binary looking down.

{% include youtube-embed.html id="Qg6PwRI2uS8" %}

{% include image.html class="captionless right"
   url="/images/lensing/ParaHighRes.png"
   description="3 to 1 mass ratio binary: Face-on"
%}

We see an Einstein ring surrounding both masses.  This is not general,
however.  When the black holes are separated by a large distance
spatially, we could see an Einstein ring around each black hole
individually.  Near both shadows we see a smaller shadow, which is
called an eyebrow due to its shape.  These secondary shadows
correspond to one black hole casting a shadow which is lensed by the
other black hole on the way to the camera.  [Our
paper](http://arxiv.org/abs/1410.7775) explores these smaller shadows
in more detail, finding that there are in fact an infinite number of
these shadows, but we can only resolve a few in this video.

After the merger, the shadows transition to a single shadow and the
background deflections settle to a stationary state which looks like
the lensing by a single black hole.  This matches our expectations.
After black holes have merged, there is a ringdown phase, where energy
is radiated from the black hole until it settles to a stationary
single black hole solution.

We have another viewpoint of this merger, shown below.  The opening
angles of the cameras were slightly different for this video, so we
also provide what the background stars would look like with these new
parameters.

{% include image.html class="captionless"
   url="/images/lensing/PerpFlat.png"
   description="Milky Way - Star rendering code"
%}

{% include youtube-embed.html id="ENd8Sz0AFOk" %}

{% include image.html class="captionless right"
   url="/images/lensing/PerpHighRes.png"
   description="3 to 1 mass ratio binary: Edge-on"
%}

In this video, the camera is essentially located in the orbital plane
of the binary.  This is what we call an "edge-on" view.  As the black
holes orbit, one black hole passes behind the other relative to the
camera.  As this happens, the shadow cast by the farther black hole is
lensed by the closer black hole into a ring-like shadow.
Additionally, we can see the effect that the arbitrary spins has on
the orbit.  The orbital plane precesses visibly in these last three
orbits before merger.  As before, we see that the lensing settles down
to look like lensing by a single black hole.

We have some interesting brightness effects which are more apparent
from this viewpoint than the previous video's viewpoint.  Some photons
passing through the binary system have accumulate non-unity redshift.
The brightness is affected by the redshift by a factor of redshift
cubed, so there is a large brightness change for only a small redshift
difference.  Overall, near the left side of the shadows we see the
brightness damped significantly, while on the right side we see
flashes of brightness!

## Black holes at Cornell

{% include image.html class="captionless left"
   url="/images/lensing/Clocktower/ClockTower.png"
   description="Clock tower"
%}

While looking at black holes in front of a field of stars, it is easy
to lose your bearings.  In [our
paper](http://arxiv.org/abs/1410.7775), we frequently color sections
of the sky with a grid to more easily understand the deflection of
light by the black holes.  A more fun way to accomplish this is by
using a recognizable image.  Instead of using stars, we therefore use
a picture of the clock tower at Cornell.

Now we stick a black hole on campus, because we can and it's awesome.
We can see clearly that near the edges of the image, the view of
campus is only slightly changed.  The image of the clock tower is bent
slightly.  However, inside the Einstein ring, we can see the size of
the deflections grows.  The image is also inverted.  The clock tower
here is on the left and is upside down, in addition to being even more
bent.  The grass is up and the sky is down inside the Einstein ring.

Now is a good time to remind you that light can be deflected all the
way around the black hole.  To properly see what a black hole on
campus would look like, we need not only an image of what's in front
of the camera, but also directly above and below the camera.  Even
light from directly behind the camera will get deflected around the
black hole on its way to the camera!  Light-rays can take paths which
orbit many times around the black hole before reaching the camera,
resulting in an infinite number of clock towers (if you had an
infinite resolution camera to see them)!

{% include image.html class="captionless left"
   url="/images/lensing/Clocktower/ClockTower_BH.png"
   description="Black hole in front of clock tower"
%}
{% include image.html class="captionless right"
   url="/images/lensing/Clocktower/ClockTower_Para.png"
   description="Black hole in front of clock tower"
%}

If we can put one black hole on campus, why not two?  This is the same
binary discussed in the Binary black hole section.  It is a three to
one mass ratio binary.  The same discussion of an infinite number of
black hole shadows applies here as well.
