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


def get_twin_primes(primes):
    """" calcula todos los primos gemelos de la lista.
         Primos gemelos son los primos consecutivos de la lista, tal que 
         p_i+1 - p_i = 2
    """
    twin_primes = []
    for i in range(0, len(primes)-2):
        if primes[i+1] - primes[i] == 2:
            twin_primes.append([primes[i], primes[i+1]])
    return twin_primes


def get_digit_product(num):
    """ Calcula:
            - Producto de los 2 primos gemelos.
            - Sumas los digitos del producto
               - Si sale d <= 9, se acabó
               - Si sale d > 9, se vuelven a sumar los dígitos, hasta que 
                 quede un dígito, ese es el resultado.
    """

    p1 = str(num)
    sum = 0
    for d in p1:
        sum += int(d)
    if sum > 9:
        d = get_digit_product(sum)
        return d
    else:
        #print(num, sum)
        return sum


def get_digit_product_of_all_twin_primes(twin_primes):
    """ Calcula:
            - Producto de los 2 primos gemelos.
            - Sumas los digitos del producto
               - Si sale d <= 9, se acabó
               - Si sale d > 9, se vuelven a sumar los dígitos, hasta que 
                 quede un dígito, ese es el resultado.
    """

    digit_products = []
    for i, val in enumerate(twin_primes):
        p1 = val[1] * val[0]
        twin_primes[i].append(p1)
        d = get_digit_product(p1)
        #print(val, p1, d)
        twin_primes[i].append(d)
    return



primes = prime_numbers_up_to_max(10**7)
twin_primes = get_twin_primes(primes)
get_digit_product_of_all_twin_primes(twin_primes)
#print(twin_primes)
for l in twin_primes:
    if l[-1] != 8: 
        print(l[0], l[1], ":", l[-1]) 
print("In the first", len(twin_primes), "twin-primes")

# Conclusion: El digit product es siempre 8 excepto en (3, 5)
