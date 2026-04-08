import sys
sys.setrecursionlimit(2*10**5)

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

T=int(input())
for t in range(T):
    N,M=map(int,input().split())
    edges=[[]for _ in[0]*N]
    tm=[]
    for _ in[0]*M:
        s,e=map(int,input().split())
        edges[s]+=e,
        tm+=(s,e),
    
    idx=0

    node_id=[0]*N
    finished=[0]*N

    stack=[]
    res=[]
    for u in range(N):
        if finished[u]<1:
            scc(u)
    
    dm={}
    for i,arr in enumerate(res):
        for v in arr:dm[v]=i
    
    N=len(res)
    edges=[[]for _ in[0]*N]
    deg=[0]*N
    for s,e in tm:
        ss,ee=dm[s],dm[e]
        if ss-ee:
            edges[ss]+=ee,
            deg[ee]+=1
    if 1<deg.count(0):
        print('Confused')
    else:
        print(*sorted(res[-1]))
    
    if t==T-1:
        break
    input()
    print()