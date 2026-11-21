p,_,*l=map(int,open(0).read().split())
L=[0]*p
while l:p,q,r,*l=l;L[p-1:q]=[r]*(q-p+1)
print(*L)