import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import sys

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

def L_t(L0, mu):
   return L0*(np.exp((mu-1)*t))

def Tau_L(L0, mu):
   return ( np.log(L/L0) / ((mu - 1) * L) )


L0 = 554
mu = 1.00101
t0 = 0
tend = 4000
count = 4000#10000

t = np.linspace(t0, tend, count)
t = np.flip(t)
if False:
   print ("t:", t)
   print ("L_t:", L_t(L0, mu))
   df = pd.DataFrame({"t": t, "L(t)": L_t(L0, mu)})
   print(df)
   #sys.exit()

# <L(t)>
if False:
   plt.plot(t, L_t(L0, mu), '.', markersize=0.1, color='black', label='log')
   plt.title("<Length>")
   plt.xlabel("t")
   plt.ylabel("<L(t)>")
   plt.show()

#plt.plot(t, L_t(L0, mu)/t, '.', markersize=0.01, color='black', label='log')
#plt.title("<Speed>")
#plt.xlabel("t")
#plt.ylabel("<v(t)>")
#plt.show()

plt.plot(t, t/L_t(L0, mu), '.', markersize=0.1, color='black', label='log')
plt.title("Tau(t)")
plt.xlabel("t (Mya)")
plt.ylabel("t/<L(t)>")
plt.show()


start = L0 + 1 #1.001
end   =70000 
count = 70000 #10000
L = np.linspace(L0+1, end, count)
L = np.flip(L)
plt.plot(L, Tau_L(L0, mu), '.', markersize=0.1, color='black', label='log')
plt.title("Tau(<L>)")
plt.xlabel("<L>")
plt.ylabel("Tau")
plt.show()
