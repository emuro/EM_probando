


def pyramid(symbol, num_lines):
    '''
    pyramid pattern: n lines made with symbol (i.e *)
    '''
    symbol_pos={}
    for l in range(0,num_lines): # line
        #print(l)
        pos=[]
        for s in range(num_lines-l,num_lines+l+1, 2): # pos of pattern in line
            #print("\t",s)
            pos.append(s)
        symbol_pos[l]=pos[:]
    #print(symbol_pos)

    #ascii plot of the pyramid
    for l in range(0,num_lines): # line
        for p in range(1,2*num_lines+1): # pos of pattern in line
            if p in symbol_pos[l]:
                print(symbol, end="")
            else:
                print(' ', end="")
        print("") # just for the \n


def inverted_pyramid(symbol, num_lines):
    '''
    inverted_pyramid pattern: n lines made with symbol (i.e *)
    '''
    symbol_pos={}
    for l in range(0,num_lines): # line
        #print(l)
        pos=[]
        for s in range(num_lines-l,num_lines+l+1, 2): # pos of pattern in line
            #print("\t",s)
            pos.append(s)
        symbol_pos[l]=pos[:]
    #print(symbol_pos)

    #ascii plot of the pyramid
    for l in range(0,num_lines): # line
        for p in range(1,2*num_lines+1): # pos of pattern in line
            if p in symbol_pos[abs(l-num_lines+1)]:
                print(symbol, end="")
            else:
                print(' ', end="")
        print("") # just for the \n


def right_pyramid(symbol, num_lines):
    for i in range(0, num_lines):
        for j in range(i, -1, -1):
            print("* ", end="")
        print("") # just for the \n

    for i in range(num_lines-1, 0, -1):
        for j in range(0, i):
            print("* ", end="")
        print("") # just for the \n


def left_pyramid(symbol, num_lines):
    '''
    left pyramid pattern: n lines made with symbol (i.e *)
    '''
    symbol_pos={}
    for x in range(0,2*num_lines-1): # line
        #print(l)
        pos=[]
        if(x<=num_lines-1):
            for y in range(num_lines-x-1,num_lines, 2): # col of pattern in line
                #print("\t",s)
                pos.append(y)
        else:
            #print(x, "**", num_lines-(x-num_lines+2), flush=True)
            pos=symbol_pos[num_lines-(x-num_lines+2)][:]
        symbol_pos[x]=pos[:]
    #print(symbol_pos)

    #ascii plot of the pyramid
    for x in range(0,2*num_lines-1): # line
        for y in range(num_lines):   # col of pattern in line
            if y in symbol_pos[x]:
                print(symbol, end="")
            else:
                print(' ', end="")
        print("") # just for the \n


# main code
###########

symbol=""

# pyramid
if True:
    num_lines=int(input("the number of lines of your pyramid pattern: "))
    pyramid(symbol, num_lines)

# inverted pyramid
if False:
    num_lines=int(input("the number of lines of your inverted pyramid pattern: "))
    inverted_pyramid(symbol, num_lines)

# rombo
if False:
    num_lines=int(input("the number of lines of your rombo pattern: "))
    pyramid(symbol, num_lines)
    inverted_pyramid(symbol, num_lines)

# right pyramid
if False:
    num_lines=int(input("the number of lines of your right pyramid pattern: "))
    right_pyramid(symbol, num_lines)

# left pyramid
if False:
    num_lines=int(input("the number of lines of your left pyramid pattern: "))
    left_pyramid(symbol, num_lines)