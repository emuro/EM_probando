import math
import numpy as np
import pandas as pd
from IPython.display import display
from matplotlib import pyplot as plt
import matplotlib
import seaborn as sns
import sys


plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

def Tau(l):
   mu = 1.00101
   L0 = 554
   return np.log(l/L0) /((mu - 1)*l) 


start = 554
step  = 10
end   = 68000 
count = int (end/step) + 1
stop  = start + (step*count)
l = np.linspace(start, end, count)
l = np.append(l, [68287.])  #human
if 0:
   print ("l:", l)
   print ("Tau:", Tau(l))
   df = pd.DataFrame({"l": l, "Tau": Tau(l)})
   display(df)


plt.plot(l, Tau(l), '--', markersize=2, color='red', label='Theoretical')
plt.title("Algorithmic complexity") #" dependance with the mean gene length")
plt.xlabel("<L> [nt]")
TAU = "τ"
plt.ylabel("%s(<L>) [Mya/nt]" % TAU)


# get and plot observations
#
BOOL_OBSERVATIONS = True
if BOOL_OBSERVATIONS:
	#obs_file = "/home/emuro/git/github/gene_length/main_tables/suppl_tables/gene_length_vs_divergence_time.tsv"
	obs_file = "my_gene_length_vs_divergence_time.tsv"
	df2 = pd.read_csv(obs_file, sep="\t", comment='#')
	df2 = df2[['Group of organisms', 'Time from LUCA', '<L>']]
	df2.columns = ['group', 'time', '<L>']
	df3 = df2.iloc[3:].copy()
	df3['complexity'] = df3['time'] / df3['<L>']
	print(df3)
	
	
	
	
	L = df3['<L>'].to_list()
	c = df3['complexity'].to_list()
	group_labels = ['Fungi', 'Viridiplantae', 'Arthropoda', 'Actinopterygii', 'Aves', 'Mammalia (except Primates)', 'Primates']
	group_colors = ['lightskyblue', "lightgreen", 'plum', 'lightpink', 'salmon', 'tomato', 'orangered']
	sns.scatterplot(x=L, y=c, hue=group_labels, palette=group_colors)
	plt.legend(loc='upper right', fontsize="8", edgecolor="white" )

BOOL_LOGARITHMIC_SCALE = True
if BOOL_LOGARITHMIC_SCALE:
	ax = plt.gca()
	plt.xlabel('<L> [nt]')
	plt.xscale('log')
	#plt.minorticks_on
	ax.xaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
	ax.xaxis.set_minor_formatter(matplotlib.ticker.ScalarFormatter())
	#ax.tick_params(axis='x', rotation=55)
	ax.tick_params(axis='x', which='major', length=6, rotation=55)
	ax.tick_params(axis='x', which='minor', length=5, color='b', rotation=55)
	plt.autoscale(enable=True, axis='x')

plt.show()

