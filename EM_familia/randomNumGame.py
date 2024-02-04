import random

MAX_NUM=20  # rand num: 0 to MAX_NUM

# get a  rand num to guess
rand_num=random.randint(0,MAX_NUM)

print("Emma o Manuel, di un número del 0 al ", MAX_NUM,
      ". Yo he pensado uno, a ver si lo aciertas!: ", sep='')

guess=-1
while (guess != rand_num):
    guess=int(input())
    if guess<rand_num:
        print("Te has confundido", str(guess), "es demasiado pequeño. Prueba otra vez: ")
    elif guess>rand_num:
        print("Te has confundido", str(guess), "es demasiado grande. Prueba otra vez: ")
    else:
        print("Guau!,", str(guess), " has acertado. Qué bueno eres!")
        print("Quieres jugar otra vez? (s/n): ")
        answer=str(input())
        if answer=="s":
            rand_num=int(random.randint(0,MAX_NUM))
            guess=-1
            print("Venga, Emma o Manuel, vuelve a decir un número del 0 al ", MAX_NUM,
                    ". Yo he pensado otro número diferente, a ver si lo aciertas!: ", sep='')

print("Hasta la vista!, a ver si luego jugamos otra vez!.")
