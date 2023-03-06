import sys
import re

print(sys.argv)

if len(sys.argv) != 3:
    print("\nShow columns. Examples of use:")
    print("# Up to the line:")
    print("python3", sys.argv[0], "fileName", "upToTheLine")
    print("python3", sys.argv[0], "em.tsv", "2")
    print("# Only one line:")
    print("python3", sys.argv[0], "fileName", "[numOfLine]")
    print("python3", sys.argv[0], "em.tsv", "[2]")
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


bool_show_only_one_line = False
selected_line = -1
m = re.search(r"\[(\d+)\]", sys.argv[2])
if m:
    bool_show_only_one_line = True 
    selected_line = int(m.group(1))
    up_to_line = selected_line
else:
    up_to_line = int(sys.argv[2])
    
# 
if up_to_line:
    for l in range(1, up_to_line+1): # Desde linea 1 a linea==sys.argv[2]
        if bool_show_only_one_line and (l < selected_line):
            continue
        header  = lines[l]
        columns = header.split("\t")
        print("\nThe line", str(l), "by columns:\n")
        for i, col in enumerate(columns):
            print("[" + str(i+1) + "|" + header_cols[i] + "|" + str(col) + "]",
                  sep="")



