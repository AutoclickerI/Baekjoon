N,T,*A=map(int,open(0).read().split())
c=t=1
v=[0]*-~N
while T:
 T-=1
 if v[c]:T%=t-v[c];v=[0]*-~N
 v[c]=t;c=A[c-1];t+=1
print(c)