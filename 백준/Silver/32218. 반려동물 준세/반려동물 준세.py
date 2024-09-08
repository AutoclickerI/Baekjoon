*l,=map(int,[*open(0)][1].split())
c=1
while any(l):l=[sum(j>l[i]for j in l[i:])for i in range(len(l))];c+=1
print(c)