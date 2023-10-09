import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import sys

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

def f(a, b):
   return 4 * ( 1 - ( b*(np.log(b)-1) - a*(np.log(a)-1) )/((b-a) * (b+a-2)) )


start = 1.0001
end   = 2 
count = 10000


a = 1
b = np.linspace(start, end, count)
b = np.flip(b)
print ("b:", b)
print ("exponent:", f(a, b))
df = pd.DataFrame({"b": b, "exponent": f(a, b)})
print(df)
#sys.exit()


#plt.plot(b, f(a, b), '--', markersize=0.05, color='pink', label='log')
plt.plot(b, f(a, b), '.', markersize=0.005, color='red', label='log')
plt.title("Exponent (a=1)")
plt.xlabel("b")
plt.ylabel("beta")
plt.show()

# Puedo mostrar automaticamente la especie mas cercana a esa distancia. Mirar:
# https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
