from collections import deque

d={}
dq=deque()
m=c=0

for i in[*open(0)][1][::2]:
    d[i]=d.get(i,0)+1
    c+=1
    while len(d)>2:
        v=dq.popleft()
        d[v]-=1
        if d[v]<1:
            del d[v]
        c-=1
    m=max(m,c)
    dq+=i,
print(m)