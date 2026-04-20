N,M=map(int,input().split())
a=[input()for _ in[0]*N]

c=[[10,8,7,5,1],
   [8,6,4,3,1],
   [7,4,3,2,1],
   [5,3,2,2,1],
   [1,1,1,1,0]]
d={'A':0,'B':1,'C':2,'D':3,'F':4}

V=N*M
SRC=V
DST=V+1
edges=[[]for _ in[0]*(V+2)]

def add_edge(s,e,f,c):
    edges[s].append([e,f,len(edges[e]),c])
    edges[e].append([s,0,len(edges[s])-1,-c])

flow=0
for i in range(N):
    for j in range(M):
        n=i*M+j
        if i+j&1<1:
            flow+=1
            add_edge(SRC,n,1,0)
            add_edge(n,DST,1,0)
            for dy,dx in (1,0),(-1,0),(0,1),(0,-1):
                y,x=i+dy,j+dx
                if 0<=y<N and 0<=x<M:
                    add_edge(n,y*M+x,1,-c[d[a[i][j]]][d[a[y][x]]])
        else:
            add_edge(n,DST,1,0)

def min_cost_flow(src,dst,flow):
    cost_sum=0

    while flow:
        dist=[float('inf')]*(V+2)
        inq=[0]*2*-~V
        prev=[(-1,-1)]*(V+2)

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

        if 0<=dist[dst]:
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
        cost_sum+=fl*dist[dst]
    return cost_sum

print(-min_cost_flow(SRC,DST,flow))