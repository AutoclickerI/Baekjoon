[N,M],*l=[map(int,i.split())for i in open(0)]
v=[0]*999
for t,p in l:
 i=999
 while t<i:i-=1;v[i]=max(v[i-t]+p,v[i])
print(v[N])