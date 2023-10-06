import sys

import random



my_input_len = int(input("length of the first string: "))

random.seed( random.randint(0, 1000000) )
o = range(my_input_len)

my_input = [random.randint(0, 1) for e in o]

l  = ''.join(' X'[x] for x in my_input)


#sys.exit()

for r in o:
    print(l);
    l = ''.join('X '[l[c-1:c+2] in ('XXX','   ','X  ','','')] for c in o)
