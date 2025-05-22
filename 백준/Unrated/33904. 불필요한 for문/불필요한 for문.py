d={}
l=[i.strip()for i in open(0)]
for i in range(len(l)-1):
    d[l[i][9]]=i
for i in*d,:
    if i not in l[-1]:
        del d[i]
c=0
for i in sorted(d,key=lambda i:d[i]):
    print(c*' '+l[d[i]])
    c+=1
print(c*' '+l[-1])