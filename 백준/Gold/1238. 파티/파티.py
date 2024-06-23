N,M,X=map(int,input().split())
*f,=eval('[],'*-~N)
*b,=eval('[],'*-~N)
for _ in[0]*M:
    s,e,t=map(int,input().split())
    f[s]+=(e,t),
    b[e]+=(s,t),
from heapq import *
hq=[[0,X]]
v=[0]*-~N
cli=[1e9]*-~N
cli[0]=cli[X]=0
x=N
while x:
    p,e=heappop(hq)
    if cli[e]<p:
        continue
    v[e]=1
    x-=1
    for n,c in f[e]:
        if p+c<cli[n]:
            cli[n]=p+c
            heappush(hq,[p+c,n])

hq=[[0,X]]
v=[0]*-~N
cli2=[1e9]*-~N
cli2[0]=cli2[X]=0
x=N
while x:
    p,e=heappop(hq)
    if cli2[e]<p:
        continue
    v[e]=1
    x-=1
    for n,c in b[e]:
        if p+c<cli2[n]:
            cli2[n]=p+c
            heappush(hq,[p+c,n])
print(max(map(sum,zip(cli,cli2))))