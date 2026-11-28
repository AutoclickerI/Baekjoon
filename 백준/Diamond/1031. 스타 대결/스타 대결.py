[N,M],A,B=[[*map(int,i.split())]for i in open(0)]
edges=[[]for _ in[0]*(N+M+2)]

def add_edge(s,e,f):
    edges[s].append([e,f,len(edges[e])])
    edges[e].append([s,0,len(edges[s])-1])

for i in range(N):
    for j in range(M):
        add_edge(i,N+j,1)

for i in range(N):
    add_edge(N+M,i,A[i])

for j in range(M):
    add_edge(N+j,N+M+1,B[j])

def max_flow(src,dst):
    flow=0
    while 1:
        level=[-1]*(N+M+2)
        level[src]=0
        l=[src]
        for n in l:
            for e,f,_ in edges[n]:
                if level[e]==-1 and f:
                    level[e]=level[n]+1
                    l+=e,
        if level[dst]==-1:
            return flow

        def dfs(n,push):
            if n==dst:
                return push
            for i,(e,f,p)in enumerate(edges[n]):
                if f and level[e]==level[n]+1:
                    fl=dfs(e,min(push,f))
                    if fl:
                        edges[n][i][1]-=fl
                        edges[e][p][1]+=fl
                        return fl
            return 0

        while fl:=dfs(src,float('inf')):
            flow+=fl

if sum(A)!=sum(B) or max_flow(N+M,N+M+1)<sum(A):
    exit(print(-1))

def dfs(n):
    if n==dst:
        return 1
    vis[n]=1
    for i,(e,f,p)in enumerate(edges[n]):
        if f and not vis[e] and dfs(e):
            edges[n][i][1]-=1
            edges[e][p][1]+=1
            return 1
    return 0

for i in range(N):
    s=''
    for j in range(M):
        dst,f,p=edges[i][j]
        edges[i][j][1]=edges[dst][p][1]=0
        if not f:
            vis=[0]*(N+M+2)
            f=dfs(i)
        s+='01'[f<1]
    print(s)