import sys
import re


bool_check = 0
if bool_check:    
    print(sys.argv)

if len(sys.argv) != 5:
    print("\nSubset of f1 using f2 as key. Examples of use:")
    print("# Up to the line:")
    print("python3", sys.argv[0], "MainFileName__f1", "col_f1", "KeyFileName__f2", "col_f2",
          "#The columns are the key to merge")
    print("python3", sys.argv[0], "all.tsv", "2", "key.txt", 0)
    sys.exit()

f1_name = sys.argv[1]
c1 = int(sys.argv[2])
f2_name = sys.argv[3]
c2 = int(sys.argv[4])



# Main file
f1_h = open(f1_name)
lines   = f1_h.read().split("\n")
if bool_check:
    print("\n##", f1_name, "has\n", len(lines), "entries")
lines   = [x for x in lines if x != '']
if bool_check:
    print("##", f1_name, "has\n", len(lines), "non empty entries")
header  = lines[0]
columns = header.split("\t")
f1_h.close()

# Key file
k_h = open(f2_name)
lines2   = k_h.read().split("\n")
if bool_check:
    print("##", f2_name, "has\n", len(lines2), "entries")
lines2   = [x for x in lines2 if x != '']
if bool_check:
    print("##", f2_name, "has\n",  len(lines2), "non empty entries")
header2  = lines2[0]
columns2 = header2.split("\t")
k_h.close()

# get keys
keys = [l.split()[c2] for l in lines2]
keys = set(keys)
#print(keys)

#output of filtered lines 
for l in lines:
    aux_l = l.split()
    if aux_l[c1] in keys:
        print(l)

