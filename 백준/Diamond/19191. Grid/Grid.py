N,M=map(int,input().split())
a=[input().strip()for _ in[0]*N]

E=2*N*M-N-M
B=2*N+2*M
K=N*M
OPT=K+E+B
SRC=OPT
DST=OPT+1
V=DST+1

edges=[[]for _ in[0]*V]

def add_edge(s,e,f,c):
    edges[s].append([e,f,len(edges[e]),c])
    edges[e].append([s,0,len(edges[s])-1,-c])

h=[[-1]*max(M-1,0)for _ in[0]*N]
v=[[-1]*M for _ in[0]*max(N-1,0)]

o=K
for i in range(N):
    for j in range(M-1):
        h[i][j]=o
        add_edge(o,DST,1,0)
        o+=1

for i in range(N-1):
    for j in range(M):
        v[i][j]=o
        add_edge(o,DST,1,0)
        o+=1

d='^>v<'
p={c:i for i,c in enumerate(d)}
def cost(x,y):
    t=abs(p[x]-p[y])
    return min(t,4-t)

for i in range(N):
    for j in range(M):
        n=i*M+j
        add_edge(SRC,n,1,0)

        if i:
            e=v[i-1][j]
        else:
            e=o
            add_edge(o,DST,1,0)
            o+=1
        add_edge(n,e,1,cost(a[i][j],'^'))

        if j<M-1:
            e=h[i][j]
        else:
            e=o
            add_edge(o,DST,1,0)
            o+=1
        add_edge(n,e,1,cost(a[i][j],'>'))

        if i<N-1:
            e=v[i][j]
        else:
            e=o
            add_edge(o,DST,1,0)
            o+=1
        add_edge(n,e,1,cost(a[i][j],'v'))

        if j:
            e=h[i][j-1]
        else:
            e=o
            add_edge(o,DST,1,0)
            o+=1
        add_edge(n,e,1,cost(a[i][j],'<'))

def min_cost_flow(src,dst,flow):
    cost_sum=0

    while flow:
        dist=[float('inf')]*V
        inq=[0]*V
        prev=[(-1,-1)]*V

        dist[src]=0
        l=[src]
        inq[src]=1

        for n in l:
            inq[n]=0
            for i,(e,f,p,c)in enumerate(edges[n]):
                nd=dist[n]+c
                if f and nd<dist[e]:
                    dist[e]=nd
                    prev[e]=n,i
                    if inq[e]<1:
                        inq[e]=1
                        l+=e,

        fl=flow
        n=dst
        while n!=src:
            pn,pi=prev[n]
            fl=min(fl,edges[pn][pi][1])
            n=pn

        n=dst
        while n!=src:
            pn,pi=prev[n]
            e,f,p,cost=edges[pn][pi]
            edges[pn][pi][1]-=fl
            edges[e][p][1]+=fl
            n=pn

        flow-=fl
        cost_sum+=fl*dist[dst]
    return cost_sum

print(min_cost_flow(SRC,DST,N*M))