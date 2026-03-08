for _ in[0]*int(input()):
    M,N,A,B=map(int,input().split())
    *a,=map(int,input().split())
    *b,=map(int,input().split())
    c=[[*map(int,input().split())]for _ in[0]*M]

    SRC=2*N
    DST=2*N+1
    edges=[[]for _ in[0]*2*-~N]

    def add_edge(s,e,f,c):
        edges[s].append([e,f,len(edges[e]),c])
        edges[e].append([s,0,len(edges[s])-1,-c])

    for j in range(N):
        if a[j]:
            add_edge(SRC,j,a[j],0)

    for j in range(N):
        for k in range(N):
            add_edge(j,N+k,float('inf'),min(A*c[i][j]+B*c[i][k]for i in range(M)))

    for k in range(N):
        if b[k]:
            add_edge(N+k,DST,b[k],0)

    def min_cost_flow(src,dst,flow):
        cost_sum=0

        while flow:
            dist=[float('inf')]*2*-~N
            inq=[0]*2*-~N
            prev=[(-1, -1)]*2*-~N

            dist[src]=0
            l=[src]
            inq[src] = 1

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

    print(min_cost_flow(SRC,DST,sum(a)))