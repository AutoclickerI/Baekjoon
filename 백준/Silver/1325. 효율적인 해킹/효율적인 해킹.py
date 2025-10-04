(N,M),*l=[[*map(int,i.split())]for i in open(0)]

edges=[[]for _ in[0]*-~N]
v=[]
for e,s in l:
    edges[s]+=e,
    v+=s,

def BFS(n):
    f=1
    visited[n]=1
    ll=[n]
    for n in ll:
        for e in edges[n]:
            if visited[e]<1:
                visited[e]=1
                ll+=e,
                f+=1
    return f
        
ans=[]
mv=0
for i in{*v}:
    visited=[0]*-~N
    vv=BFS(i)
    if mv<vv:
        mv=vv
        ans=[i]
    elif mv==vv:
        ans+=i,

print(*sorted(ans))