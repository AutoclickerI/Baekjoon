[N],_,*l=[map(int,i.split())for i in open(0)]
deg=[0]*-~N
need=[{}for _ in deg]
edges=[[]for _ in deg]
for x,y,k in l:
    edges[y]+=(x,k),
    deg[x]+=1

l=[]
for i in range(1,N+1):
    if deg[i]<1:l+=i,;need[i]={i:1}
for n in l:
    for e,c in edges[n]:
        for i in need[n]:
            need[e][i]=need[e].get(i,0)+need[n][i]*c
        deg[e]-=1
        if deg[e]<1:l+=e,
for i in sorted(need[n]):
    print(i,need[n][i])