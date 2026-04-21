"""
Study of Stirling’s approximation for the factorial.

This program compares the exact value of the factorial n! with its
approximation using Stirling’s formula:

    n! ≈ sqrt(2πn) * (n/e)^n

The goal is to analyze how the approximation error behaves as n increases,
using different orders of magnitude.

The program:
- Computes the exact factorial n! using high-precision arithmetic
- Computes Stirling’s approximation
- Compares both values
- Calculates the relative error
- Displays the results in a human-readable table

It shows how the approximation improves as n grows,
illustrating the asymptotic nature of Stirling’s formula.
"""

import pandas as pd
import mpmath as mp
from tabulate import tabulate

mp.mp.dps = 100

def exact_factorial(n):
    return mp.factorial(n)

def stirling(n):
    n = mp.mpf(n)
    return mp.sqrt(2 * mp.pi * n) * (n / mp.e) ** n

ns = [1, 5, 10, 20, 50, 100]

rows = []

for n in ns:
    real = exact_factorial(n)
    approx = stirling(n)
    error_abs = abs(real - approx)
    error = error_abs / real

    rows.append([
        n,
        str(real),
        str(approx),
        f"{float(error_abs):.3e}",
        f"{float(error):.3e}"
    ])

df = pd.DataFrame(rows, columns=[
    "n",
    "n! exacto",
    "Stirling",
    "error absoluto",
    "error relativo"
])

print(tabulate(df, headers="keys", tablefmt="fancy_grid", showindex=False))
