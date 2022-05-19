import random

cake_len = 15 # cm
cake = {"v1": 0., "v2": 0., "c":0.}

simulations = 1000000

success = 0
for i in range(1, simulations+1):
    cake["v1"] = random.uniform(0,1)
    cake["v2"] = random.uniform(0,1)
    cake["c"] = random.uniform(0,1)
    r = sorted(cake.keys(), key = lambda x: cake[x]) # print(r)
    
    if r[1] == "c":
        success +=1
    if i % 1000 == 0:
        print(i, success/i)
