import matplotlib.pyplot as plt



height = [189, 185, 195, 149, 189, 147, 154,  
          174, 169, 195, 159, 192, 155, 191,  
          153, 157, 140, 144, 172, 157, 181,  
          182, 166, 167] 
  
counts, bins, *rest = plt.hist(height, edgecolor="red", bins=5) 
print("counts:\n\t", counts,
      "\nbins:\n\t", bins,
      "\nrest:\n\t", *rest)
plt.show() 
