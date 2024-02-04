import random
from time import time


def addition(n, max):
    '''Das Program kann n Nummern [0, max] addieren
       :param n: int 
    '''
    s = [] # Random Nummern
    for i in range(n):
        s.append(random.randrange(max+1))
        ##print("He generado un sumando aleatorio:", s[i])
    # Frage des Computers
    for i in range(len(s)-1):
        print(s[i], '+ ', end='')
    print(s[-1], '= ', end='')
    # Antwort
    emma = int(input())
    # 
    if emma == sum(s):
        print("Correcto!")
        return 1
    else:
        print("Incorrecto...Era " + str(sum(s)) + "\n")
        return 0
       
def main():
    NUM_CORRECT = 10
    print("Hola Emma, Manuel. Soy tu programa de matemáticas.")
    print("Tienes que hacer ", NUM_CORRECT, " cuentas correctamente.")

    start_time = time()
    num_correct = 0
    num_tries = 0
    while True:
        num_tries += 1 
        num_correct += addition(2, 5000)
        if num_correct >= NUM_CORRECT:
            break
    print(num_correct, "correctas de", num_tries, "preguntas.")
    total_time = time() - start_time
    print("Has tardado %.2f segundos. Una media de %.0f segundos por pregunta." %
          (total_time, total_time/NUM_CORRECT))
        
if __name__ == "__main__":
    main()
