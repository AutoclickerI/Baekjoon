[N,M,T,L],*l=[[*map(int,i.split())]for i in open(0)]

src=0
pb=1
ub=pb+M
dst=ub+N

edges=[[]for _ in[0]*(dst+1)]

def add_edge(s,e,f,c):
    edges[s].append([e,f,len(edges[e]),c])
    edges[e].append([s,0,len(edges[s])-1,-c])

for i in range(M):
    add_edge(src,pb+i,1,0)

B=M*T+1
c=T//L

for i in range(N):
    k,*a=l[i]
    for p in a:
        add_edge(pb+p-1,ub+i,1,0)
    for j in range(1,min(c,k)+1):
        add_edge(ub+i,dst,1,j*L-B)

def min_cost_flow(src,dst,flow):
    cost_sum=0
    max_flow=0

    while flow:
        dist=[float('inf')]*(dst+1)
        inq=[0]*(dst+1)
        prev=[(-1,-1)]*(dst+1)

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

        if dist[dst]==float('inf'):
            break

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
        max_flow+=fl
        cost_sum+=fl*dist[dst]

    return max_flow,cost_sum

r,c=min_cost_flow(src,dst,M)
print(r,c+B*r)