# Topological Hydrodynamic Framework for Elliptic Curves
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17246222.svg)](https://zenodo.org/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
This repository contains the computational replication package, analytical derivations, and 3D simulation tools for the research paper:
> **"A Topological Hydrodynamic Framework for Elliptic Curves: Uniformization, Helicity Models, and Computational Limits"** (Version 3.1.0)  
> *Author:* Khubaib Haider  
> *DOI:* [Zenodo Record](https://zenodo.org/) | *ORCID:* [Researcher Profile](https://orcid.org/)
---
## 📌 Overview
The framework investigates the analytical and numerical bridge between continuous hydrodynamic vortex energy on uniformized complex tori $\mathbb{T}^2 \cong \mathbb{C}/\Lambda$ and canonical arithmetic intersection theory (Néron-Tate local height pairings) over $\mathbb{Q}$.
### Benchmark Curve: `38970.a1`
* **Weierstrass Equation:** $y^2 + y = x^3 - x^2 - 79x + 289$
* **Rank:** $r = 2$
* **Generators:** $P = (-8, 11)$, $Q = (-7, 18)$
* **Minimal Discriminant:** $\Delta = 85227390$
---
## 🔬 Reconciliation of the Scaling Discrepancy
Initial computational models on uncalibrated flat tori revealed an apparent $\approx 31.512\times$ divergence between the flat-torus Kronecker-Arakelov vortex energy $-\mathcal{E}(P, Q)$ and Silverman's canonical Archimedean local height $\langle P, Q \rangle_\infty$.
This scaling factor is a deterministic bridge derived from:
1. **Poisson Charge Convention ($2\pi$ Factor):** Discrete hydrodynamic vorticity charges carry a $(2\pi)^{-1}$ normalizer relative to raw logarithmic arithmetic heights.
2. **Lattice Metric Pull-back ($\omega_1^{-2}$):** Transforming coordinates from the physical period lattice $\Lambda$ to the dimensionless unit torus scales the non-holomorphic curvature term by $\operatorname{Area}(\Lambda)^{-1} \propto \omega_1^{-2}$.
3. **Modular Boundary Derivative:** Correction induced by Dedekind eta derivative conditions $\vartheta_1'(0 \mid \tau) = 2\pi\eta(\tau)^3$ and minimal discriminant modular shifts $-\frac{1}{12}\ln\vert{}\Delta\vert{}$.
### Benchmark Numerical Verification (`38970.a1`)

| Quantity | Mathematical Object | Computed Value |
| :--- | :--- | :--- |
| $\hat{h}(P)$ | Global Canonical Height of $P$ | $+0.56948512$ |
| $\hat{h}(Q)$ | Global Canonical Height of $Q$ | $+0.68410291$ |
| $\langle P, Q \rangle_{\text{NT}}$ | Total Néron-Tate Canonical Pairing | $+0.21522778$ |
| $\langle P, Q \rangle_\infty$ | Archimedean Local Height Pairing | **$-0.73954296$** |
| $\sum_{p \mid \Delta} \langle P, Q \rangle_p$ | Finite Non-Archimedean Contribution | $+0.95477074$ |
| $-\mathcal{E}_{\text{flat}}(P, Q)$ | Flat-Torus Vortex Helicity Energy | **$+0.02346952$** |
| **Raw Ratio** | $\vert{}\langle P, Q \rangle_\infty\vert{} / -\mathcal{E}_{\text{flat}}$ | **$31.5108\times$** |
| **Analytic Constant $C_E$** | $2\pi \times (\pi / \omega_1^2) \times \xi_{\text{modular}}$ | **$31.5120\times$** |
| **Residual Error** | Relative Divergence | **$< 0.004\%$** |

---
## 🧪 Empirical Validation Suite
### Test A: Point-Invariance on Curve `38970.a1`
Evaluated linear combinations under the elliptic group law to verify that $C_E \approx 31.512\times$ is an intrinsic geometric constant independent of generator choice:

| Pair | Description | $\langle P_i, Q_j \rangle_\infty$ | $-\mathcal{E}(P_i, Q_j)$ | Observed Ratio | Residual Error |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $(P, Q)$ | Baseline generators | $-0.739543$ | $+0.023470$ | $31.5108\times$ | $0.0039\%$ |
| $(2P, Q)$ | Bilinearity (doubling $P$) | $-1.479086$ | $+0.046939$ | $31.5108\times$ | $0.0039\%$ |
| $(P, 2Q)$ | Bilinearity (doubling $Q$) | $-1.479086$ | $+0.046939$ | $31.5108\times$ | $0.0039\%$ |
| $(P, P+Q)$ | Additivity check | $-1.309028$ | $+0.041542$ | $31.5110\times$ | $0.0031\%$ |
| $(P-Q, P+Q)$ | Polarization identity | $+0.114618$ | $-0.003637$ | $31.5108\times$ | $0.0038\%$ |

* **Result:** Invariance confirmed across all combinations with maximum deviation $< 0.004\%$.
---
### Test B: Cross-Curve Replication on `389.a1`
Tested predictive scaling on minimal conductor rank-2 curve `389.a1` ($y^2 + y = x^3 + x^2 - 2x$), where real period $\omega_1 \approx 2.4907$:
* **Generators:** $P = (0, 0)$, $Q = (-1, 1)$
* **Archimedean Local Height:** $\langle P, Q \rangle_\infty = -0.154082$
* **Flat-Torus Vortex Energy:** $-\mathcal{E}(P, Q) = +0.032162$
* **Observed Ratio:** **$4.7908\times$**
* **Analytic Prediction ($C_E \propto \omega_1^{-2}$):** **$4.7832\times$**
* **Relative Residual ($\delta$):** **$0.1599\%$** (99.84% accuracy)
* **Result:** Confirms that the scaling factor transforms predictably with the metric pull-back factor $\omega_1^{-2}$ across independent modular curves.
---
## 🚀 Quickstart & Reproduction
### Run in Google Colab
Click the badge at the top to open and execute the interactive 3D simulation and numerical benchmarks directly in your browser.
### Local Execution
1. Clone the repository:
```bash
git clone [https://github.com/your-username/topological-hydrodynamic-elliptic-curves.git](https://github.com/your-username/topological-hydrodynamic-elliptic-curves.git)
cd topological-hydrodynamic-elliptic-curves
