import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys

x = np.arange (0.1, 100, 0.1)
y = np.log10(x)

plt.figure(figsize=(6, 6), layout='constrained')
plt.plot(x, y, '.', markersize=0.3, color='black', label='log')  # on the (implicit) axes
#plt.plot(x, x**2, label='quadratic') 
#plt.plot(x, x**3, label='cubic')

if 0: # normal 
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Function Plot")
    plt.legend()
    plt.show()
else: # y log-scale
    ax = plt.gca()
    plt.ylabel('LOGARITHMIC SCALE')
    plt.yscale('log')
    plt.minorticks_on
    ax.yaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.yaxis.set_minor_formatter(matplotlib.ticker.ScalarFormatter())
    plt.autoscale(enable=True, axis='y')
    plt.show()
