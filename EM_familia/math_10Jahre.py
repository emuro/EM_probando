import random

print("Hola Emma. Soy tu programa de matemáticas.")
s1 = random.randrange(1000)
s2 = random.randrange(1000)
s3 = random.randrange(1000)

print("El primer sumando es (s1):", s1)
print("Otro sumando es (s2):", s2)
print("El otro sumando es (s3):", s3)
print(s1, "+" , s2, "+" , s3, "= ", end='')
emma = int(input())
if emma == s1+s2+s3:
    print("Correcto!")
else:
    print("Eres muy mala en matemáticas...vete a estudiar un rato!")

