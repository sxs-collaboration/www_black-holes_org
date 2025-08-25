---
title: Gravitational Waveform Models
subtitle: From NR to data analysis
paginate_from_menu: true
---

Since 2015, observatories like LIGO have detected dozens of black hole mergers through the faint ripples of gravitational waves. These detections have opened an entirely new way of observing the universe. But to interpret what the detectors see we need accurate theoretical models of the waveforms.

One of the most important astrophysical sources of these waves comes from compact binaries: two black holes or neutron stars orbiting each other, gradually spiraling inward until they merge. As they move, their dynamics generate gravitational waves that propagate outward and can be detected by observatories such as LIGO. Modeling these signals is challenging because the underlying physics is governed by complicated systems of differential equations. To interpret LIGO detections and do meaningful astrophysics, we need highly accurate models of the gravitational waveforms.

Numerical relativity (NR) provides the only fully accurate method for simulating the merger stage of binary black hole systems. Given a specific set of parameters -- such as the masses of the black holes and the directions of their spins -- NR simulations compute the corresponding gravitational waveform. These waveforms are essential for a wide variety of applications: building template banks for searches, estimating source parameters, testing general relativity, and exploring model biases, to name just a few.

Numerical relativity (NR) provides the only fully accurate method for simulating the merger stage of binary black hole systems. Given a specific set of parameters—such as the masses of the black holes and the directions of their spins—NR simulations compute the corresponding gravitational waveform. These waveforms are essential for a wide variety of applications: building template banks for searches, estimating source parameters, testing general relativity, and exploring model biases, to name just a few. Modern state-of-the-art models, such as the effective one body and phenomenological families, rely on NR simulations for calibration (e.g., "matching the analytic waveform against NR results in the strong-field regime"), ensuring their predictions remain faithful.

The challenge is that NR simulations are extremely computationally expensive, often requiring days to months on powerful supercomputers. This makes them far too slow for most applications, which often require evaluating waveforms millions of times.

{% include image.html class="right"
url="/images/surrogates/Paramspace.png"
description="Sampling the parameter space"
%}

### Surrogate models: A faster alternative

Surrogate modeling provides a practical, data-driven solution. Rather than solving Einstein’s equations from scratch each time, surrogate models learn from previously computed NR simulations. These simulations can provide a range of astrophysically important outputs, including gravitational waveforms, the properties of the remnant black hole formed after merger, and more.

This approach is a lot like weather forecasting. Running a full atmospheric simulation would take far too long to be useful. Instead, meteorologists sometimes use reduced models that capture the essential physics but can be run quickly to provide timely forecasts. Surrogate models play the same role for gravitational waves: they retain the accuracy of expensive simulations but deliver answers in milliseconds instead of months.

To build such a model, we first generate a large library of NR simulations that cover the relevant parameter space. For example, consider a simplified class of systems known as *aligned-spin binaries*. In these systems:

1. The black holes orbit in the xy-plane,
2. Their spins are aligned with the orbital angular momentum (the z-axis).

The parameter space for these systems is three-dimensional, defined by the mass ratio (q), the spin on the larger black hole, and the spin on the smaller black hole. An algorithm selects the most informative points in this three-dimensional space, and for each mass ratio and spin configuration we run a full NR simulation to compute the waveform.

Hundreds to thousands of simulations are needed to adequately cover the parameter space, as shown in the figure. Once this dataset is assembled, we build the surrogate model in three main steps:

1. **Feature extraction**: Break each waveform into simpler building blocks.
2. **Dimensionality reduction**: Approximate each building block in a compact, low-dimensional space.
3. **Regression**: Use fitting and interpolation techniques to connect the low-dimensional features across the parameter space.

{% include image.html class="left"
url="/images/surrogates/gwsurrogate.png"
description="Example surrogate model evaluation"
%}

The result is a model that can reproduce the accuracy of expensive NR simulations but at a tiny fraction of the cost. For example, the figure compares the output of a surrogate model with a full NR simulation of a precessing binary black hole system. The NR simulation required 70,881 CPU-hours (about 1.75 months on 56 cores of the Frontera supercomputer), while the surrogate model produced a prediction in just 100 milliseconds.

Surrogate modeling has therefore become a powerful tool in gravitational wave astronomy, enabling researchers to explore parameter space rapidly and extract astrophysical insights that would otherwise be computationally inaccessible.


If you'd like to learn more about surrogate modeling techniques, please watch the [Surrogate Movie](https://vijayvarma392.github.io/SurrogateMovie/).
