N,M,V=map(int,input().split())
edges=[[]for _ in range(N+1)]

for _ in range(M):
    s,e=map(int,input().split())
    edges[s].append(e)
    edges[e].append(s)

for i in edges:
    i.sort()

from collections import deque
def DFS(n):
    ret.append(n)
    visited[n]=1
    for e in edges[n]:
        if visited[e]<1:
            DFS(e)

def BFS(n):
    visited[n]=1
    dq=deque([n])
    while dq:
        n=dq.popleft()
        ret.append(n)
        for e in edges[n]:
            if visited[e]<1:
                visited[e]=1
                dq.append(e)

visited=[0]*(N+1)
ret=[]
DFS(V)
print(*ret)

visited=[0]*(N+1)
ret=[]
BFS(V)
print(*ret)