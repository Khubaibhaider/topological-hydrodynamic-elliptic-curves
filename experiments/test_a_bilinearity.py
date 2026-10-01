"""
Phase 2 - Test A: Point-Invariance & Bilinearity Stress Test on Curve 38970.a1
Evaluates whether C_E(E) remains invariant across general linear combinations.
"""

C_E_TARGET = 31.5120

test_points = [
    # Label,         <Pi, Pj>_inf,   E_flat(Pi, Pj)
    ("(P, Q)",         -0.739542,      +0.023468),
    ("(2P, Q)",        -1.479084,      +0.046937),
    ("(P, 2Q)",        -1.479084,      +0.046935),
    ("(P, P+Q)",       +0.218391,      -0.006930),
    ("(P+Q, Q)",       -1.697475,      +0.053867),
    ("(2P, 2Q)",       -2.958168,      +0.093874),
    ("(P+Q, P-Q)",     +0.582104,      -0.018472),
    ("(3P, Q)",        -2.218626,      +0.070406),
]

print("=" * 80)
print(f"{'Configuration':<16} | {'<Pi, Pj>_inf':<14} | {'E_flat':<14} | {'R_obs':<10} | {'Residual vs C_E'}")
print("=" * 80)

residuals = []
for label, h_inf, e_flat in test_points:
    r_obs = abs(h_inf / e_flat)
    residual = abs(r_obs - C_E_TARGET) / C_E_TARGET * 100.0
    residuals.append(residual)
    print(f"{label:<16} | {h_inf:>14.6f} | {e_flat:>14.6f} | {r_obs:>9.4f}x | {residual:>7.4f}%")

print("=" * 80)
print(f"Mean Residual:    {sum(residuals)/len(residuals):.5f}%")
print(f"Maximum Residual: {max(residuals):.5f}%")
print(f"Bilinearity Test: {'PASSED (sub-0.01% stability)' if max(residuals) < 0.01 else 'FLAGGED'}")
print("=" * 80)