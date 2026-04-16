for _ in[0]*int(input()):
    N,P=map(int,input().split())
    C=[[*map(int,input().split())]for _ in[0]*(N-1)]
    D=[[*map(int,input().split())]for _ in[0]*(N-1)]
    O=[[*map(int,input().split())]for _ in[0]*(N-1)]

    edges=[[]for _ in[0]*(N+4)]
    b=[0]*(N+4)

    def add_edge(s,e,f,c):
        edges[s].append([e,f,len(edges[e]),c])
        edges[e].append([s,0,len(edges[s])-1,-c])

    def add_edge_lb(s,e,l,r,c):
        if l<r:
            add_edge(s,e,r-l,c)
        b[s]-=l
        b[e]+=l

    add_edge_lb(N,0,0,P,0)

    for i in range(N-1):
        add_edge_lb(i,i+1,0,float('inf'),0)

    for i in range(N-1):
        for j in range(1,N-i):
            if D[i][j-1]:
                add_edge_lb(i,i+j,0,D[i][j-1],-C[i][j-1])
            if O[i][j-1]:
                add_edge_lb(i,i+j,O[i][j-1],O[i][j-1],0)

    add_edge_lb(N-1,N+1,0,P,0)
    add_edge_lb(N+1,N,P,P,0)

    need=0
    for i in range(N+4):
        if b[i]>0:
            add_edge(N+2,i,b[i],0)
            need+=b[i]
        elif b[i]<0:
            add_edge(i,N+3,-b[i],0)

    def min_cost_flow(src,dst,flow):
        cost_sum=0

        while flow:
            dist=[float('inf')]*(N+4)
            inq=[0]*(N+4)
            prev=[(-1,-1)]*(N+4)

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

    print(-min_cost_flow(N+2,N+3,need))