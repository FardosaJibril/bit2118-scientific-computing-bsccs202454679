# BIT 2118 Scientific Computing

Name: Fardosa Jibril | Reg No: bsccs202454679

## Task 2: NumPy Arrays and Numerical Computation

**Inputs and operation:** The input is an array of 24 hourly temperatures in °C. The program computes the mean, minimum and maximum, and converts every value to Fahrenheit with F = 1.8C + 32 in one vectorized expression.

**Parameter change:** I changed the peak reading from 29.4 to 35.0. The maximum became 35.0 °C and the mean rose from 23.12 to about 23.35 °C. The mean rose by only (35.0 - 29.4)/24 ≈ 0.23 because one reading is only 1/24 of the total.

**Output interpretation:** The station's average temperature over the day was 23.12 °C, ranging from a cool 17.5 °C in the early morning to 29.4 °C in the early afternoon. The first six Fahrenheit values are about 65.3, 64.4, 64.0, 63.5, 64.2 and 66.2 °F.

**New related case:** Heart-rate readings (bpm) taken every hour for 24 hours. Assumption: readings are accurate and evenly spaced. I computed the mean, min and max with the same NumPy functions, and used a vectorized expression to convert to beats per second (bpm / 60). The mean shows the resting level over the day, and the max shows the most active hour.

## Task 3: Mathematical Functions and Vectorization

**Inputs and operation:** The input is 1,000,000 random latency values between 5 and 250 ms (seed 42). The program converts each to seconds (÷1000) and squares it, once with a Python loop and once with a vectorized NumPy expression.

**Parameter change:** I changed the array size from 1,000,000 to 100,000. The loop time dropped to 0.0233 s and the vectorized time to 0.0007 s, so the speed-up was 35.6x times. Smaller arrays take less time for both methods.

**Output interpretation:** The loop took 0.1575 s and the vectorized version 0.0040 s, a speed-up of about 39.9x. Vectorization is faster because NumPy runs the operation in optimized compiled code instead of executing Python instructions one value at a time. The first five squared latencies (for example 0.0379 s² for the first reading) are small because latencies of a few hundred milliseconds are only fractions of a second.

**New related case:** Convert one million sensor voltages from millivolts to volts and compute power P = V²/R with R = 10 ohms. Assumption: a constant resistance. I timed the loop against the vectorized form again and found vectorization to be much faster, so it is the better choice for large datasets.

## Task 4: Floating-Point Arithmetic and Numerical Errors

**Inputs and operation:** The inputs are 0.1 + 0.2 compared with 0.3, the values √2 and 1.414, and small values of x (1e-4, 1e-8, 1e-12). The program compares numbers exactly and with a tolerance, computes absolute and relative error, and compares two formulas for (√(1+x) - 1)/x.

**Parameter change:** I changed the approximation from 1.414 to 1.4142. The absolute error fell from about 0.00021356 to about 0.00001356, and the relative error fell from 0.0151% to about 0.00096%. More correct digits mean a smaller error.

**Output interpretation:** 0.1 + 0.2 prints 0.30000000000000004, so the exact comparison is False, while np.isclose gives True. Computers store 0.1 and 0.2 approximately in binary. In the last part, the direct formula loses accuracy as x gets very small because it subtracts two nearly equal numbers (catastrophic cancellation), while the rearranged stable formula stays close to 0.5.

**New related case:** Add 0.1 ten times in a loop and compare the total with 1.0. Assumption: ordinary double-precision floats. The total prints 0.9999999999999999, so `total == 1.0` is False and `np.isclose(total, 1.0)` is True. The lesson for banking-style sums is to use a tolerance (or integer cents) rather than exact equality.
## Task 5: Matrix Algebra and Matrix Operations

**Inputs and operation:** The inputs are the four corners of a unit square, a 45° rotation matrix and a scaling matrix (x by 2, y by 1.5). The program multiplies the two matrices to get one transformation and applies it to every point by matrix multiplication.

**Parameter change:** I changed the angle from 45° to 90°. The point (1, 0) moved to (0, 2) instead of (1.41, 1.41), and (1, 1) moved to (-1.5, 2). The determinant stayed 3.0, because rotation does not change area and the scaling gives 2 × 1.5 = 3.

**Output interpretation:** The square becomes a rotated parallelogram. The determinant of 3.0 means every area is multiplied by 3. A positive determinant means the shape is not mirrored.

**New related case:** A triangle with corners (0,0), (4,0), (0,3) is rotated 90° and scaled by 0.5 in both directions. Assumption: the scale is uniform. The new corners are (0,0), (0,2) and (-1.5,0), and the determinant is 0.25, so the area shrinks to a quarter. Tiny values like 1e-16 in the output are round-off error from computing cos(90°).

## Task 6: Solution of Systems of Linear Equations

**Inputs and operation:** The inputs are the CPU and memory use per server type (matrix A) and the observed totals (vector b = [20, 72]). The program solves Ax = b with np.linalg.solve and checks the residual b - Ax.

**Parameter change:** I changed the totals to 24 CPU units and 80 GB. The solution became 4 Type A and 4 Type B servers, instead of 3 and 4. More resource use means more servers.

**Output interpretation:** There are 3 Type A servers and 4 Type B servers. The residual norm is essentially zero (around 1e-15), so the solution reproduces the observed totals.

**New related case:** A bakery makes cakes (x) and pies (y). Cakes need 2 oven-hours and 1 labour-hour, and pies need 1 oven-hour and 3 labour-hours. There are 10 oven-hours and 15 labour-hours available. Assumption: all the hours are fully used. The solution is 3 cakes and 4 pies, and the residual is about zero.

## Task 7: Gaussian Elimination and LU Decomposition

**Inputs and operation:** The inputs are a 3×3 coefficient matrix A and three different measurement vectors. The program factors A once with lu_factor, then solves for each vector with lu_solve.

**Parameter change:** I changed the first measurement vector from [15, 10, 10] to [20, 10, 10]. The solution changed from [5, 5, 5] to about [6.34, 5.37, 5.12]. A larger first measurement raises x the most, because it is directly tied to the first equation.

**Output interpretation:** Each solution gives the unknowns for one measurement set, and the first one is [5, 5, 5]. The residual norms are around 1e-15, so the solutions are accurate and match the direct solve. Factoring once and reusing it saves work when A stays the same.

**New related case:** A smaller coupled system with A = [[3,-1,0],[-1,3,-1],[0,-1,3]] and three new measurement vectors. Assumption: each unknown depends on its neighbours. The first vector [2, 1, 2] gives [1, 1, 1], and the other two also solve with residuals near zero.

## Task 8: Iterative Methods for Linear Systems

**Inputs and operation:** The inputs are a 5×5 tridiagonal matrix, a right-hand side with boundary temperatures of 100 °C and 20 °C, and a tolerance of 1e-8. Jacobi and Gauss-Seidel start from zeros and repeatedly improve the estimate until the change is below the tolerance.

**Parameter change:** I changed the tolerance from 1e-8 to 1e-4. Jacobi iterations fell from about 150 to about 85 and Gauss-Seidel from about 75 to about 42. A looser tolerance lets the methods stop earlier, so fewer iterations are needed, but the temperatures are less accurate (the final change is only below 0.0001 instead of 0.00000001). Gauss-Seidel still needed about half as many iterations as Jacobi.

**Output interpretation:** Both methods give about 86.67, 73.33, 60.00, 46.67 and 33.33 °C, which matches the direct solution. The temperature falls steadily from the hot boundary (100 °C) to the cold boundary (20 °C). Jacobi needed about 150 iterations and Gauss-Seidel about 75, so Gauss-Seidel converged about twice as fast. On the graph, the horizontal axis is the iteration number and the vertical axis is the maximum change in any temperature between iterations, on a log scale. Both lines fall almost straight down from about 50 to below 1e-8, which shows steady convergence. The Gauss-Seidel line is steeper because it uses the newest values immediately within each iteration, while Jacobi waits for the next one.

![Task 8 convergence](task8_convergence.png)

**New related case:** A heated rod with four interior points, a left boundary of 50 °C and a right boundary of 10 °C. Assumption: steady state with no heat source. The temperatures are about 42, 34, 26 and 18 °C, a straight-line drop.
## Task 9: Eigenvalues and Eigenvectors

**Inputs and operation:** The input is a 4×4 adjacency matrix for a network of nodes A, B, C and D (1 means the nodes are linked). The program finds the eigenvalues and eigenvectors with np.linalg.eig, takes the dominant eigenvector and normalizes it so the scores add up to 1.

**Parameter change:** I added a link between A and D. The dominant eigenvalue rose from 2.56 to 3.0, and every node scored 0.25. Every node now has exactly three links, so no node is more important than another.

**Output interpretation:** The dominant eigenvalue is 2.56. B and C score 0.2808 each and A and D score 0.2192 each. B and C are the most influential nodes because each is linked to all three of the other nodes. The verification error is close to zero, so Av = λv holds.

**New related case:** A relay chain A–B–C in which B links the other two. Assumption: links work in both directions. Input data: A = [[0,1,0],[1,0,1],[0,1,0]]. Output: the dominant eigenvalue is 1.4142 and the scores are 0.2929, 0.4142 and 0.2929. Interpretation: the middle node is the most important, because everything passes through it.

## Task 10: Root Finding: Bisection and Fixed-Point Methods

**Inputs and operation:** The input is the heat-balance function f(T) = T - 25 - 10e^(-T/20), a bracket of [20, 40] and a tolerance of 1e-10. Bisection halves the bracket until it finds f(T) = 0. Fixed-point iteration repeats T = 25 + 10e^(-T/20), starting from T = 30.

**Parameter change:** I changed the constant 10 to 20 in both formulas. The equilibrium temperature rose from 27.53 °C to 29.56 °C, and fixed-point iteration needed 17 steps instead of 13. A larger heat term moves the balance point higher and makes the iteration a little slower.

**Output interpretation:** Both methods give an equilibrium temperature of 27.5252 °C, where heat gain equals heat loss. Fixed-point iteration took 13 iterations. On the graph, the horizontal axis is temperature and the vertical axis is the heat-balance function. The curve rises from about -9 at 20 °C to about +14 at 40 °C and crosses zero once, at the dashed vertical line near 27.5 °C. Below that temperature the function is negative and above it the function is positive.

![Task 10 equilibrium](task10_equilibrium.png)

**New related case:** Break-even quantity for a small business, with profit(q) = 8√q - 0.5q - 20, where q is the number of units. Assumption: profit has diminishing returns. Bisection on [1, 50] (profit is -12.5 at q = 1 and positive at q = 50) gives a break-even of 9.62 units. Interpretation: the business starts making a profit after selling about 10 units.

## Task 11: Root Finding: Newton-Raphson and Secant Methods

**Inputs and operation:** The inputs are an investment of 10,000 followed by yearly inflows of 3000, 3500, 4000 and 2500. The program finds the rate at which the net present value is zero (the internal rate of return, IRR), using Newton-Raphson (with the derivative, starting at 0.10) and the secant method (starting at 0.05 and 0.20).

**Parameter change:** I changed the investment from 10,000 to 9,000. The IRR rose from 11.54% to 16.73%. The same inflows from a smaller investment give a higher return.

**Output interpretation:** Both methods give an IRR of 11.5425%. At that discount rate the present value of the inflows equals the investment, so the NPV is essentially zero. If the cost of borrowing is below 11.54%, the project is worthwhile.

**New related case:** A loan of 5,000 repaid with 1,400 each year for 4 years. Assumption: equal yearly payments. Input data: cash flows [-5000, 1400, 1400, 1400, 1400]. Output: the rate that makes the NPV zero is 4.69% per year. Interpretation: that is the yearly interest rate the borrower is paying on this loan.

## Task 12: Polynomial and Nonlinear Equation Solving

**Inputs and operation:** The inputs are the circle x² + y² = 4 and the parabola y = x² - 1, with starting guesses [1, 1] and [-1, 1]. scipy.optimize.root searches for the (x, y) that makes both equations zero.

**Parameter change:** I changed the circle's right-hand side from 4 to 9 (radius 3 instead of 2). The intersections moved from (±1.52, 1.30) to (±1.84, 2.37). A larger circle meets the parabola higher up.

**Output interpretation:** The two guesses converge to (1.5175, 1.3028) and (-1.5175, 1.3028). The residuals are about 1e-13 and Converged is True for both. The circle and parabola are both symmetric about the y-axis, so the two intersections are mirror images of each other.

**New related case:** A drone flies along the parabola y = x² - 1 and crosses a straight road y = x + 1. Assumption: both are in the same plane. Starting from the guesses [3, 3] and [-2, 0], the solver finds the crossing points (2, 3) and (-1, 0), both with Converged True. Check: 2² - 1 = 3 and (-1)² - 1 = 0.