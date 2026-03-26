[N,M,K],*l=[map(int,i.split())for i in open(0)]
edges=[[]for _ in[0]*(N+M+3)]

def add_edge(s,e,f):
    edges[s].append([e,f,len(edges[e])])
    edges[e].append([s,0,len(edges[s])-1])

add_edge(N+M,N+M+1,K)

for i in range(N):
    add_edge(N+M,i,1)
    add_edge(N+M+1,i,K)

for i in range(M):
    add_edge(N+i,N+M+2,1)

for i,(_,*v) in enumerate(l):
    for j in v:
        add_edge(i,j+N-1,float('inf'))

def max_flow(src,dst):
    flow=0
    while 1:
        level=[-1]*(N+M+3)
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

print(max_flow(N+M,N+M+2))