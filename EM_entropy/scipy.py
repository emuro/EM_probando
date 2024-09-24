import numpy as np
import pandas as pd
from scipy.stats import entropy
from matplotlib import pyplot as plt



base = 2  # work in units of bits
if 0:
    pk = np.array([1/2, 1/2])  # fair coin
    H = entropy(pk, base=base)
    print(H)


p1_np = np.array([])  # fair coin
h_np = np.array([])   
for i in np.arange(0., 1.001, 0.01):
    p1 = i
    p2 = 1 - p1
    pk = np.array([p1, p2])  # fair coin
    h = entropy(pk, base=base)
    print(pk, h, sep="\t")
    if 0:
        print("\t\t", -np.sum(pk * np.log(pk)) / np.log(base) )
    p1_np = np.append(p1_np, [p1])
    h_np  = np.append(h_np, [h])
#df = pd.DataFrame({"p1": p1_np, "h": h_np})

#plt.plot(p1_np, h_np, '--', markersize=1, color='pink', label='log')
plt.plot(p1_np, h_np, '.', markersize=5, color='red', label='log')
plt.title("Entropy in coin tossing")
plt.xlabel("p1")
plt.ylabel("$H(X)$")
plt.show()
