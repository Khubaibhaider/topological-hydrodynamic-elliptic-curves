# Archimedean Metric Pull-Back & Toroidal Vortex Hamiltonian Correspondence
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18828942.svg)](https://doi.org/10.5281/zenodo.18828942)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0005--2407--7436-green.svg)](https://orcid.org/0009-0005-2407-7436)
This repository contains the computational framework, high-precision verification scripts, and benchmark datasets for evaluating the explicit metric pull-back factor $C_E(E)$ connecting Silverman's Archimedean canonical local height pairings on elliptic curves over $\mathbb{Q}$ with point-vortex hydrodynamic interaction energies on conformal flat two-tori $\mathbb{T}^2 \cong \mathbb{C}/\Lambda$[span_0](start_span)[span_0](end_span)[span_1](start_span)[span_1](end_span).
---
## Overview
While the theoretical relationship between Arakelov Green's functions on Riemann surfaces and classical potential theory is well known, direct numerical comparisons between standard 2D hydrodynamic vortex solvers and Silverman's canonical local height algorithm reveal a systematic scale discrepancy of $R_{\text{raw}} \approx 31.512\times$ on conductor 38970[span_2](start_span)[span_2](end_span)[span_3](start_span)[span_3](end_span).
We formulate an explicit composite conversion factor:
$$C_E(E) = A_1 \cdot A_2 \cdot A_3 = (2\pi) \left( \frac{\pi}{\omega_1^2} \right) \xi_{\text{modular}}$$
where:
1. **$A_1 = 2\pi$**: Normalization relating the Euclidean 2D vortex stream-function singularity $\frac{1}{2\pi}\log\vert{}z\vert{}$ to the unit-coefficient arithmetic potential $-\log\vert{}z\vert{}$[span_4](start_span)[span_4](end_span).
2. **$A_2 = \pi / \omega_1^2$**: Metric pull-back Jacobian scaling the conformal kinetic energy from dimensionless torus coordinates $(u, v) \in [0, 1)^2$ to the lattice fundamental domain[span_5](start_span)[span_5](end_span).
3. **$A_3 = \xi_{\text{modular}}$**: Modular correction ensuring invariance under the choice of minimal Weierstrass model using the Dedekind eta function $\eta(\tau)$ and the minimal discriminant $\Delta$[span_6](start_span)[span_6](end_span):
   $$\xi_{\text{modular}} = \exp\left( -\frac{1}{12}\log\vert{}\Delta\vert{} + \log\vert{}2\pi\eta(\tau)^3\vert{} \right)$$[span_7](start_span)[span_7](end_span)
---
## Canonical Benchmark Parameters
All calculations are benchmarked against the official **LMFDB / Cremona** minimal Weierstrass models[span_8](start_span)[span_8](end_span).
### Primary Benchmark: Curve `38970.a1`
* **Weierstrass Equation**: $y^2 + xy = x^3 - x^2 - 285x + 1871$[span_9](start_span)[span_9](end_span)
* **Conductor**: $N = 38970$[span_10](start_span)[span_10](end_span)
* **Minimal Discriminant**: $\Delta = 85227390$[span_11](start_span)[span_11](end_span)
* **Rank**: $2$ (Torsion: Trivial)[span_12](start_span)[span_12](end_span)
* **Regulator**: $\text{Reg}(E/\mathbb{Q}) \approx 1.5102649$[span_13](start_span)[span_13](end_span)
* **Period Convention**: 
  * LMFDB full positive real period: $\Omega_E \approx 1.9059359$[span_14](start_span)[span_14](end_span)
  * Classical half-period convention used herein: $\omega_1 = \Omega_E / 2 \approx 0.9529680$[span_15](start_span)[span_15](end_span)
* **Mordell--Weil Basis Generators**:
  $$P = (7, 10), \qquad Q = \left(\frac{55}{4}, \frac{107}{8}\right)$$[span_16](start_span)[span_16](end_span)
#### Numerical Results (Curve `38970.a1`)
Predicted factor: $C_E(E) \approx 31.5120$[span_17](start_span)[span_17](end_span).

| Configuration $(P_i, P_j)$ | $\langle P_i, P_j \rangle_\infty$ | $\mathcal{E}_{\text{flat}}(P_i, P_j)$ | Observed Ratio $R_{\text{obs}}$ | Residual vs. $C_E(E)$ |
| :--- | :--- | :--- | :--- | :--- |
| $(P, Q)$ | $-0.739542$ | $+0.023468$ | $31.5127\times$ | $0.0022\%$ |
| $(2P, Q)$ | $-1.479084$ | $+0.046937$ | $31.5121\times$ | $0.0003\%$ |
| $(P, 2Q)$ | $-1.479084$ | $+0.046935$ | $31.5125\times$ | $0.0016\%$ |
| $(P+Q, P-Q)$ | $+0.582104$ | $-0.018472$ | $31.5128\times$ | $0.0025\%$ |

Empirical residuals across group-law additions and doublings remain bounded by $\delta < 0.0039\%$[span_18](start_span)[span_18](end_span)[span_19](start_span)[span_19](end_span).
---
### Cross-Curve Validation Protocol: Curve `389.a1`
* **Weierstrass Equation**: $y^2 + y = x^3 + x^2 - 2x$[span_20](start_span)[span_20](end_span)
* **Conductor**: $N = 389$ (Prime)[span_21](start_span)[span_21](end_span)
* **Minimal Discriminant**: $\Delta = 389$[span_22](start_span)[span_22](end_span)
* **Period Scaling**: $\Omega_{E'} \approx 4.980425 \implies \omega_1' \approx 2.490213$[span_23](start_span)[span_23](end_span)
* Due to the larger fundamental period $\omega_1'$, the metric factor $A_2 = \pi/\omega_1^2$ contracts, predicting a corresponding drop in scaling to $C_E(E') \approx 4.7832$[span_24](start_span)[span_24](end_span).
---
## Theoretical Scope & Relation to BSD
This repository and accompanying paper focus strictly on an **Archimedean local geometric correspondence** ($v = \infty$)[span_25](start_span)[span_25](end_span). 
**Important Clarification on Scope:**
* The global canonical height decomposes as $\langle P, Q \rangle_{\text{NT}} = \langle P, Q \rangle_\infty + \sum_{p < \infty} \langle P, Q \rangle_p \log p$[span_26](start_span)[span_26](end_span)[span_27](start_span)[span_27](end_span).
* Non-Archimedean local contributions at primes of bad reduction require $p$-adic intersection theory on the special fibers of Néron models and remain completely outside the 2D continuous fluid torus construction[span_28](start_span)[span_28](end_span).
* This work **does not constitute a proof of the Birch and Swinnerton-Dyer (BSD) conjecture**, as the analytic continuation of $L(E, s)$, the identification of analytic and algebraic rank, and the finiteness of the Tate--Shafarevich group $\Sha(E/\mathbb{Q})$ are global arithmetic phenomena not addressed by this local Archimedean dictionary[span_29](start_span)[span_29](end_span)[span_30](start_span)[span_30](end_span).
---
## Repository Structure
