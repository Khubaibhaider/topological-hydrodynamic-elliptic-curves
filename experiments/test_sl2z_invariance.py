"""
Phase 2 / Phase 3 Bridge - Test C: SL_2(Z) Modular Invariance Test
Verifies that the full Arakelov Green function / height kernel is invariant under:
    T: tau -> tau + 1
    S: tau -> -1 / tau
"""

import cmath
import math

def theta1_approx(z, tau, n_terms=20):
    """Computes Jacobi theta_1(z, tau) series expansion."""
    q = cmath.exp(1j * math.pi * tau)
    total = 0.0 + 0.0j
    for n in range(n_terms):
        coeff = ((-1) ** n) * (q ** ((n + 0.5) ** 2))
        angle = (2 * n + 1) * math.pi * z
        total += coeff * cmath.sin(angle)
    return 2.0 * total

def dedekind_eta_log(tau, n_terms=60):
    """Computes log|eta(tau)|."""
    # eta(tau) = exp(i*pi*tau/12) * prod(1 - q^(2n))
    log_prod = 0.0
    q_sq = cmath.exp(2j * math.pi * tau)
    term = q_sq
    for _ in range(1, n_terms):
        val = 1.0 - term
        if abs(val) < 1e-15:
            break
        log_prod += math.log(abs(val))
        term *= q_sq
    return -(math.pi * tau.imag / 12.0) + log_prod

def g_arakelov_invariant(z, tau):
    """
    Computes the full SL_2(Z)-invariant Arakelov Green kernel:
    G(z, tau) = -log|theta_1(z, tau)| + pi*(Im(z))^2 / Im(tau) + log|eta(tau)|
    """
    th = theta1_approx(z, tau)
    if abs(th) < 1e-15:
        return float('inf')
    
    val = -math.log(abs(th)) + math.pi * ((z.imag) ** 2) / tau.imag + dedekind_eta_log(tau)
    return val

def run_sl2z_test():
    tau = complex(0.24510, 0.81735)
    z_point = complex(0.3125, 0.1875)
    
    # Baseline invariant Green kernel
    g_base = g_arakelov_invariant(z_point, tau)
    
    # 1. T transformation: tau -> tau + 1, z -> z
    tau_T = tau + 1.0
    z_T = z_point
    g_T = g_arakelov_invariant(z_T, tau_T)
    res_T = abs(g_T - g_base) / abs(g_base) * 100.0
    
    # 2. S transformation: tau -> -1/tau, z -> z/tau
    tau_S = -1.0 / tau
    z_S = z_point / tau
    g_S = g_arakelov_invariant(z_S, tau_S)
    res_S = abs(g_S - g_base) / abs(g_base) * 100.0
    
    print("=" * 76)
    print("TEST C: SL_2(Z) MODULAR INVARIANCE ON THE COMPLETE ARAKELOV KERNEL")
    print("=" * 76)
    print(f"Base Modulus (tau):       {tau.real:+.5f} + {tau.imag:.5f}i")
    print(f"Test Point (z):           {z_point.real:+.5f} + {z_point.imag:.5f}i")
    print(f"Base Kernel Value:        G(z, tau)        = {g_base:+.8f}")
    print("-" * 76)
    print(f"T-Transform [tau + 1]:    G(z, tau+1)      = {g_T:+.8f} (Res: {res_T:.6f}%)")
    print(f"S-Transform [-1/tau]:     G(z/tau, -1/τ)   = {g_S:+.8f} (Res: {res_S:.6f}%)")
    print("=" * 76)
    
    if max(res_T, res_S) < 0.05:
        print("VERDICT: PASS — Kernel is strictly invariant under full modular group SL_2(Z).")
    else:
        print("VERDICT: FAIL — Residual exceeds tolerance.")
    print("=" * 76)

if __name__ == "__main__":
    run_sl2z_test()