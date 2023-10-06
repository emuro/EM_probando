import math
import numpy as np
import pandas as pd
from IPython.display import display
from matplotlib import pyplot as plt
import matplotlib
import sys


plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

def Tau(l):
   k = 0.0013561601380
   L0 = 452
   return np.log(l/L0) /(k*l)   #452 * np.exp(k * (3700-t))


start = 452
step  = 100
end   = 68000  #human
count = int (end/step) + 1
stop  = start + (step*count)
l = np.linspace(start, end, count)
l = np.append(l, [68287.])
end   = 68287
#print ("l:", l)
#print ("Tau:", Tau(l))
df = pd.DataFrame({"l": l, "Tau": Tau(l)})
display(df)

plt.plot(l, Tau(l), '--', markersize=1, color='gray', label='log')
plt.plot(l, Tau(l), '.', markersize=3, color='red', label='log')
plt.title("Characteristic time dependance with Mean gene length")
plt.xlabel("l [nt]")
plt.ylabel("Tau$(L_{g})$ [Mya/nt]")

BOOL_LOGARITHMIC_SCALE = True
if BOOL_LOGARITHMIC_SCALE:
	ax = plt.gca()
	plt.xlabel('l [nt]')
	plt.xscale('log')
	#plt.minorticks_on
	ax.xaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
	ax.xaxis.set_minor_formatter(matplotlib.ticker.ScalarFormatter())
	#ax.tick_params(axis='x', rotation=55)
	ax.tick_params(axis='x', which='major', length=6, rotation=55)
	ax.tick_params(axis='x', which='minor', length=5, color='b', rotation=55)
	plt.autoscale(enable=True, axis='x')

plt.show()

