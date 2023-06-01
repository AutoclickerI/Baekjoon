from collections import deque
N,K=map(int,input().split())
l=deque([N])
v=[0]*999999
while 1:
    t=l.popleft()
    if t==K:break
    for i in t-1,t+1,2*t:
        if -1<i<999999 and not v[i]:
            v[i]=v[t]+1
            l.append(i)
print(v[K])