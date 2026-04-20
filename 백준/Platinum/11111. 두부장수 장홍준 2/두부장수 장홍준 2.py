from heapq import*
from collections import*

[N,M],*l=[i.split()for i in open(0)]
N=int(N)
M=int(M)
l=sum(l,[])

d={'A':0,'B':1,'C':2,'D':3,'F':4}
p=[
    [10,8,7,5,1],
    [8,6,4,3,1],
    [7,4,3,2,1],
    [5,3,2,2,1],
    [1,1,1,1,0]
]

def cv(y,x):return y*M+x

src=N*M
dst=src+1

edges=[[]for _ in[0]*(N*M+2)]

def add_edge(s,e,f,c):
    edges[s].append([e,f,len(edges[e]),c])
    edges[e].append([s,0,len(edges[s])-1,-c])

for y in range(N):
    for x in range(M):
        n=cv(y,x)
        if y+x&1:
            add_edge(n,dst,1,0)
        else:
            add_edge(src,n,1,0)
            g=d[l[y][x]]
            for dy,dx in(1,0),(-1,0),(0,1),(0,-1):
                ny,nx=y+dy,x+dx
                if 0<=ny<N and 0<=nx<M:
                    add_edge(n,cv(ny,nx),1,-p[g][d[l[ny][nx]]])

def min_cost_flow(src,dst):
    V=N*M+2
    h=[float('inf')]*V
    inq=[0]*V

    h[src]=0
    q=deque([src])
    inq[src]=1

    while q:
        n=q.popleft()
        inq[n]=0
        for e,f,p,c in edges[n]:
            nd=h[n]+c
            if f and nd<h[e]:
                h[e]=nd
                if inq[e]<1:
                    inq[e]=1
                    q+=e,

    for i in range(V):
        if h[i]==float('inf'):
            h[i]=0

    cost_sum=0

    while 1:
        dist=[float('inf')]*V
        prev=[(-1,-1)]*V

        dist[src]=0
        q=[(0,src)]

        while q:
            cd,n=heappop(q)
            if cd!=dist[n]:
                continue
            for i,(e,f,p,c)in enumerate(edges[n]):
                if f<1:
                    continue
                nd=cd+c+h[n]-h[e]
                if nd<dist[e]:
                    dist[e]=nd
                    prev[e]=n,i
                    heappush(q,(nd,e))

        if dist[dst]==float('inf'):
            break

        fl=dist[dst]+h[dst]-h[src]
        if 0<=fl:
            break

        for i in range(V):
            if dist[i]<float('inf'):
                h[i]+=dist[i]

        n=dst
        while n!=src:
            pn,pi=prev[n]
            e,f,p,c=edges[pn][pi]
            edges[pn][pi][1]-=1
            edges[e][p][1]+=1
            n=pn

        cost_sum+=fl

    return cost_sum

print(-min_cost_flow(src,dst))