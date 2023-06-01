a,*b=open(0)
N,M=map(int,a.split())
F=[0]*(N+1)
for i in b:p,q=map(int,i.split());F[p]+=1;F[q]+=1
print(*F[1:])