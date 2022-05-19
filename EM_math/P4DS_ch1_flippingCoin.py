# Python code to generate a geometric sequence
import numpy as np
import math
import matplotlib.pyplot as plt

p = 1/2
if 0:
    n = np.arange(1,10)
    X = np.power(p,n)
else:
    n = list(range(1,10))
    X = [math.pow(p, i) for i in n]
plt.bar(n,X)
plt.show()
