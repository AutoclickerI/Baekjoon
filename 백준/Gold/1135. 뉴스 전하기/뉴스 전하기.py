N,*l=map(int,open(0).read().split())
edges=[[]for _ in[0]*N]
for i in range(1,N):
    edges[l[i]]+=i,


def DFS(n):
    if edges[n]==[]:
        return 0
    l=sorted(DFS(e)for e in edges[n])
    N=len(l)
    return max(v+N-i for i,v in enumerate(l))

print(DFS(0))