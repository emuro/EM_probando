import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import sys

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

def Lg(t):
   k = 0.0013561601380
   return 452 * np.exp(k * (3700-t))

def mya(Lg):
   k = 0.0013561601380
   return (np.log(452) - np.log(Lg) + k * 3700)/k


start = 0
step  = 500
end   = 3500 #should be 3700
count = int (end/step) + 1
stop  = start + (step*count)
t = np.linspace(start, end, count)
t = np.append(t, [3700.])
end   = 3700
print ("t:", t)
print ("length:", Lg(t))
df = pd.DataFrame({"t": t, "length": Lg(t)})
print(df)

plt.plot(t, Lg(t), '--', markersize=1, color='pink', label='log')
plt.plot(t, Lg(t), '.', markersize=5, color='red', label='log')
plt.title("Mean gene length dependence with time")
plt.xlabel("t [Mya]")
plt.ylabel("$<L_{g}(t)>$ [nt]")
#plt.show()

# Puedo mostrar automaticamente la especie mas cercana a esa distancia. Mirar:
# https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array



LgMin            = np.array([6328.07101316192, 20276.2457972491, 24989.2293819869,
                             22116.5949857129, 31702.7753590552,
                             36854.496308828]).round(decimals=1)
LgMax            = np.array([71400.6717131956, 31443.2530905547, 57440.5056160653,
                             62135.9179115892, 31702.7753590552,
                             68287.0898077693]).round(decimals=1) 
LgMiddle           = (LgMax + LgMin) / 2.
LgMiddle = LgMiddle.round(decimals=1)
clades = np.array(["fishes", "birds", "reptiles", "mammals",
                   "anfibios", "primates"])

origin_mya_googleQuickSearch = np.array([530., 165., 320., 225., 400., 55.]).round(decimals=1) 

time_LgMin = mya(LgMin).round(decimals=1)
time_LgMax = mya(LgMax).round(decimals=1)
time_LgMiddle = mya(LgMiddle).round(decimals=-1)
time_LgMin = mya(LgMin).astype(int)
time_LgMax = mya(LgMax).astype(int)
time_LgMiddle = mya(LgMiddle).astype(int)
df2 = pd.DataFrame({"clades": clades,
                  "LgMin":  LgMin,
                  "LgMax":  LgMax,
                  "LgMiddle": LgMiddle,
                  "time_LgMin": time_LgMin,
                  "time_LgMax": time_LgMax,
                  "time_LgMiddle": time_LgMiddle,
                  "origin_mya_googleQuickSearch": origin_mya_googleQuickSearch}
                  )
                                  
print(df2[["clades", "LgMin", "LgMax", "LgMiddle"]])
print(df2[["clades", "time_LgMiddle", "time_LgMin", "time_LgMax", "origin_mya_googleQuickSearch"]])


