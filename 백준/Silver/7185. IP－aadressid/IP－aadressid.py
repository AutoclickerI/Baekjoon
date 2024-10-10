import re
s=set()
m=[]
for i in[*open(0)][1:]:
    i=i[:-1]
    if i in s:
        continue
    for j in s:
        if re.search(i,j):
            m+=i,
            break
    s.add(i)
print(len(m))
for i in m:
    print(i)