# primero le quito la repeticion del header para cada estudiante, dejando solo la cabecera

# p3 see_results.py /home/emuro/Dropbox/current/teaching/Undergrad_Modul4-2_Sept2023/exams/1stExam_SoSe_29Sept2023/Klausur_module_4-2_Sose_2023_1.Klausur_results.csv_Klausur_module_4-2_Sose_2023_1.Klausur_results.csv

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
df = pd.read_csv(sys.argv[1], sep=";")
print(df.head())
print(df.columns)



df["Test Results in Marks"] = df["Test Results in Marks"].str.replace('nicht bestanden', '5.', regex=True)
df["Test Results in Marks"] = df["Test Results in Marks"].str.replace(',', '.', regex=True).astype('category')
print(df["Test Results in Marks"].value_counts())
df = df.sort_values("Test Results in Marks", ascending=True)

num_students = df.shape[0]
bins = 12
df["Test Results in Marks"].hist(bins =
                                 np.arange(bins) - 0.5, edgecolor='black', linewidth=1.2)
plt.xticks(range(bins))
plt.yticks(np.arange(0., 120.+1, 10.0))
title = "Mod4.2 distribution of results for " + str(num_students) + " students"
plt.title(title)
plt.ylabel('Counts')
plt.xlabel("Mark")
plt.show()
