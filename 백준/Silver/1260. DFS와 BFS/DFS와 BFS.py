p,q,r=map(int,input().split())
l=[[]for _ in range(p+1)]
visited={}
for _ in[0]*q:
    a,b=map(int,input().split())
    l[a]+=[b]
    l[b]+=[a]
    visited[a]=visited.get(a,0)
    visited[b]=visited.get(b,0)
l=[sorted(i)for i in l]
def DFS(pos):
    visited[pos]=1
    print(pos,end=' ')
    if all(visited.values()):
        return
    for i in l[pos]:
        if not visited[i]:
            DFS(i)
DFS(r)
from collections import deque
print()
print(r,end=' ')
visited[r]=0
BFS=deque(l[r])
while any(visited.values()):
    i=BFS.popleft()
    if visited[i]==0:continue
    visited[i]=0
    print(i,end=' ')
    for j in l[i]:
        if visited[j]:
            BFS.append(j)