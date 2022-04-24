print ("*** Willkommen bei Fibonacci Zahlen ***")
print ("!!!!!!!!!!!!!!Vorsicht nur gerade Zahlen bei der Variabel b eingeben")
a = 0
b = float(input("Fibonacci Zahlen bis zur Zahl: "))
x = 1
y = 2
o = 0
while x < b or y < b:
    a = a + 1
    if x % 2 == 0:
        o = o + x
    if y % 2 == 0:
        o = o + y
    print (x)
    x = x + y
    print(y)
    y = y + x
print ("Die Summe aller gerader Zahlen ist: ", o)