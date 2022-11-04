import random

#a list to store the generated random numbers
number_set = []
#Generate 100,000 random numbers
for x in range(100000):
   #pick numbers between 1 and 10,000
   number_set.append(random.randint(1,10001))

print(len(number_set))





##A list to store the leading digits
first_digit_set = []
#a method to get the leading digit
def get_leading_digit(number):
    #convert the number to a string
    #take the first character
    #convert back to an integer and return the value
    return int(str(number)[:1])
for d in number_set:
    first_digit_set.append(get_leading_digit(d))

for i in list(range(1, 10)):
    print("There are " + str(first_digit_set.count(i)) + " leading " + str(i) + "'s")

    
