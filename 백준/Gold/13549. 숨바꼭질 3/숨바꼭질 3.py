from collections import deque
N,K=map(int,input().split())
l=deque([N])
v=[-1]*999999
p=[0]*999999
v[N]=0
p[N]=1
while 1:
    t=l.popleft()
    if t==K:break
    z=2*t
    while z<999999 and v[t]!=v[z]:
        v[z]=v[t]
        p[z]=p[t]
        l.appendleft(z)
        z*=2
    for i in t-1,t+1:
        if -1<i<999999:
            if v[i]<0:
                v[i]=v[t]+1
                p[i]=p[t]
                l.append(i)
            elif v[t]+1==v[i]:
                p[i]+=p[t]
print(v[K])