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