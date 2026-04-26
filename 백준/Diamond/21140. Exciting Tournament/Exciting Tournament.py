[N],*l=[[*map(int,i.split())]for i in open(0)]

S,G=zip(*sorted(l))

V=2*N+2
SRC=2*N
DST=SRC+1

def add_edge(s,e,f,c):
    edges[s].append([e,f,len(edges[e]),c])
    edges[e].append([s,0,len(edges[s])-1,-c])

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
            e,f,p,c=edges[pn][pi]
            edges[pn][pi][1]-=fl
            edges[e][p][1]+=fl
            n=pn
        
        flow-=fl
        cost_sum+=fl*dist[dst]
    
    return cost_sum

def calc(t):
    global edges
    edges=[[]for _ in[0]*V]
    
    for i in range(N-1):
        add_edge(SRC,i,1,0)
    
    for i in range(N-1):
        for j in range(i+1,N):
            add_edge(i,N+j,1,t*(S[i]^S[j]))
    
    for j in range(N):
        add_edge(N+j,DST,G[j]-(j<N-1),0)
    
    return min_cost_flow(SRC,DST,N-1)

print(calc(1),-calc(-1))