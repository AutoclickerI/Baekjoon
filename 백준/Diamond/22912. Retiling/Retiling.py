import sys
input=sys.stdin.readline

def add_edge(s,e,f,c):
    edges[s].append([e,f,len(edges[e]),c])
    edges[e].append([s,0,len(edges[s])-1,-c])

def min_cost_flow(src,dst,flow):
    cost_sum=0
    
    while flow:
        dist=[float('inf')]*(n+m+2)
        inq=[0]*(n+m+2)
        prev=[(-1,-1)]*(n+m+2)
        
        dist[src]=0
        l=[src]
        inq[src]=1
        
        for v in l:
            inq[v]=0
            for i,(e,f,p,c)in enumerate(edges[v]):
                nd=dist[v]+c
                if f and nd<dist[e]:
                    dist[e]=nd
                    prev[e]=v,i
                    if inq[e]<1:
                        inq[e]=1
                        l+=e,
        
        if prev[dst]==(-1,-1)or 0<=dist[dst]:
            break
        
        fl=flow
        v=dst
        while v!=src:
            pv,pi=prev[v]
            fl=min(fl,edges[pv][pi][1])
            v=pv
        
        v=dst
        while v!=src:
            pv,pi=prev[v]
            e,f,p,cost=edges[pv][pi]
            edges[pv][pi][1]-=fl
            edges[e][p][1]+=fl
            v=pv
        
        flow-=fl
        cost_sum+=fl*dist[dst]
    return cost_sum

for T in range(int(input())):
    R,C,F,S=map(int,input().split())
    a=[input()for _ in[0]*R]
    b=[input()for _ in[0]*R]
    
    x=[]
    y=[]
    for i in range(R):
        for j in range(C):
            if a[i][j]!=b[i][j]:
                if a[i][j]=='M':
                    x+=[(i,j)]
                else:
                    y+=[(i,j)]
    
    n=len(x)
    m=len(y)
    src=n+m
    dst=n+m+1
    
    edges=[[]for _ in[0]*(n+m+2)]
    
    for i in range(n):
        add_edge(src,i,1,0)
    for j in range(m):
        add_edge(n+j,dst,1,0)
    
    for i in range(n):
        x1,y1=x[i]
        for j in range(m):
            x2,y2=y[j]
            d=(abs(x1-x2)+abs(y1-y2))*S-2*F
            add_edge(i,n+j,1,d)
    
    print(f'Case #{T+1}:',(n+m)*F+min_cost_flow(src,dst,min(n,m)))