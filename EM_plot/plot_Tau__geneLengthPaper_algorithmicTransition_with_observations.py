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
if True:
   print ("t:", t)
   print ("L_t:", L_t(L0, mu))
   df = pd.DataFrame({"t": t, "L(t)": L_t(L0, mu)})
   print(df)
   

# <L(t)>
if False: #True:
	#df.plot(x="t", y="L(t)", style='.', markersize=0.1, color='black', label="_Hidden_label")
	plt.plot(t, L_t(L0, mu), '.', markersize=0.1, color='black')
	plt.title("<Length>")
	plt.xlabel("t")
	plt.ylabel("<L(t)>")
	plt.show()

# v(t)
if False: #True:
	plt.plot(t, L_t(L0, mu)/t, '.', markersize=0.1, color='black', label='log')
	plt.ylim(0, 100)
	plt.title("<Speed>")
	plt.xlabel("t")
	plt.ylabel("v(t)")
	plt.show()

# Tau(t)
if False: #True:
	plt.plot(t, t/L_t(L0, mu), '.', markersize=0.1, color='black', label='log')
	plt.title("Tau(t)")
	plt.xlabel("t (Mya)")
	plt.ylabel("t/<L(t)>")
	plt.show()


# Tau(<L>)
if False: #True:
	start = L0 + 1 #1.001
	end   = 70000 
	count = 70000 #70000 #10000
	L = np.linspace(L0+1, end, count)
	L = np.flip(L)
	plt.plot(L, Tau_L(L0, mu), '.', markersize=0.1, color='black', label='log')
	plt.title("Tau(<L>)")
	plt.xlabel("<L>")
	plt.ylabel("Tau")
	plt.show()
	#
	print ("L:", L)
	print ("Tau_L:", Tau_L(L0, mu))
	df = pd.DataFrame({"L": L, "Tau_L": Tau_L(L0, mu)})
	print(df)


# Tau(<L>)
start = L0 + 1 #1.001
end   = 70000 
count = 70000 #70000 #10000
L = np.linspace(L0+1, end, count)
L = np.flip(L)
if False: #False:
	plt.plot(L, Tau_L(L0, mu), '.', markersize=0.1, color='black', label='log')
	plt.title("Tau(<L>)")
	plt.xlabel("<L>")
	plt.ylabel("Tau")
	plt.show()
	#
	print ("L:", L)
	print ("Tau_L:", Tau_L(L0, mu))
	df = pd.DataFrame({"L": L, "Tau_L": Tau_L(L0, mu)})
	print(df)


# Tau(<L>) and observations
obs_file = "/home/emuro/git/github/gene_length/main_tables/suppl_tables/gene_length_vs_divergence_time.tsv"
df2 = pd.read_csv(obs_file, sep="\t", comment='#')
#print(df2.columns)
#['#Group', 'Divergence Time with Homo sapiens (Mya)', 'Time from LUCA (Myr - assuming LUCA 3700 Mya)', 'average <L> of the group (bases)', 'average <log L> of the group']

##df2 = df2[['Group of organisms', 'Divergence with human', '<L>']]
df2 = df2[['Group of organisms', 'Time from LUCA', '<L>']]
df2.columns = ['group', 'time', '<L>']
df3 = df2.iloc[3:].copy()
df3['complexity'] = df3['time'] / df3['<L>']
print(df3)

#df3.plot('<L>', 'complexity', color='blue', label='log')
#plt.title("Tau(<L>)")
#plt.xlabel("<L>")
#plt.ylabel("Tau")
#plt.show()


plt.plot(L, Tau_L(L0, mu), '.', markersize=0.1, color='black', label='log')
L = df3['<L>'].to_list()
c = df3['complexity'].to_list()
#plt.plot(L, c, '.', markersize=5., color=['blue', 'green', 'magenta', 'lightcoral', 'salmon', 'red'])
plt.plot(L, c, '.', markersize=7.5, color='salmon')

plt.title("Tau(<L>)")
plt.xlabel("<L>")
plt.ylabel("Tau")
plt.show()
