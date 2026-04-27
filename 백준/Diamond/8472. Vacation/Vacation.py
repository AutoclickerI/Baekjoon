[N,K],l=[[*map(int,i.split())]for i in open(0)]

DST=4*N

edges=[[]for _ in[0]*-~DST]

def add_edge(s,e,f,c):
    edges[s].append([e,f,len(edges[e]),c])
    edges[e].append([s,0,len(edges[s])-1,-c])

for i in range(DST):
    add_edge(i,i+1,float('inf'),0)

for i in range(3*N):
    add_edge(i,N+i,1,-l[i])

def min_cost_flow(src,dst,flow):
    cost_sum=0
    
    while flow:
        dist=[float('inf')]*-~DST
        inq=[0]*-~DST
        prev=[(-1,-1)]*-~DST
        
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

print(-min_cost_flow(0,DST,K))