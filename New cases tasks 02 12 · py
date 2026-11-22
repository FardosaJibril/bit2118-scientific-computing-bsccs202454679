"""Parameter changes (requirement C) and new related cases (requirement E)
for Tasks 2-12. Run once: python code/new_cases_tasks_02_12.py
No graphs are drawn, so it runs straight through."""
import timeit
import numpy as np
from scipy.optimize import root_scalar, root
from scipy.linalg import lu_factor, lu_solve

np.set_printoptions(precision=4, suppress=True)

def title(s):
    print("\n" + "=" * 8, s, "=" * 8)

# ---------------- Task 2 ----------------
title("Task 2")
temps = np.array([18.5, 18.0, 17.8, 17.5, 17.9, 19.0, 21.5, 23.8, 25.6, 27.1,
                  28.3, 29.0, 29.4, 29.1, 28.5, 27.6, 26.2, 24.8, 23.4, 22.1,
                  21.0, 20.2, 19.6, 19.0])
print("Original mean:", round(temps.mean(), 2))
changed = temps.copy()
changed[12] = 35.0                       # peak reading 29.4 -> 35.0
print("Changed peak: mean", round(changed.mean(), 2), "max", changed.max())
heart = np.array([62, 60, 58, 57, 59, 65, 78, 85, 88, 90, 92, 95,
                  97, 94, 90, 86, 82, 80, 76, 72, 68, 66, 64, 62], float)
print("New case heart rate: mean", round(heart.mean(), 2),
      "min", heart.min(), "max", heart.max())
print("First three in beats/second:", heart[:3] / 60)

# ---------------- Task 3 ----------------
title("Task 3")
for n in (1_000_000, 100_000):
    lat = np.random.default_rng(42).uniform(5, 250, n)
    def loop():
        out = []
        for v in lat:
            out.append((v / 1000.0) ** 2)
        return out
    def vec():
        return (lat / 1000.0) ** 2
    a = timeit.timeit(loop, number=1)
    b = timeit.timeit(vec, number=3) / 3
    print(f"n={n}: loop {a:.4f} s, vectorized {b:.5f} s, speed-up {a/b:.1f}x")
volts_mv = np.random.default_rng(1).uniform(100, 5000, 1_000_000)
power = (volts_mv / 1000.0) ** 2 / 10.0   # P = V^2 / R, R = 10 ohm
print("New case: first three powers (W):", power[:3])

# ---------------- Task 4 ----------------
title("Task 4")
for approx in (1.414, 1.4142):
    ae = abs(np.sqrt(2) - approx)
    print(f"approx {approx}: abs error {ae:.8f}, relative {ae/np.sqrt(2):.6%}")
total = 0.0
for _ in range(10):
    total += 0.1
print("0.1 added ten times:", repr(total), "== 1.0 ?", total == 1.0,
      "isclose ?", np.isclose(total, 1.0))

# ---------------- Task 5 ----------------
title("Task 5")
def transform(points, deg, scale):
    ang = np.deg2rad(deg)
    R = np.array([[np.cos(ang), -np.sin(ang)], [np.sin(ang), np.cos(ang)]])
    T = R @ scale
    return points @ T.T, np.linalg.det(T)
square = np.array([[0, 0], [1, 0], [1, 1], [0, 1.]])
print("90 degrees:\n", transform(square, 90, np.diag([2.0, 1.5]))[0])
tri = np.array([[0, 0], [4, 0], [0, 3.]])
pts, det = transform(tri, 90, np.diag([0.5, 0.5]))
print("New case triangle:\n", pts, "\ndeterminant", round(det, 4))

# ---------------- Task 6 ----------------
title("Task 6")
A = np.array([[4, 2], [8, 12.]])
print("Totals 24 CPU, 80 GB:", np.linalg.solve(A, [24, 80]))
bake = np.array([[2, 1], [1, 3.]])
print("New case bakery (cakes, pies):", np.linalg.solve(bake, [10, 15]))

# ---------------- Task 7 ----------------
title("Task 7")
A = np.array([[4, -1, 0], [-1, 4, -1], [0, -1, 3.]])
print("First vector [20,10,10]:", np.linalg.solve(A, [20, 10, 10]))
A2 = np.array([[3, -1, 0], [-1, 3, -1], [0, -1, 3.]])
lu, piv = lu_factor(A2)
for b in ([2, 1, 2], [4, 1, 4], [3, 0, 3]):
    x = lu_solve((lu, piv), np.array(b, float))
    print("New case", b, "->", x, "residual", np.linalg.norm(b - A2 @ x))

# ---------------- Task 8 ----------------
title("Task 8")
def jacobi(A, b, tol):
    D = np.diag(A); R = A - np.diagflat(D); x = np.zeros_like(b); n = 0
    for _ in range(500):
        xn = (b - R @ x) / D; n += 1
        if np.linalg.norm(xn - x, np.inf) < tol:
            return xn, n
        x = xn
    return x, n
def gauss_seidel(A, b, tol):
    x = np.zeros_like(b); n = 0
    for _ in range(500):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        n += 1
        if np.linalg.norm(x - old, np.inf) < tol:
            return x, n
    return x, n
A5 = 2*np.eye(5) - np.eye(5, k=1) - np.eye(5, k=-1)
b5 = np.array([100, 0, 0, 0, 20.])
for tol in (1e-8, 1e-4):
    print(f"tol {tol}: Jacobi {jacobi(A5, b5, tol)[1]} iterations, "
          f"Gauss-Seidel {gauss_seidel(A5, b5, tol)[1]} iterations")
A4 = 2*np.eye(4) - np.eye(4, k=1) - np.eye(4, k=-1)
b4 = np.array([50, 0, 0, 10.])
xj, nj = jacobi(A4, b4, 1e-8)
print("New case rod:", xj, "Jacobi", nj, "Gauss-Seidel", gauss_seidel(A4, b4, 1e-8)[1])

# ---------------- Task 9 ----------------
title("Task 9")
def centrality(A):
    w, v = np.linalg.eig(A)
    i = np.argmax(w.real)
    d = np.abs(v[:, i].real)
    return round(w[i].real, 4), d / d.sum()
A = np.array([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0.]])
print("Original:", centrality(A))
A[0, 3] = A[3, 0] = 1
print("With A-D link:", centrality(A))
print("New case relay chain:", centrality(np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0.]])))

# ---------------- Task 10 ----------------
title("Task 10")
for c in (10, 20):
    f = lambda T: T - 25 - c * np.exp(-T / 20)
    r = root_scalar(f, bracket=[20, 40], method="bisect", xtol=1e-10).root
    print(f"constant {c}: equilibrium {r:.4f} C")
profit = lambda q: 8 * np.sqrt(q) - 0.5 * q - 20
print("New case break-even quantity:",
      round(root_scalar(profit, bracket=[1, 50], method="bisect", xtol=1e-10).root, 4))

# ---------------- Task 11 ----------------
title("Task 11")
def irr(cf):
    npv = lambda r: sum(c / (1 + r) ** t for t, c in enumerate(cf))
    d = lambda r: sum(-t * c / (1 + r) ** (t + 1) for t, c in enumerate(cf) if t > 0)
    return root_scalar(npv, fprime=d, x0=0.10, method="newton", xtol=1e-12).root
print(f"Original IRR {irr([-10000, 3000, 3500, 4000, 2500]):.4%}")
print(f"Investment 9000 IRR {irr([-9000, 3000, 3500, 4000, 2500]):.4%}")
print(f"New case loan rate {irr([-5000, 1400, 1400, 1400, 1400]):.4%}")

# ---------------- Task 12 ----------------
title("Task 12")
def solve_pair(eqs, guesses):
    for g in guesses:
        s = root(eqs, g)
        print("  guess", g, "->", s.x, "converged:", s.success)
print("Radius squared 9:")
solve_pair(lambda z: [z[0]**2 + z[1]**2 - 9, z[1] - (z[0]**2 - 1)], ([1., 1.], [-1., 1.]))
print("New case line y = x + 1 and parabola y = x^2 - 1:")
solve_pair(lambda z: [z[1] - (z[0] + 1), z[1] - (z[0]**2 - 1)], ([3., 3.], [-2., 0.]))