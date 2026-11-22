"""Parameter changes (requirement C) and new related cases (requirement E)
for Tasks 13-16. Run once: python code/new_cases_tasks_13_16.py
No graphs are drawn, so it runs straight through."""
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
from scipy.optimize import curve_fit
from scipy.integrate import simpson

np.set_printoptions(precision=4, suppress=True)

def title(s):
    print("\n" + "=" * 8, s, "=" * 8)

# ---------------- Task 13 ----------------
title("Task 13")
hours = np.array([8, 9, 10, 11, 12, 13, 14], float)
temp = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0])
lin, cub = interp1d(hours, temp), CubicSpline(hours, temp)
print("All points, 10:30: linear", float(lin(10.5)), "cubic", round(float(cub(10.5)), 2))
# Parameter change: remove the 11:00 measurement, then estimate 11:00
h2 = np.array([8, 9, 10, 12, 13, 14], float)
t2 = np.array([18.0, 20.0, 22.5, 25.0, 25.5, 25.0])
lin2, cub2 = interp1d(h2, t2), CubicSpline(h2, t2)
print("11:00 removed, estimate at 11:00: linear", float(lin2(11)),
      "cubic", round(float(cub2(11)), 2), "(real value was 24.0)")
# New case: phone battery voltage every hour
hv = np.arange(0, 7, dtype=float)
volts = np.array([4.20, 4.12, 4.02, 3.91, 3.80, 3.70, 3.62])
lv, cv = interp1d(hv, volts), CubicSpline(hv, volts)
print("Battery at 2.5 h: linear", float(lv(2.5)), "cubic", round(float(cv(2.5)), 3))
print("Battery at 4.5 h: linear", float(lv(4.5)), "cubic", round(float(cv(4.5)), 3))

# ---------------- Task 14 ----------------
title("Task 14")
users = np.array([50, 100, 150, 200, 250, 300, 350], float)
resp = np.array([82, 95, 115, 145, 185, 238, 305], float)
models = {
    "linear": lambda x, a, b: a * x + b,
    "quadratic": lambda x, a, b, c: a * x**2 + b * x + c,
    "cubic": lambda x, a, b, c, d: a * x**3 + b * x**2 + c * x + d,
}
for name, f in models.items():
    p, _ = curve_fit(f, users, resp)
    rmse = np.sqrt(np.mean((resp - f(users, *p)) ** 2))
    print(f"{name}: RMSE {rmse:.2f} ms, predicted at 400 users {f(400, *p):.2f} ms")
ad = np.arange(1, 8, dtype=float)
sales = np.array([12.5, 15.1, 17.2, 19.8, 22.4, 24.9, 27.3])
f = models["linear"]
p, _ = curve_fit(f, ad, sales)
rmse = np.sqrt(np.mean((sales - f(ad, *p)) ** 2))
print(f"New case sales = {p[0]:.4f} * ad + {p[1]:.4f}, RMSE {rmse:.2f}, "
      f"predicted at 8 = {f(8, *p):.2f}")

# ---------------- Task 15 ----------------
title("Task 15")
def speed_estimates(t, x):
    s = np.zeros_like(x)
    s[0] = (x[1] - x[0]) / (t[1] - t[0])
    for i in range(1, len(t) - 1):
        s[i] = (x[i + 1] - x[i - 1]) / (t[i + 1] - t[i - 1])
    s[-1] = (x[-1] - x[-2]) / (t[-1] - t[-2])
    return s
time = np.arange(7, dtype=float)
pos = np.array([0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0])
print("Original speeds:", speed_estimates(time, pos))
changed = pos.copy()
changed[3] = 17.0                       # reading at t = 3 s: 16.1 -> 17.0
print("Changed speeds: ", speed_estimates(time, changed))
tf = np.arange(0, 4.5, 0.5)
sf = 4.9 * tf**2                        # falling object, s = 4.9 t^2
print("Falling object estimated:", speed_estimates(tf, sf))
print("Falling object true v=9.8t:", 9.8 * tf)

# ---------------- Task 16 ----------------
title("Task 16")
th = np.array([0, 2, 4, 6, 8, 10, 12], float)
pw = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])
print("Original: trapezoid", round(np.trapezoid(pw, th), 3),
      "Simpson", round(simpson(pw, x=th), 3))
pw2 = pw.copy()
pw2[3] = 2.6                            # reading at 06:00: 1.8 -> 2.6 kW
print("Peak 2.6 kW: trapezoid", round(np.trapezoid(pw2, th), 3),
      "Simpson", round(simpson(pw2, x=th), 3))
tv = np.arange(0, 70, 10, dtype=float)
vel = np.array([0, 5, 12, 18, 22, 24, 24], float)
print("Car distance: trapezoid", round(np.trapezoid(vel, tv), 2),
      "Simpson", round(simpson(vel, x=tv), 2))