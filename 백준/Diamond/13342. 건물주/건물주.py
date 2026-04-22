N,C,M,W,D=map(int,input().split())
*c,=map(int,input().split())
a=0,*map(int,input().split())

g=[N*[float('inf')]for _ in[0]*N]
for i in range(N):
    for j,x in enumerate(map(int,input().split())):
        if i==j:g[i][j]=0
        elif x:g[i][j]=x

for k in range(N):
    for i in range(N):
        ik=g[i][k]
        if ik==float('inf'):continue
        gi=g[i]
        gk=g[k]
        for j in range(N):
            nd=ik+gk[j]
            if nd<gi[j]:
                gi[j]=nd

src=C+M
dst=src+1
V=dst+1

edges=[[]for _ in[0]*V]

def add_edge(s,e,f,c):
    edges[s].append([e,f,len(edges[e]),c])
    edges[e].append([s,0,len(edges[s])-1,-c])

for i in range(C):
    add_edge(src,i,1,0)

for i in range(M):
    add_edge(C+i,dst,1,0)

for i,x in enumerate(c):
    for j in range(M):
        add_edge(i,C+j,1,W*g[a[j]][x]+D*g[x][a[j+1]]-W*g[a[j]][a[j+1]])

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
        
        if prev[dst][0]<0 or 0<=dist[dst]:
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

print(W*sum(g[i][j]for i,j in zip(a,a[1:]))+min_cost_flow(src,dst,min(C,M)))