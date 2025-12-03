[N,T],*l=[map(int,i.split())for i in open(0)]
v=[0]*-~T
for k,s in l:
 for i in range(T-k,-1,-1):v[i+k]=max(v[i+k],v[i]+s)
print(v[-1])