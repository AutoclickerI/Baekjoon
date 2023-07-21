from collections import deque
import sys
input=sys.stdin.readline
N,M,X,Y=map(int,input().split())
A=[0,*map(int,input().split())]
l=[[]for _ in[0]*-~N]
for _ in[0]*M:
    p,q=map(int,input().split())
    l[p]+=q,
    l[q]+=p,
visited=[-1]*-~N
*start,=map(int,input().split())
for i in start:
    visited[i]=0
dq=deque((i,0)for i in start)
prev=-1
while dq:
    n,p=dq.popleft()
    for i in l[n]:
        if visited[i]==-1:
            visited[i]=p+1
            dq.append((i,p+1))
money=[i*j for i,j in zip(visited,A)]
for i in range(N):
    if visited[i+1]<0<A[i+1]:exit(print(-1))
print(sum(sorted(money)[-X:]))