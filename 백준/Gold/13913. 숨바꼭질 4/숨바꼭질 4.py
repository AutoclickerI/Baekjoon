from collections import deque
N,K=map(int,input().split())
l=deque([N])
v=[-1]*999999
p=[-1]*999999
v[N]=0
while 1:
    t=l.popleft()
    if t==K:break
    for i in t-1,t+1,2*t:
        if -1<i<999999:
            if v[i]<0:
                v[i]=v[t]+1
                p[i]=t
                l.append(i)
print(v[K])
a=[]
while 0<=K:a+=K,;K=p[K]
print(*a[::-1])