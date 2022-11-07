import random

from random import choices
from collections import Counter

import math, sys

import matplotlib.pyplot as plt


#a method to get the leading digit
def get_first_int_digit(number):
    #convert the number to a string
    #take the first character
    #convert back to an integer and return the value
    return int(str(number)[:1])

#a method to get the last digit
def get_last_int_digit(number):
    #convert the number to a string
    #take the last character
    #convert back to an integer and return the value
    return int(str(number)[-1:])


# Get integers [1, N] using a uniform distribution
first_d = [1, 2, 3, 4, 5, 6, 7, 8, 9] # EM list(range(1,10))
num = 5000
N   = 10**6


# Uniform random distribution
#############################
number_set = []
for x in range(num): #Generate 100,000 random numbers between 1 and 10,000
   number_set.append(random.randint(1, N+1))
if 0:
   print(len(number_set))

#A list to store the leading digits
first_digit_set = []
last_digit_set = []
for rand_int in number_set:
    first_digit_set.append(get_first_int_digit(rand_int))
    last_digit_set.append(get_last_int_digit(rand_int))
if 0:
    print(number_set)
    print(first_digit_set)
    print(last_digit_set)
    sys.exit()

#first digit set distribution
first_digit_set_dist = []
last_digit_set_dist = []
for i in first_d:
   first_digit_set_dist.append(first_digit_set.count(i)/num)
   # 0 can be the last digit when analyzing the last digit
   last_digit_set_dist.append(last_digit_set.count(i)/(num - last_digit_set.count(0))) 

for i in first_d:
    print("There are " + str(first_digit_set_dist[i-1]) + " leading " + str(i) + "'s", end='')
    print(" (%2.3f" % (first_digit_set_dist[i-1]) + "%)")
for i in first_d:
    print("There are " + str(last_digit_set_dist[i-1]) + " last " + str(i) + "'s", end='')
    print(" (%2.3f" % (last_digit_set_dist[i-1]) + "%)")


# Benford 1st digit distribution
################################
#Specify the Benford Law weights)
weights = [0.301, 0.176, 0.124, 0.096, 0.079, 0.066, 0.057, 0.054, 0.047]
#generate sample first_digit set with Benford disctibution
#k = 10**6 generates 1 million values 
first_digits = choices(first_d, weights, k=num)
#use the standard library's counter module to get the counts in order
values_in_order = Counter(first_digits).most_common()
[print(i) for i in values_in_order]


# EM get the benford distribution
benford_dist = []
for d in first_d:
   benford_dist.append(math.log10(1+1/int(d)))
print("Benford 1st digit distribution:") 
for i, val in enumerate(benford_dist):
   print("\t(%d, %2.4f" % (i, val) + "%)")


# Plot
######
#Get the values for each digit
weighted_prob = []
for c in values_in_order:
    weighted_prob.append(c[1]/num)
    
#sets spaces to put digit count into
x_pos = first_d
#Plot: set size of the whole chart
plt.figure(figsize=(6, 6))
plt.xticks(x_pos, first_d) # x: define pos and label
plt.xlabel('Digit')
plt.ylabel('First Digit Density Prob')
plt.title('Benford\'s Law Distribution')

# Create bars and choose color
#plt.bar(first_d, weighted_prob, label="weighted prob") # plt.bar(y_pos, count, color = 'pink')
plt.bar(first_d, benford_dist, label="benford dist")
#plt.plot(first_d, benford_dist, 'ro', label="benford dist")
plt.plot(first_d, first_digit_set_dist, 'go', label="1st digit prob")
plt.plot(first_d, last_digit_set_dist, 'mo', markersize=2.5, label="last digit prob") 

#plt.ylim(0, int(max(count)*1.1)) # Limits for the Y axis
plt.legend()
plt.show()


