[N,M],p,*t=[[*map(int,i.split())]for i in open(0)]

P=sum(p)
SRC=N
DST=N+1

edges=[[]for _ in range(N+2)]
rank=[0]*(N+2)
to_dst=[-1]*(N+2)
last=[-1]*M

def add_edge(s,e,f,c):
    edges[s].append([e,f,len(edges[e]),c])
    edges[e].append([s,0,len(edges[s])-1,-c])

for i in range(N):
    if p[i]:
        add_edge(SRC,i,p[i],0)

def add_slot(j,k):
    s=len(edges)
    edges.append([])
    rank.append(k)
    to_dst.append(-1)

    for i in range(N):
        add_edge(i,s,1,k*t[i][j])

    add_edge(s,DST,1,0)
    to_dst[s]=len(edges[s])-1
    last[j]=s

for j in range(M):
    add_slot(j,1)

def min_cost_flow(src,dst,flow):
    cost_sum=0

    while flow:
        V=len(edges)
        dist=[float('inf')]*V
        inq=[0]*V
        prev=[(-1,-1)]*V

        dist[src]=0
        q=[src]
        inq[src]=1

        for n in q:
            inq[n]=0
            dn=dist[n]

            for i,(e,f,p,c)in enumerate(edges[n]):
                nd=dn+c
                if f and nd<dist[e]:
                    dist[e]=nd
                    prev[e]=n,i
                    if inq[e]<1:
                        inq[e]=1
                        q+=e,

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

        for j in range(M):
            s=last[j]
            if rank[s]<P and edges[s][to_dst[s]][1]<1:
                add_slot(j,rank[s]+1)

    return cost_sum

print(min_cost_flow(SRC,DST,P))