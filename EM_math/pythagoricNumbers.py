from math import sqrt

print("Given a max. val of the hypotenuse, the program finds all the possible pytagorian relations")

#get max_h
while True:
    max_h=int(input("Introduce the max val of the hypotenuse:"))
    if max_h<=0:
        print("El valor suministrado ha de ser un entero positivo")
    else:
        break

results=[]
explanation=[]
for a in range(1,max_h+1):
    for b in range(a, max_h+1):
        h2= a**2+b**2
        h=int(sqrt(h2))
        if h2==h**2:
            results.append((a,b,h))
            explanation.append((a**2,b**2,h**2))

i=len(results)
j=0
while i>0:
    print(results[j])
    print("\t", explanation[j])
    i-=1
    j+=1
print("Hay", len(results), "diferentes combinaciones pitagóricas")
