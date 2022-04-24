from random import randint
print ("Wilkommen zu meinen Programm Manuel und Emma hier lernt ihr Rechnungen durchzufuehren")
maxl = float(input("Hoechste Zahl? "))
max = maxl / 2
x = 0
ersteer = float(input("Anzahl der Aufgaben? "))
y = ersteer - 1
while x <= y:
    x = x + 1
    zufallszahl = randint(0, max)
    zufallszahl2 = randint(0, max)
    print (zufallszahl, " + ", zufallszahl2)
    r = float(input("Loesung "))
    if r == zufallszahl + zufallszahl2:
        print ("Gut gemacht du hast jetzt ", x, " Punkte.")
    else:
        x = x - 1
        print ("Leider Falsch gemacht du hast Momentan ", x, " Punkte.")
tipp = input("Kopf (K) oder Zahl (Z): ")
zufallszahl3 = randint(0, 1)
if zufallszahl3 == 0:
    print("Kopf ist gefallen.")
    Seite = "K"
    seite = "k"
else:
    print("Zahl ist gefallen.")
    Seite = "Z"
    seite = "z"
if (tipp == Seite or tipp == seite):
    print ("Du hast gewonnen!")
else:
    print ("Du hast verloren ):")