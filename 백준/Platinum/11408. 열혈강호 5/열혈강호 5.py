[N,M],*l=[[*map(int,i.split())]for i in open(0)]

edges=[[]for _ in[0]*(N+M+2)]

def add_edge(s,e,f,c):
    edges[s].append([e,f,c,len(edges[e])])
    edges[e].append([s,0,-c,len(edges[s])-1])

for i,[_,*v]in enumerate(l,1):
    add_edge(0,i,1,0)
    for j,c in zip(*[iter(v)]*2):
        add_edge(i,j+N,1,c)

for i in range(M):
    add_edge(i+N+1,N+M+1,1,0)

def min_cost_max_flow(src,dst):
    flow=cost=0
    while 1:
        dist=[float('inf')]*(N+M+2)
        inq=[0]*(N+M+2)
        dist[src]=0
        l=[src]
        inq[src]=1

        for n in l:
            inq[n]=0
            for e,f,c,_ in edges[n]:
                if f and dist[n]+c<dist[e]:
                    dist[e]=dist[n]+c
                    if not inq[e]:
                        inq[e]=1
                        l+=e,

        if dist[dst]==float('inf'):
            return flow,cost

        def dfs(n,push):
            if n==dst:
                return push
            vis[n]=1
            for i,(e,f,c,p)in enumerate(edges[n]):
                if f and not vis[e] and dist[e]==dist[n]+c:
                    fl=dfs(e,min(push,f))
                    if fl:
                        edges[n][i][1]-=fl
                        edges[e][p][1]+=fl
                        return fl
            return 0

        while 1:
            vis=[0]*(N+M+2)
            fl=dfs(src,1)
            if not fl:
                break
            flow+=fl
            cost+=fl*dist[dst]

print(*min_cost_max_flow(0,N+M+1))