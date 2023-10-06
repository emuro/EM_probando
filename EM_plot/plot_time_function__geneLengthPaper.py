import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import sys

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

def f(t):
   k = 0.0013561601380
   return 452 * np.exp(k * (3700-t))


start = 0
step  = 500
end   = 3500 #should be 3700
count = int (end/500) + 1
stop  = start + (step*count)
t = np.linspace(start, end, count)
t = np.append(t, [3700.])
end   = 3700
print ("t:", t)
print ("length:", f(t))
df = pd.DataFrame({"t": t, "length": f(t)})
print(df)

plt.plot(t, f(t), '--', markersize=1, color='pink', label='log')
plt.plot(t, f(t), '.', markersize=5, color='red', label='log')
plt.title("Mean gene length dependence with time")
plt.xlabel("t [Mya]")
plt.ylabel("$L_{g}(t)$ [nt]")
plt.show()

# Puedo mostrar automaticamente la especie mas cercana a esa distancia. Mirar:
# https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
