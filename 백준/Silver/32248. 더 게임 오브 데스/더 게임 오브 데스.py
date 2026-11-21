N,T,*A=map(int,open(0).read().split())
c=t=0
v=[0]*N
while T:
 T-=1;v[c]=t;t+=1
 if v[c:=A[c]-1]:T%=t-v[c]
print(1+c)