[N,_],*l=[map(int,i.split())for i in open(0)]

edges=[[]for _ in[0]*N]
end=[-1]*N

for s,e in l:
    edges[s-1]+=e-1,

def DFS(n):
    v[n]=1
    for e in edges[n]:
        if end[e]<0 or v[end[e]]<1 and DFS(end[e]):
            end[e]=n
            return 1
    return 0

r=0
for i in range(N):
    v=[0]*N
    r+=DFS(i)

print(r)