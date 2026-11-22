"""Parameter changes (requirement C) and new related cases (requirement E)
for Tasks 17-20. Run once: python code/new_cases_tasks_17_20.py
No graphs are drawn, so it runs straight through."""
import numpy as np
from math import erf, sqrt
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

def title(s):
    print("\n" + "=" * 8, s, "=" * 8)

# ---------------- Task 17 ----------------
title("Task 17")
def euler_cooling(T0, Ta, k, h, end):
    t = np.arange(0.0, end + h, h)
    T = np.zeros_like(t)
    T[0] = T0
    for i in range(len(t) - 1):
        T[i + 1] = T[i] + h * (-k * (T[i] - Ta))
    exact = Ta + (T0 - Ta) * np.exp(-k * t)
    return T[-1], exact[-1], abs(T[-1] - exact[-1])
for h in (1.0, 5.0, 0.1):
    e, x, err = euler_cooling(90.0, 25.0, 0.12, h, 30.0)
    print(f"h={h}: Euler {e:.2f} C, exact {x:.2f} C, error {err:.4f} C")
e, x, err = euler_cooling(95.0, 22.0, 0.07, 2.0, 40.0)
print(f"New case tea, h=2: Euler {e:.2f} C, exact {x:.2f} C, error {err:.3f} C")

# ---------------- Task 18 ----------------
title("Task 18")
def rc_charge(R, C, Vs=5.0):
    s = solve_ivp(lambda t, V: [(Vs - V[0]) / (R * C)], (0, 5), [0.0],
                  t_eval=np.linspace(0, 5, 200), rtol=1e-9, atol=1e-11)
    exact = Vs * (1 - np.exp(-s.t / (R * C)))
    return s.success, s.y[0, -1], np.max(np.abs(s.y[0] - exact))
print("C = 0.001 F:", rc_charge(1000.0, 0.001))
print("C = 0.005 F:", rc_charge(1000.0, 0.005))
R, C = 2000.0, 0.0005
s = solve_ivp(lambda t, V: [-V[0] / (R * C)], (0, 5), [9.0],
              t_eval=[3.0, 5.0], rtol=1e-9, atol=1e-11)
print(f"New case discharge: V(3 s) = {s.y[0,0]:.4f} V, V(5 s) = {s.y[0,1]:.4f} V")

# ---------------- Task 19 ----------------
title("Task 19")
def optimise(cost_a, cost_b, cap_a, cap_b, required):
    sol = minimize(lambda z: cost_a * z[0] + cost_b * z[1], x0=[5, 3],
                   method="SLSQP", bounds=[(0, None), (0, None)],
                   constraints={"type": "ineq",
                                "fun": lambda z: cap_a * z[0] + cap_b * z[1] - required})
    best = None
    for a in range(0, 40):
        for b in range(0, 40):
            capacity = cap_a * a + cap_b * b
            if capacity >= required:
                total = cost_a * a + cost_b * b
                if best is None or total < best[0]:
                    best = (total, a, b, capacity)
    print(f"  success {sol.success}, A={sol.x[0]:.3f}, B={sol.x[1]:.3f}, "
          f"cost {sol.fun:.2f}, best whole-number (cost, A, B, capacity): {best}")
print("Original (cost B = 18):")
optimise(12, 18, 100, 170, 1000)
print("Cost of B raised to 22:")
optimise(12, 22, 100, 170, 1000)
print("New case, delivery vans (cost 40, 300 parcels) and bikes (cost 15, 80 parcels), need 2000:")
optimise(40, 15, 300, 80, 2000)

# ---------------- Task 20 ----------------
title("Task 20")
def monte_carlo(mean, std, capacity, N, seed=42):
    demand = np.random.default_rng(seed).normal(mean, std, N)
    overloaded = demand > capacity
    return overloaded.mean(), int(overloaded.sum())
def exact(mean, std, capacity):
    z = (capacity - mean) / std
    return 0.5 * (1 - erf(z / sqrt(2)))
p, n = monte_carlo(850, 120, 1000, 100_000)
print(f"Original: {p:.4%} ({n} cases), exact {exact(850,120,1000):.4%}")
p, n = monte_carlo(850, 160, 1000, 100_000)
print(f"Std 160: {p:.4%} ({n} cases), exact {exact(850,160,1000):.4%}")
p, n = monte_carlo(850, 120, 1000, 1_000)
print(f"N = 1000: {p:.4%} ({n} cases)")
p, n = monte_carlo(45, 8, 60, 100_000)
print(f"New case help desk (mean 45, std 8, capacity 60): {p:.4%} ({n} cases), "
      f"exact {exact(45,8,60):.4%}")