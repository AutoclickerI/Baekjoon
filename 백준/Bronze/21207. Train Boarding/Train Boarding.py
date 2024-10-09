N,L,_,*s=map(int,open(0).read().split())
l=[m:=0]*N
for i in s:
    r,q=divmod(i,L)
    if r<N:l[r]+=1;m=max(m,abs(q-L//2))
    else:l[N-1]+=1;m=max(m,q+L//2+(r-N)*L)
print(m,max(l))