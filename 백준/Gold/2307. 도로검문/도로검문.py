from heapq import*

[N,M],*l=[map(int,i.split())for i in open(0)]
edges=[[]for _ in[0]*-~N]

for i,(a,b,t) in enumerate(l):
    edges[a]+=(b,t,i),
    edges[b]+=(a,t,i),

def dijkstra(b,k):
    d=[float('inf')]*-~N
    p=[0]*-~N
    pe=[-1]*-~N
    d[1]=0
    hq=[(0,1)]
    
    while hq:
        c,n=heappop(hq)
        if d[n]<c:
            continue
        if n==N:
            break
        for e,w,i in edges[n]:
            if i==b:
                continue
            nc=c+w
            if nc<d[e]:
                d[e]=nc
                heappush(hq,(nc,e))
                if k:
                    p[e]=n
                    pe[e]=i
    return d[N],p,pe

base,p,pe=dijkstra(-1,1)

if base==float('inf'):
    exit(print(-1))

P=[]
n=N
while n-1:
    P+=pe[n],
    n=p[n]

r=0
for i in P:
    v,_,_=dijkstra(i,0)
    r=max(r,v-base)

print(-(r==float('inf'))or r)