---
layout: post
title: "SpEC: Spectral Einstein Code"
date: 2025-01-04
redirect_from: /code/SpEC.html
---

# Introduction

The Spectral Einstein Code (SpEC) is a flexible infrastructure for
solving partial differential equations using multi-domain spectral
methods. While SpEC was primarily designed for fully
general-relativistic compact object simulations, it can be applied to
a wide range of hyperbolic and elliptic equations. Some of its
features are:

- A flexible domain decomposition supporting individual subdomains
  (cells, elements) of various topologies, e.g. blocks, spheres,
  cylinders, and any combination thereof. Subdomains can touch or
  overlap.
- Solves hyperbolic and elliptic PDEs.
- Interfaces to the visualization software ParaView and VisIt.

<figure class="inline-images">
    <img src="{{ site.baseurl }}/images/spec/t33.png" alt="Binary black holes early in the inspiral phase (t=33)" />
    <img src="{{ site.baseurl }}/images/spec/t7920.png" alt="Binary black holes just before merger (t=7920)" />
    <img src="{{ site.baseurl }}/images/spec/t8200.png" alt="Binary black holes at the moment of merger (t=8200)" />
    <img src="{{ site.baseurl }}/images/spec/t9000.png" alt="Binary black holes well after merger (t=9000)" />
    <figcaption>SpEC simulation of inspiral and merger of two black holes</figcaption>
</figure>

The main application area of SpEC lies in simulating compact binary
objects. Specifically, it is one of the most accurate and efficient
codes to compute the gravitational waveforms for inspiraling and
coalescing binary black holes.

# Contributors

SpEC was originally developed by
<span class="contrib-name">Lawrence Kidder</span>,
<span class="contrib-name">Harald Pfeiffer</span>,
and
<span class="contrib-name">Mark Scheel</span>,
who remain the principal maintainers of the code. Since then, many
further individuals have contributed to SpEC. Most especially,
<span class="contrib-name">Matthew Duez</span>
and
<span class="contrib-name">Francois Foucart</span>
have developed the hydrodynamics module;
<span class="contrib-name">Béla Szilágyi</span>
and
<span class="contrib-name">Dan Hemberger</span>
have made numerous valuable additions throughout the code; and
<span class="contrib-name">Lee Lindblom</span>
has contributed significantly to the algorithms used in SpEC.

The following researchers have substantially contributed to SpEC:
<span class="contrib-name">Andy Bohn</span>,
<span class="contrib-name">Michael Boyle</span>,
<span class="contrib-name">Luisa Buchman</span>,
<span class="contrib-name">M. Brett Deaton</span>,
<span class="contrib-name">Nils Deppe</span>,
<span class="contrib-name">Roland Haas</span>,
<span class="contrib-name">Francois Hebert</span>,
<span class="contrib-name">Kate Henriksson</span>,
<span class="contrib-name">Stephen Lau</span>,
<span class="contrib-name">Geoffrey Lovelace</span>,
<span class="contrib-name">Curran Muhlberger</span>,
<span class="contrib-name">Sergei Ossokine</span>,
<span class="contrib-name">Rob Owen</span>,
<span class="contrib-name">Saul Teukolsky</span>,
and
<span class="contrib-name">Will Throwe</span>.

Further contributions to SpEC were made by
<span class="contrib-name">Kevin Barkett</span>,
<span class="contrib-name">Thomas Baumgarte</span>,
<span class="contrib-name">Jonathan Blackman</span>,
<span class="contrib-name">Wyatt Brege</span>,
<span class="contrib-name">Jeandrew Brink</span>,
<span class="contrib-name">Tony Chu</span>,
<span class="contrib-name">Michael Cohen</span>,
<span class="contrib-name">Gregory Cook</span>,
<span class="contrib-name">Tim Dietrich</span>,
<span class="contrib-name">Matt Giesler</span>,
<span class="contrib-name">Jason Grigsby</span>,
<span class="contrib-name">Casey Handmer</span>,
<span class="contrib-name">Frank Herrmann</span>,
<span class="contrib-name">Ian Hinder</span>,
<span class="contrib-name">Jeff Kaplan</span>,
<span class="contrib-name">Rez Khan</span>,
<span class="contrib-name">Prayush Kumar</span>,
<span class="contrib-name">Adam Lewis</span>,
<span class="contrib-name">François Limousin</span>,
<span class="contrib-name">Jonas Lippuner</span>,
<span class="contrib-name">Keith Matthews</span>,
<span class="contrib-name">Abdul Mroué</span>,
<span class="contrib-name">Lydia Nevin</span>,
<span class="contrib-name">Fatemeh Nouri</span>,
<span class="contrib-name">Maria Okounkova</span>,
<span class="contrib-name">David Radice</span>,
<span class="contrib-name">Oliver Rinne</span>,
<span class="contrib-name">Olivier Sarbach</span>,
<span class="contrib-name">Deirdre Shoemaker</span>,
<span class="contrib-name">Leo C. Stein</span>,
<span class="contrib-name">Nick Tacik</span>,
<span class="contrib-name">Nick Taylor</span>,
<span class="contrib-name">Manuel Tiglio</span>,
<span class="contrib-name">Vijay Varma</span>,
<span class="contrib-name">Trevor Vincent</span>,
<span class="contrib-name">John Wendell</span>,
<span class="contrib-name">Catherine Woodford</span>,
<span class="contrib-name">Anil Zenginoglu</span>,
<span class="contrib-name">Fan Zhang</span>,
and
<span class="contrib-name">Aaron Zimmerman</span>.

Finally, we thank the following undergraduate students for assisting with
visualization and running simulations with SpEC:
<span class="contrib-name">Nousha Afshari</span>,
<span class="contrib-name">Aliya Babul</span>,
<span class="contrib-name">Adam Bartnik</span>,
<span class="contrib-name">Deshpreet Bedi</span>,
<span class="contrib-name">Darius Bunandar</span>,
<span class="contrib-name">Iryna Butsky</span>,
<span class="contrib-name">Patrick Calhoun</span>,
<span class="contrib-name">Sourabh Chakraborty</span>,
<span class="contrib-name">Cameron Cogburn</span>,
<span class="contrib-name">Nick Demos</span>,
<span class="contrib-name">Patrick Fraser</span>,
<span class="contrib-name">Alyssa Garcia</span>,
<span class="contrib-name">Bryant Garcia</span>,
<span class="contrib-name">Yi Chen Hu</span>,
<span class="contrib-name">Daniel Jones</span>,
<span class="contrib-name">Haroon Khan</span>,
<span class="contrib-name">Dave Kotfis</span>,
<span class="contrib-name">Dongjun Li</span>,
<span class="contrib-name">Yor Limkumnerd</span>,
<span class="contrib-name">Ian MacCormack</span>,
<span class="contrib-name">Tamin Mansour</span>,
<span class="contrib-name">Robert McGehee</span>,
<span class="contrib-name">Dmitry Meyerson</span>,
<span class="contrib-name">Adam Neumann</span>,
<span class="contrib-name">Amin Nikbin</span>,
<span class="contrib-name">Hiroaki Oyaizu</span>,
<span class="contrib-name">Daniel Parada</span>,
<span class="contrib-name">Jennifer Seiler</span>,
<span class="contrib-name">Haolin Shi</span>,
<span class="contrib-name">Keara Soloway</span>,
<span class="contrib-name">Alexandre Streicher</span>,
and
<span class="contrib-name">Allen Sussman</span>.

# Publications

The following publications have made use of SpEC. For their abstracts
and additional papers, see the [SXS Papers page]({{ site.baseurl }}{%
link for-researchers/sxs-papers.markdown %}).


{% include paper-list.html
    numbered=true
    filter_field="used_spec"
    suppress_abstracts=true %}
