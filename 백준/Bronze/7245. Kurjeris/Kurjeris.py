[N,_],*l=[map(int,i.split())for i in open(0)]
T=[0]*N
m=T[:]
for t,v,*z in l:
    I=[i for i in range(N)if T[i]<=t]
    if I:i=min(I,key=lambda i:z[i]);T[i]=t+z[i];m[i]+=v
print(*m)