import sys
sys.setrecursionlimit(2*10**5)

N=int(input())
edges=[[]for _ in[0]*N]
v=[0]*N
for i in range(1,N):
    t,c,p=input().split()
    edges[int(p)-1]+=i,
    v[i]=int(c)*(-('S'<t)|1)

def DFS(n):
    r=v[n]
    for e in edges[n]:
        r+=DFS(e)
    return max(r,0)

print(DFS(0))