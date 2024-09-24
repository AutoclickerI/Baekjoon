from collections import deque
N,K=map(int,input().split())
l=deque([N])
v=[0]*999999
p=[0]*999999
p[N]=1
while 1:
    t=l.popleft()
    if t==K:break
    for i in t-1,t+1,2*t:
        if -1<i<999999:
            if not v[i]:
                v[i]=v[t]+1
                p[i]=p[t]
                l.append(i)
            elif v[t]+1==v[i]:
                p[i]+=p[t]
print(v[K])
print(p[K])