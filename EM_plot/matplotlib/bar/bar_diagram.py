import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file_name = "./tree_age.tsv"

# get dataframe
data = pd.read_csv(file_name, sep="\t")
print(data.columns)
print(data)
#data["Baumart"] = data["Baumart"].astype("category")
print(data.dtypes)


# plot
fig, ax = plt.subplots()
ax.bar(data.Baumart, data.Jahre)
ax.set_ylabel("Edad en años")
ax.set_xlabel("Árbol")
ax.set_title("Edad de distintos tipos de árboles")
#ax.legend(title="Árbol")
plt.show()
