d={}
for i in input():
    d[i]=d.get(i,0)+1
for i in input():
    d[i]=d.get(i,0)-1
print(sum(map(abs,d.values())))