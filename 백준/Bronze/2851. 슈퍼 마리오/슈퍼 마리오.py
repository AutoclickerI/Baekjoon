a=0
*l,=map(int,open(0))
for i in range(11):a=[k:=sum(l[:i]),a][abs(a-100)<abs(k-100)]
print(a)