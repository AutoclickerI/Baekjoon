[N],*l=[[*map(int,i.split())]for i in open(0)]
edges=[[]for _ in l]
for i in range(N):
    for j in range(N):
        if l[i]==l[j]:
            if i<j:
                edges[i]+=j,
        else:
            if all(p<=q for p,q in zip(l[i],l[j])):
                edges[j]+=i,

end=[-1]*N

def DFS(n):
    v[n]=1
    for e in edges[n]:
        if end[e]<0 or v[end[e]]<1 and DFS(end[e]):
            end[e]=n
            return 1
    return 0

edges*=2
for i in range(2*N):
    v=[0]*2*N
    DFS(i)

print(sum(i<0 for i in end))