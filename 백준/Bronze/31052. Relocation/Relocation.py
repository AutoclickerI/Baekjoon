_,i,*l=open(0)
*x,=map(int,i.split())
for j in l:
    n,a,b=map(int,j.split())
    if~-n:print(abs(x[a-1]-x[b-1]))
    else:x[a-1]=b