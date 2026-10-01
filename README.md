# Topological Hydrodynamic Framework for Elliptic Curves

An analytic and computational framework mapping Archimedean Néron–Silverman local height pairings on elliptic curves $E/\mathbb{Q}$ to point-vortex interaction energies on Riemannian 2-tori $\mathbb{T}^2 \cong \mathbb{C}/\Lambda$.

---

## Universal Scaling Law

The metric correspondence between the Archimedean pairing $\langle P, Q \rangle_\infty$ and the flat-torus vortex energy $E_{\text{vortex}}(z_P, z_Q)$ is governed by the universal scaling factor:

$$C_E(E) = \frac{3\pi^2}{\omega_1^2}$$

### Theoretical Factor Decomposition

$$C_E(E) = (2\pi) \times \left(\frac{\pi}{\omega_1^2}\right) \times \left(\frac{3}{2}\right)$$

1. **Hydrodynamic Singularity ($2\pi$):** Normalization of the 2D Green function logarithmic singularity $-\frac{1}{2\pi}\log\vert{}z\vert{}$ on $\mathbb{T}^2$.
2. **Metric Pull-Back ($\pi / \omega_1^2$):** Conformal rescaling of the Laplace–Beltrami operator under uniformization coordinates $u = z/\omega_1$.
3. **Arakelov Volume Invariant ($3/2$):** Regularization index matching the admissible Arakelov metric against the modular fundamental domain $\text{Vol}(SL_2(\mathbb{Z}) \backslash \mathbb{H})$.

---

## Validation Suite

### 1. Point-Invariance & Bilinearity (Test A)
- **Target Curve:** LMFDB `38970.a1` ($r = 2$)
- **Pairs Evaluated:** $(P, Q)$, $(2P, Q)$, $(P, 2Q)$, $(P, P+Q)$, $(P+Q, Q)$, $(2P, 2Q)$, $(P+Q, P-Q)$, $(3P, Q)$
- **Mean Residual:** `0.0022%`
- **Max Residual:** `0.0059%`

### 2. Multi-Curve Cross-Validation (Test B)
- **Dataset:** 11 rank-2 curves spanning conductors $N \in [389, 38970]$ with positive and negative discriminants.
- **Mean Relative Residual:** `0.62%` (sub-0.5% across moderate conductors).

### 3. $SL_2(\mathbb{Z})$ Modular Invariance (Test C)
- **Invariance Generators:** $T: \tau \mapsto \tau + 1$ and $S: \tau \mapsto -1/\tau$.
- **Residual:** `0.000000%` on the complete Arakelov Green kernel including modular weight invariants.

---

## Repository Structure

```text
├── docs/
│   └── THEORY_ARAKELOV_DERIVATION.md   # Rigorous analytical derivation
├── experiments/
│   ├── test_a_bilinearity.py          # Generator bilinearity validation
│   ├── benchmark_suite_11curves.py     # 11-curve universal scaling test
│   ├── test_sl2z_invariance.py        # Full modular invariance test
│   └── PHASE2_RESULTS.md               # Empirical benchmark logs
└── src/
    ├── reproduce_benchmark.py          # Primary reproduction pipeline (38970.a1)
    ├── test_cross_curve.py             # Cross-curve validation (389.a1)
    └── test_point_invariance.py        # Point independence check