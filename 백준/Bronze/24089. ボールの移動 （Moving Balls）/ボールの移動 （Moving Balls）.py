N,*x=open(0)
_,*l=range(int(N.split()[0])+1)
for i in x:a,b=i.split();l[int(a)-1]=b
print(*l)