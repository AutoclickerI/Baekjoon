import sys
input=sys.stdin.readline

from collections import deque

N=int(input())
edges=[[]for _ in[0]*-~N]
edges_back=[[]for _ in[0]*-~N]
deg=[0]*-~N

for i in range(1,N):
    input()
    for e in map(int,input().split()):
        edges[i]+=e,
        edges_back[e]+=i,
        deg[e]+=1

dq=deque([1])
visited=[0]*-~N
visited[1]=1

while dq:
    n=dq.popleft()
    for e in edges[n]:
        if visited[e]<1:
            visited[e]=1
            dq+=e,

dq=deque([N])
visited_back=[0]*-~N
visited_back[N]=1

while dq:
    n=dq.popleft()
    for e in edges_back[n]:
        if visited_back[e]<1:
            visited_back[e]=1
            dq+=e,

for i in range(1,N+1):
    if visited[i]<1:
        for e in edges[i]:
            deg[e]-=1
        edges[i]=[]

f2=0
dq=deque([1])

if deg[1]:
    f2=1

a=[]

while dq:
    n=dq.popleft()
    a+=n,
    
    for e in edges[n]:
        deg[e]-=1
        if deg[e]==0:
            dq+=e,

print(['PRISON','PARDON'][all(i==j for i,j in zip(visited,visited_back)if i)],'UN'*(f2 or len(a)<sum(visited))+'LIMITED')