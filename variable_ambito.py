def f1():
    a=2*2
    print(b)
    #b="caracpöa"
    return a


def main():

    print("hola")
    if 1:
        global b  # la hago global
    else:
        pass
    b="feo"
    c=f1()
    print(c)

if 0:
    if __name__=="__main__":
        main()  # no puede hacer el print(b) en f1, el ámbito de b es local a main, no global
else:
    print("hola")
    #global b
    b="feo"  # esta variable la utiliza f1 si el ambito es global
    b=f1()
    print(b)  # no puede, da error porque a pertenece al ámbito de f1