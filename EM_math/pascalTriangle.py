
def pascal_triangle(num_lines):
    for i in range(0,num_lines):
        for j in range(0,i+1):
            if j==0 or j==i:
                P[i][j]=1
            else:
                P[i][j]=P[i-1][j]+P[i-1][j-1]
    #print (P)



P=[] # Pascal matrix
if True:
    num_lines=int(input("the number of lines of your Pascal triangle: "))
    P=[[0 for x in range(num_lines)] for y in range(num_lines)]
    pascal_triangle(num_lines)

    for i in range(0,num_lines):
        for j in range(0,i+1):
            print (P[i][j], end=" ")
        print("")