import sys

if sys.argv != 2:
    print("python3", sys.argv[0], "fileName")

f_h = open(sys.argv[1])
lines   = f_h.read().split("\n")
header  = lines[0]
columns = header.split()

output = ""
for i, col in enumerate(columns):
    if i != 0:
        output += " " 
    output += "[" + str(i+1) + ":" + str(col) + "]"
print("\nHeader by columns:\n", output, sep="")
