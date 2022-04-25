import sys
from decimal import *
import re

# FUNCTIONS
###########
def prime_numbers_up_to_max(p_max):
    """" calcula todos los primos <= p_max
        utilizando el método de la criba de Erastótenes.
        Llega bien hasta  10e7...~6sec en spica.
    """
    p = [1] * (p_max+1)  # max prime number al que llego bien solo por mem. es 10e8...~3sec.
    p[0] = 0
    p[1] = 0

    for i in range(2, p_max+1):
        if p[i] == 1:
            if 2*i <= p_max+1:
                for j in list(range(2*i, p_max+1, i)):
                    if p[j] == 0:
                        continue
                    else:
                        p[j] = 0
                        continue
        elif p[i] == 0:
            continue

    primes = []
    for i in range(0, p_max+1):
        if p[i] == 1:
            primes.append(i)
    print("There are", len(primes), "prime numbers <=", p_max)
    return primes


primes = prime_numbers_up_to_max(150000)
for i, p in enumerate(primes[3:]):
    getcontext().prec = 2 * p  # change dinamically the precision!
    r = str(Decimal(1)/Decimal(p))
    #m = re.search(r"^0\.(\d+?)\1+", r)
    m = re.search(r"^0.(0*\d+?)\1+", r)
    pattern = m.group(1)

    if 1: # less info
        print(i, p, len(pattern))
    else:
        print(i, p, 2*p, len(pattern), pattern, r)
