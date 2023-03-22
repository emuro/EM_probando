d = range(1, 7) # a dice


#additive
a = dict()
for i in d:
    for j in d:
        new = i + j
        if new in a.keys():
            a[new] = a[new] + 1
        else:
            a[new] = 1


k = sorted(a.keys())
for i in k:
    if i <10:
        print (str(i) + ": ", end="")
    else:
        print (str(i) + ":", end="")
    for j in range(0, a[i]):
        print("|", sep="|", end="")
    print()


#multiplicative
m = dict()
for i in d:
    for j in d:
        new = i * j
        if new in m.keys():
            m[new] = m[new] + 1
        else:
            m[new] = 1
sorted_m_by_val = sorted(m.items(), key=lambda x:x[1], reverse=True)
print(sorted_m_by_val)
ms_keys = []
for i in sorted_m_by_val:
    ms_keys.append(i[0])
    
for i in ms_keys:
    if i <10:
        print (str(i) + ": ", end="")
    else:
        print (str(i) + ":", end="")
    for j in range(0, m[i]):
        print("|", sep="|", end="")
    print()
