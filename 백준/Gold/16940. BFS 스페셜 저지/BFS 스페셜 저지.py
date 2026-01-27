[N],*l,v=[map(int,i.split())for i in open(0)]
d=[[]for _ in[0]*-~N]
z={1}
for s,e in l:
    d[s]+=e,
    d[e]+=s,
for i in range(N+1):
    d[i]={*d[i]}
f=1
from collections import*
dq=deque([{1}])
used={1}
for i in v:
    used|={i}
    while dq and i not in z:
        if z-used:
            f=0
        z=dq.popleft()
    if i in z:
        dq+=d[i],
    else:
        f=0
print(f)