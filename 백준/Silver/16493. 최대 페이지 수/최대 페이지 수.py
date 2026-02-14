[N,M],*l=[map(int,i.split())for i in open(0)]
v=[0]*999
for t,p in l:
 for i in range(998,t-1,-1):v[i]=max(v[i-t]+p,v[i])
print(v[N])