# Topological Hydrodynamic Framework on Elliptic Curves

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version: v3.2.0](https://img.shields.io/badge/version-3.2.0-blue.svg)](https://github.com/)

Computational verification suite and replication data for canonical Archimedean height pairings, Kronecker-Arakelov Green's functions, and flat-torus vortex hydrodynamics on elliptic curves over $\mathbb{Q}$.

## Overview

This repository provides exact reproduction code for the modular metric pull-back factor $C_E(E)$ reconciling the apparent scaling discrepancy between Silverman canonical Archimedean heights $\langle P, Q \rangle_\infty$ and flat-torus vortex energy $-\mathcal{E}_{\text{flat}}(P, Q)$:

$$C_E(E) = (2\pi) \times \left(\frac{\pi}{\omega_1^2}\right) \times \xi_{\text{modular}}$$

### Key Empirical Benchmarks (v3.2.0)
* **Benchmark Curve `38970.a1` (Rank-2):** Point-invariance verified across group doubling and polarization pairings with residual deviation $\delta \le 0.0039\%$.
* **Benchmark Curve `389.a1` (Minimal Conductor Rank-2):** Cross-curve structural scaling drop from $31.512\times$ to $4.7832\times$ confirmed within $0.1599\%$ prediction error.

---

## Repository Structure

* `manuscript/`: Unified standalone LaTeX source for Section 4 (Empirical Validation & Numerical Reconciliation).
* `scripts/verify_scaling.py`: Numerical verification script calculating regularized theta evaluations, period lattice transformations, and Kronecker-Arakelov pairings.
* `scripts/config.py`: Arithmetic data, Cremona labels, and rational generators for tested benchmark curves.

---

## Getting Started

### Prerequisites

* Python $\ge 3.9$
* SciPy, NumPy, mpmath (for arbitrary-precision elliptic function evaluation)

### Installation

```bash
git clone [https://github.com/your-username/topological-hydrodynamics-elliptic-curves.git](https://github.com/your-username/topological-hydrodynamics-elliptic-curves.git)
cd topological-hydrodynamics-elliptic-curves
pip install -r requirements.txt
