N,Q=map(int,input().split())

edges=[[]for _ in[0]*-~N]

for _ in[0]*~-N:
    s,e,c=map(int,input().split())
    edges[s]+=(e,c),
    edges[e]+=(s,c),

def BFS():
    l=[v]
    x=[0]*-~N
    x[v]=1
    for n in l:
        for e,c in edges[n]:
            if k<=c and x[e]<1:
                x[e]=1
                l+=e,
    return len(l)
for _ in[0]*Q:
    k,v=map(int,input().split())
    print(BFS()-1)