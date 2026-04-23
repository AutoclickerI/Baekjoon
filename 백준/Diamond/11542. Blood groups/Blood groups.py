[N,Q],*l=[[*map(int,i.split())]for i in open(0)]

p=[]
full=0
for b,*v in l[:N]:
    m=0
    for x in v:
        m|=1<<x-1
    p+=[m]
    full+=b==N

for _,*v in l[N:]:
    t=0
    for x in v:
        t|=1<<x-1

    if t<1:
        print('NY'[full<1])
        continue

    a=[i for i in range(N)if t>>i&1]
    K=len(a)

    src=K+N
    dst=src+1
    V=dst+1

    edges=[[]for _ in[0]*V]

    def add_edge(s,e,f,c):
        edges[s].append([e,f,len(edges[e]),c])
        edges[e].append([s,0,len(edges[s])-1,-c])

    for i in range(K):
        add_edge(src,i,1,0)

    for j in range(N):
        add_edge(K+j,dst,1,0)

    for i,x in enumerate(a):
        b=1<<x
        for j,m in enumerate(p):
            if m&b:
                add_edge(i,K+j,1,0)

    flow=K
    got=0

    while flow:
        dist=[float('inf')]*V
        inq=[0]*V
        prev=[(-1,-1)]*V

        dist[src]=0
        q=[src]
        inq[src]=1
        qi=0

        while qi<len(q):
            n=q[qi]
            qi+=1
            inq[n]=0
            for i,(e,f,pv,c)in enumerate(edges[n]):
                nd=dist[n]+c
                if f and nd<dist[e]:
                    dist[e]=nd
                    prev[e]=n,i
                    if inq[e]<1:
                        inq[e]=1
                        q+=e,

        if prev[dst][0]<0:
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
            e,f,pv,cost=edges[pn][pi]
            edges[pn][pi][1]-=fl
            edges[e][pv][1]+=fl
            n=pn

        flow-=fl
        got+=fl

    print('NY'[got==K])