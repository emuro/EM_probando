
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import seaborn as sns

np.random.seed(16)
if 1:
    x1=np.random.normal(size=20)
    x2=np.random.normal(size=200)
    x3=np.random.beta(a=1,b=5,size=20)
    x4=np.random.beta(a=1,b=5,size=200)
    fig, axs = plt.subplots(1, 4, figsize=(20, 5))
    sns.distplot(x1, hist=False, ax=axs[0])
    axs[0].set_title('First sample')
    sns.distplot(x2, hist=False, ax=axs[1])
    axs[1].set_title('Second sample')
    sns.distplot(x3, hist=False, ax=axs[2])
    axs[2].set_title('Third sample')
    sns.distplot(x4, hist=False, ax=axs[3])
    axs[3].set_title('Fourth sample')
    plt.show()

s = 5000
n = 100
p_val = 0.05
tests_names = "Shapiro,Kolmogorov-Smirnov,Dagostino-Pearson".split(",")
refute = [0,0,0]
for i in range(n):
    if 1:
        x1 = np.random.normal(size=s)
    else:
        x1 = np.random.beta(a=1,b=5,size=s)
    tests = []
    tests.append(scipy.stats.shapiro(x1))
    tests.append(scipy.stats.kstest(x1, "norm"))
    tests.append(scipy.stats.normaltest(x1))
    for i, r in enumerate(tests):
        if r.pvalue < p_val:
            refute[i] += 1

print(tests_names, "rechazan la hipótesis en", refute , "veces de", n)
