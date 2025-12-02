---
title: "From Black Hole to Galaxy: Neural Operator: Framework for Accretion and Feedback Dynamics"
authors:
  - "Bhojwani, Nihaal"
  - "Wang, Chuwei"
  - "Wang, Hai-Yang"
  - "Sun, Chang"
  - "Most, Elias R."
  - "Anandkumar, Anima"
jref:
doi:
date: 2025-12-01
arxiv: "2512.01576"
insp_recid: 3088176
used_spec:
used_spectre:
abstract: |
  Modeling how supermassive black holes co-evolve with their host
  galaxies is notoriously hard because the relevant physics spans nine
  orders of magnitude in scale-from milliparsecs to megaparsecs--
  making end-to-end first-principles simulation infeasible. To
  characterize the feedback from the small scales, existing methods
  employ a static subgrid scheme or one based on theoretical guesses,
  which usually struggle to capture the time variability and derive
  physically faithful results. Neural operators are a class of machine
  learning models that achieve significant speed-up in simulating
  complex dynamics. We introduce a neural-operator-based ''subgrid
  black hole'' that learns the small-scale local dynamics and embeds
  it within the direct multi-level simulations. Trained on small-
  domain (general relativistic) magnetohydrodynamic data, the model
  predicts the unresolved dynamics needed to supply boundary
  conditions and fluxes at coarser levels across timesteps, enabling
  stable long-horizon rollouts without hand-crafted closures. Thanks
  to the great speedup in fine-scale evolution, our approach for the
  first time captures intrinsic variability in accretion-driven
  feedback, allowing dynamic coupling between the central black hole
  and galaxy-scale gas. This work reframes subgrid modeling in
  computational astrophysics with scale separation and provides a
  scalable path toward data-driven closures for a broad class of
  systems with central accretors.
---
