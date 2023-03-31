import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(6, 6),
                        layout="constrained")
# add an artist, in this case a nice label in the middle...
x=[1,2,3]
c=[["r", "g"], ["b", "black"]]
for row in range(2):
    for col in range(2):
        #axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
        #                       transform=axs[row, col].transAxes,
        #                       ha='center', va='center', fontsize=18,
        #                       color='darkgrey')
        axs[row, col].plot(x, x, color=c[row][col])
fig.suptitle('plt.subplots()')
plt.show()
