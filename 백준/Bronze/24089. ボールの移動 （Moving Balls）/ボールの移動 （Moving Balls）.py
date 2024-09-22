N,*x=open(0)
*l,=range(int(N.split()[0])+1)
for i in x:a,b=i.split();l[int(a)]=b
print(*l[1:])