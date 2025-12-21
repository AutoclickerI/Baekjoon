[T],_,*l=[map(int,i.split())for i in open(0)]
v=[0]*-~T
v[0]=1
for p,n in l:
    t=v[:]
    for i in range(T+1):
        for j in range(i+p,min(i+p*n+1,T+1),p):
            t[j]+=v[i]
    v=t
print(v[T])