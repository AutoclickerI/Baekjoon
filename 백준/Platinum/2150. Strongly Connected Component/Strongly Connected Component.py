import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N,E=map(int,input().split())

edges=[[]for _ in[0]*N]

for _ in[0]*E:
    s,e=map(int,input().split())
    edges[s-1]+=e-1,

idx=0

node_id=[0]*N
finished=[0]*N

stack=[]
res=[]

def scc(u):
    global idx
    idx+=1
    low=node_id[u]=idx
    stack.append(u)

    for v in edges[u]:
        if node_id[v]<1:
            low=min(low,scc(v))
        elif finished[v]<1:
            low=min(low,node_id[v])
    
    if low==node_id[u]:
        c=[]
        v=None
        while u!=v:
            v=stack.pop()
            c+=v,
            finished[v]=1
        res.append(c)
        
    return low

for u in range(N):
    if finished[u]<1:
        scc(u)

for i in res:i.sort()

res.sort()

print(len(res))
for i in res:print(*[j+1 for j in i],-1)