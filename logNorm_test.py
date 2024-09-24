import statistics as st #pdf_of_normal_distr, does_data_follow_a_normal_distr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
#import statistics
import math
import sys

mean=4.4040
std=0.6444 #sigma o std
var=std*std

n = 2000 #sample number
num_bins = 100
#width_of_bin = 0.01


# Generate log-norm
###################
print("Generate log-norm given mean, std, and n")
s       = np.random.lognormal(mean, std, n)
s_log10 = np.log10(s) #s = np.log(s) o #s = np.log2(s)
s_log10_norm  = (s_log10-np.mean(s_log10))/np.std(s_log10) #Normalize for Kolmogorov/Smirnov Test s=(s-mean)/std
print("length of s:", len(s))
if 0:
    #print(s)
    print("mean de s:", s.mean())
    print("log de mean de s:", np.log(s.mean()), math.e, math.e ** (np.log( s.mean() )))
    print("log2 de mean de s:", np.log2(s.mean()), 2, 2 ** (np.log2(s.mean())))
    print("log10 de mean de s:", np.log10(s.mean()), 10, 10**np.log10( s.mean() ))
if 1:
    st.does_data_follow_a_normal_distr(s_log10_norm) # s_log10: Kolmogorov-S does not work
                                                     # data needed to be normalized
sys.exit()


# see distribution
plt.title("Histograms")
plt.hist(s_log10_norm, bins=num_bins, alpha=0.8, edgecolor='none')
#
hist_log10, bin_edges_log10 = np.histogram(s_log10, bins=num_bins)
bin_centers_log10 = np.mean(np.vstack([bin_edges_log10[0:-1],bin_edges_log10[1:]]), axis=0)
step_hist_log10 = (max(bin_edges_log10)-min(bin_edges_log10))/(num_bins)
# a way of plotting s_log10
if 1:
    plt.hist(s_log10, bins=num_bins, alpha=0.5, edgecolor='none')
else:
    plt.bar(bin_centers_log10, hist_log10, width=step_hist_log10, edgecolor='none', alpha=0.8, color="black")
#
# plot model of s_log10 (with the area of the histogram of s_log10 observations)
my_pdf_of_log10 = st.pdf_of_normal_distr(bin_centers_log10, np.mean(s_log10), np.std(s_log10))
area_log10 = 0
area_my_pdf_of_log10 = 0
for i in hist_log10:
    area_log10 += i*step_hist_log10
for i in my_pdf_of_log10:
    area_my_pdf_of_log10 += i*step_hist_log10
my_pdf_of_log10_for_plotting = (area_log10/area_my_pdf_of_log10)*my_pdf_of_log10
plt.plot(bin_centers_log10, my_pdf_of_log10_for_plotting, linewidth=1, color='r')
plt.axis('tight')
plt.show()
