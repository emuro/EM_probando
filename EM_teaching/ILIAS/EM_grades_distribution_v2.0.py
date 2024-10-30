# primero le quito la repeticion del header para cada estudiante, dejando solo la cabecera
# elimino con emacs una columna vacia.

# p3 see_results.py ./final_grades2.tsv

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re


print(sys.argv)
if len(sys.argv) != 2:
    print("\nShow columns. Examples of use:")
    print("# Up to the line:")
    print("python3", sys.argv[0], "csvInputFileName_withCompletePath")
    sys.exit()
    
# reading csv file 
df = pd.read_csv(sys.argv[1], sep="\t", comment='#', encoding='unicode_escape')
print(df.head())
print(df.columns)

#sys.exit("out")

df["Noten"] = df["Noten"].str.replace('nb', '5.', regex=True)
df["Noten"] = df["Noten"].str.replace(',', '.', regex=True).astype('category')
print(df["Noten"].value_counts())
df = df.sort_values("Noten", ascending=True)

num_students = df.shape[0]
bins = 12
df["Noten"].hist(bins = np.arange(bins) - 0.5, edgecolor='black', linewidth=1.2)
plt.xticks(range(bins))
plt.yticks(np.arange(0., 120.+1, 10.0))
title = "Mod4.2 distribution of results for " + str(num_students) + " students"
plt.title(title)
plt.ylabel('Counts')
plt.xlabel("Mark")
plt.show()
