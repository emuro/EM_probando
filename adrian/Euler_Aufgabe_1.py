# python3
# ################################################################## #
# euler1.py (C) Nov-2019 Mainz.
# Author: Enrique M. Muro
# ################################################################## #
#
# ------------------------------------------------------------------------
# Project Euler
#
# Purpose:
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all
# the multiples of 3 or 5 below 1000.
# Losung: 68878
# https://projecteuler.net/problem=1
# ------------------------------------------------------------------------
# Functions:
# if
# else
# ------------------------------------------------------------------------
# Examples of use:
#   Euler_Aufgaben_1.py

Summe = 0
a = float(input("Teilbar durch? "))
b = float(input("Teilbar durch? "))
print ("Zwischen welchen Zahlen möchtest du dividieren?")
x = float(input("Kleinste Zahl: "))
y = float(input("Größste Zahl: "))
if x >= y:
    print (x, " darf nicht größer oder gleich ", y, " sein")
else:
    while x < y:
        if x % a == 0 and x % b == 0:
            print (x, " ist teilbar durch ", a, " und ", b, ".")
            Summe = Summe + x
            x = x + 1
        else:
            if x % a == 0 or x % b == 0:
                if x % a == 0:
                    print (x, " ist nur teilbar durch ", a, ".")
                    Summe = Summe + x
                else:
                    print(x, " ist nur teilbar durch ", b, ".")
                    Summe = Summe + x
            else:
                print (x, " ist nicht teilbar durch ", a, " oder ", b, ".")
        x = x + 1
print ("Summe aller teilbaren Zahlen: ", Summe)