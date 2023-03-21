import pandas as pd
from scipy.spatial import distance_matrix
import sys
import numpy as np
# Importing necessary libraries
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceMatrix, DistanceTreeConstructor

def from_square_ndarray_to_matrix_for_distanceMatrix(ndarray):
    if ndarray.shape[0] != ndarray.shape[1]:
        print("Error!")
    dim = ndarray.shape[0]
    aux_1d = ndarray.tolist()
    new_1d = []
    for i in range(0, dim):
        new_1d.append([]) 
        for j in range(0, i+1):
            new_1d[i].append(ndarray[i][j])
    print(new_1d)
    return new_1d


data = [[5, 7], [1, 3], [5, 8]]
ctys = ['Boston', 'Phoenix', 'New York']
df = pd.DataFrame(data, columns=['xcord', 'ycord'], index=ctys)
print(df) #print(df.values)

# distance matrix (scipy)
dist_array = distance_matrix(df.values, df.values)  
formated_dist_array = from_square_ndarray_to_matrix_for_distanceMatrix(dist_array) #my format

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance_matrix.html
dist_df = pd.DataFrame(distance_matrix(df.values, df.values), index=df.index, columns=df.index)
print(dist_df)

# distance matrix (Bio::Phylo), read it 
cities_distMatrix = DistanceMatrix(ctys, matrix=formated_dist_array)
print(cities_distMatrix) 


# Creating a DistanceTreeConstructor object
constructor = DistanceTreeConstructor()
########
#  UPGMA
########
# Construct the phlyogenetic tree using UPGMA algorithm
UPGMATree = constructor.upgma(cities_distMatrix)

# Printing the phlyogenetic tree using terminal
print("UPGMATree:")
Phylo.draw_ascii(UPGMATree)
# Draw the phlyogenetic tree
Phylo.draw(UPGMATree)


#####
#  NJ
#####
if 0:
    # Construct the phlyogenetic tree using NJ algorithm
    NJTree = constructor.nj(cities_distMatrix)
    
    # Printing the phlyogenetic tree using terminal
    print("NJTree:")
    Phylo.draw_ascii(NJTree)
    # Draw the phlyogenetic tree
    Phylo.draw(NJTree)

