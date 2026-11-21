import sys
input=sys.stdin.readline

N,M,K=map(int,input().split())
d={}
for i in[0]*int(input()):
    n,s=input().split()
    d[s]=d.get(s,[])
    d[s]+=int(n),

edge=[[]for _ in[0]*-~N]
for _ in[0]*M:
    s,e=map(int,input().split())
    edge[s]+=e,
    edge[e]+=s,

from collections import deque

def bfs(starter):
    visited=[0]*-~N
    cost=[0]*-~N
    i=0
    dq=deque()
    for v in starter:
        i+=1
        visited[v]=i
        dq+=(v,i,0),
    while dq:
        v,i,k=dq.popleft()
        if K<=k*2:
            return 0
        for ne in edge[v]:
            if visited[ne]!=0:
                if visited[ne]!=i and cost[ne]+k+1<=K:
                    return 1
            else:
                visited[ne]=i
                cost[ne]=k+1
                dq+=(ne,i,k+1),
    return 0

for i in d.values():
    if len(i)>1 and bfs(i):
        print('POWERFUL CODING JungHwan')
        break
else:
    print('so sad')