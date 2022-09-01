import sys

print(sys.argv)

if len(sys.argv) != 3:
    print("\nExample of use:")
    print("python3", sys.argv[0], "fileName", "numOfExamples")
    print("python3", sys.argv[0], "em.tsv", str(1))
    sys.exit()

f_h = open(sys.argv[1])
lines   = f_h.read().split("\n")
header  = lines[0]
columns = header.split("\t")

output = ""
header_cols = []
for i, col in enumerate(columns):
    if i != 0:
        output += " " 
    output += "[" + str(i+1) + ":" + str(col) + "]"
    header_cols.append(str(col))
print("\nHeader by columns:\n", output, sep="")


# An example: The first line
if int(sys.argv[2]):
    for l in range(1, int(sys.argv[2])+1):
        header  = lines[l]
        columns = header.split("\t")
        print("\nThe line", str(l), "by columns:\n")
        for i, col in enumerate(columns):
            print("[" + str(i+1) + "|" + header_cols[i] + "|" + str(col) + "]",
                  sep="")



