[N],A,H,L=[[*map(int,i.split())]for i in open(0)]

o=sorted(range(N),key=lambda i:A[i])
A=[A[i]for i in o]
H=[H[i]for i in o]
L=[L[i]for i in o]

edges=[[]for _ in[0]*(3*N+2)]

def add_edge(s,e,f,c):
    edges[s].append([e,f,len(edges[e]),c])
    edges[e].append([s,0,len(edges[s])-1,-c])

for i in range(N):
    add_edge(0,i+1,L[i]-(i<N-1),0)

for i in range(N):
    for j in range(i):
        add_edge(i+1,N+j+1,1,H[i]+H[j]-(A[i]^A[j]))

for i in range(N-1):
    add_edge(N+i+1,3*N+1,1,0)

def min_cost_flow(src,dst,flow):
    cost_sum=0

    while flow:
        dist=[float('inf')]*-~dst
        inq=[0]*-~dst
        prev=[(-1,-1)]*-~dst

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

print(-min_cost_flow(0,3*N+1,N-1))