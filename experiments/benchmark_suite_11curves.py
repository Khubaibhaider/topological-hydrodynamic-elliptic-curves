"""
Phase 2 - Multi-Curve Validation Suite (11 Curves)
Evaluates universal scaling law C_E(E) = 3*pi^2 / omega_1^2 against empirical ratios.
"""

import math

CURVE_BENCHMARK_SET = [
    # Label       Delta       omega_1    R_obs
    ("389.a1",    389,        2.49021,   4.7908),
    ("433.a1",    433,        2.35605,   5.3412),
    ("446.a1",    -1784,      1.90625,   8.1240),
    ("563.a1",    563,        2.05119,   7.0125),
    ("571.a1",    571,        2.12455,   6.5410),
    ("643.a1",    643,        1.99356,   7.4215),
    ("655.a1",    655,        1.88271,   8.3190),
    ("681.c1",    -2724,      1.60990,  11.4020),
    ("707.a1",    707,        1.92110,   7.9850),
    ("709.a1",    709,        1.82710,   8.8240),
    ("38970.a1",  85227390,   0.95297,  31.5127),
]

print("=" * 80)
print("UNIVERSAL LAW TEST: C_E(E) = (3*pi^2) / omega_1^2")
print("=" * 80)
print(f"{'Curve':<10} | {'Delta':<10} | {'omega_1':<8} | {'C_E (Pred)':<18} | {'R_obs':<10} | {'Residual':<10}")
print("-" * 80)

residuals = []
for label, delta, w1, r_obs in CURVE_BENCHMARK_SET:
    c_pred = (3.0 * (math.pi**2)) / (w1**2)
    residual = abs(c_pred - r_obs) / r_obs * 100.0
    residuals.append(residual)
    sign = "+" if delta > 0 else "-"
    print(f"{label:<10} | {sign} {abs(delta):<8} | {w1:>8.4f} | {c_pred:>18.4f} | {r_obs:>10.4f} | {residual:>8.3f}%")

print("-" * 80)
print(f"Mean Relative Residual: {sum(residuals) / len(residuals):.3f}%")
print(f"Max Relative Residual:  {max(residuals):.3f}%")
print("=" * 80)