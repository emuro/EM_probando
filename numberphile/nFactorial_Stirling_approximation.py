"""Descubro un error bajo hasta 700 y sube al 1% ...y se mantiene ab infinitum (entiendo)
"""

import math
import numpy as np
import scipy.special

import matplotlib.pyplot as plt
from time import time
#from decimal import *
from decimal import Decimal


def stirling_approximation(n):
    """ approximates n!
    https://www.youtube.com/watch?v=6ofIBoWGc7k

    :param n: int
    :return: n**n * math.exp(-1*n) * math.sqrt(2*math.pi*n)
    """
    return Decimal(n**n) * Decimal(math.exp(-1*n)) * Decimal(math.sqrt(2*math.pi*n))

if 0:
    n = 100
    start_t = time()
    print(math.factorial(n))
    math_t = time() - start_t
    print(np.math.factorial(n))
    np_t = time() - math_t
    print(scipy.special.factorial(n))
    scipy_t = time() - np_t
    approx = stirling_approximation(n)
    print(approx)
    stirling_t = time() - scipy_t

    print("\n", math_t, np_t, scipy_t, sep="\n")
    print(stirling_t)

max_n = 1500
x, f, s, e =  [[] for x in range(4)]
tmp_f = 1
for i in range(1, max_n):
    x.append(i)
    tmp_f *= i
    f.append(tmp_f)
    s.append(stirling_approximation(i))
    e.append(abs(f[-1] - s[-1])/f[-1])
x_i = np.array(x)
y_f = np.array(f)
y_s = np.array(s)
y_e = np.array(e)
#plt.plot(x, y_f, color='b')
#plt.plot(x, y_s, color='r')
plt.plot(x, y_e, marker='.', color='g')
plt.show()

