import sys
input=sys.stdin.readline

N,M,K=map(int,input().split())

edges=[[]for _ in[0]*-~N]
deg=[0]*-~N
c=[0]*-~N
f=0

for _ in[0]*M:
    s,e=map(int,input().split())
    edges[s]+=e,
    deg[e]+=1

for _ in[0]*K:
    q,n=map(int,input().split())
    if q<2:
        if deg[n]:
            f=1
        c[n]+=1
        for e in edges[n]:
            if c[n]==1:
                deg[e]-=1
    else:
        if c[n]<1:
            f=1
        c[n]-=1
        for e in edges[n]:
            if c[n]==0:
                deg[e]+=1

print(f*'Lier!'or'King-God-Emperor')