from heapq import*

[N],*l=[[*map(int,i.split())]for i in open(0)]

src=2*N
dst=2*N+1

edges=[[]for _ in[0]*(2*N+2)]

def add_edge(s,e,f,c):
    edges[s].append([e,f,len(edges[e]),c])
    edges[e].append([s,0,len(edges[s])-1,-c])

for i in range(N):
    add_edge(src,i,1,0)

for i in range(N):
    x1,y1=l[i]
    for j in range(N):
        x2,y2=l[j]
        add_edge(i,N+j,1,((x1+x2)**2+(y1-y2)**2)**.5)

for i in range(N):
    add_edge(N+i,dst,1,0)

def min_cost_flow(src,dst,flow):
    V=2*N+2
    h=[0]*V
    cost_sum=0
    eps=1e-12

    while flow:
        dist=[float('inf')]*V
        prev=[(-1,-1)]*V

        dist[src]=0
        q=[(0,src)]

        while q:
            d,n=heappop(q)
            if d>dist[n]+eps:
                continue
            for i,(e,f,p,c)in enumerate(edges[n]):
                if f<1:
                    continue
                nd=d+c+h[n]-h[e]
                if nd+eps<dist[e]:
                    dist[e]=nd
                    prev[e]=n,i
                    heappush(q,(nd,e))

        if dist[dst]==float('inf'):
            break

        for i in range(V):
            if dist[i]<float('inf'):
                h[i]+=dist[i]

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
        cost_sum+=fl*h[dst]

    return cost_sum

print(f"{min_cost_flow(src,dst,N)/2+1e-9:.3f}")