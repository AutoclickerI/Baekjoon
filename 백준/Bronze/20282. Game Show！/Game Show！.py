*l,=map(int,open(0))
L=[0,l[1]]
for i in l[2:]:L+=[L[-1]+i]
print(100+max(L))