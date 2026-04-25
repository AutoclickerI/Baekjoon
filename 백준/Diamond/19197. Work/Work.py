N,M=map(int,input().split())
*A,=zip(*[input()for _ in[0]*N])

SRC=N+M
DST=SRC+1

edges=[[]for _ in[0]*(DST+1)]

def add_edge(s,e,f,c):
    edges[s].append([e,f,len(edges[e]),c])
    edges[e].append([s,0,len(edges[s])-1,-c])

cnt=0
ok=[]

for j in range(M):
    f='1'in A[j]
    ok+=f,
    if f:
        cnt+=1
        add_edge(SRC,N+j,1,0)

for j,v in enumerate(ok):
    for i in range(N):
        if v and A[j][i]=='1':
            add_edge(N+j,i,1,0)

used=[0]*N

for i in range(N):
    add_edge(i,DST,1,1)

def min_cost_flow(src,dst,flow):
    cost_sum=0
    
    while flow:
        dist=[float('inf')]*(DST+1)
        inq=[0]*(DST+1)
        prev=[(-1,-1)]*(DST+1)
        
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
        
        lst=-1
        n=dst
        while n!=src:
            pn,pi=prev[n]
            e,f,p,cost=edges[pn][pi]
            if e==dst:
                lst=pn
            edges[pn][pi][1]-=fl
            edges[e][p][1]+=fl
            n=pn
        
        if lst!=-1:
            used[lst]+=1
            add_edge(lst,dst,1,2*used[lst]+1)
        
        flow-=fl
        cost_sum+=fl*dist[dst]
    
    return cost_sum

min_cost_flow(SRC,DST,cnt)

ans=[[]for _ in[0]*N]

for j in range(M):
    if ok[j]:
        for e,f,p,c in edges[N+j]:
            if 0<=e<N and f==0:
                ans[e].append(j+1)
                break

for v in ans:
    print(len(v),*v)