[N],[s,e],_,*l=[map(int,i.split())for i in open(0)]

d=[[]for _ in[0]*-~N]
v=[0]*-~N
for p,q in l:d[p]+=q,;d[q]+=p,

from collections import deque
dq=deque([(s,0)])

while dq:
    s,c=dq.popleft()
    if s==e:break
    for n in d[s]:
        if v[n]<1:v[n]=1;dq+=(n,c+1),
print(-(s!=e)or c)