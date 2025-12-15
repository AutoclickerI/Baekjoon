import sys
sys.setrecursionlimit(2*10**5)

[N],*l=[map(int,i.split())for i in open(0)]
edges=[[]for _ in[0]*-~N]

for s,e in l:
    edges[s]+=e,
    edges[e]+=s,

v=[0]*-~N

def DFS(n,p=-1):
    global css
    v[n]=1
    for e in edges[n]:
        if e!=p:
            if v[e]<1:
                if DFS(e,n):
                    v[n]=2
                    return 1
            else:
                css=e
                v[n]=2
                return 1
DFS(1)
v=[0]*-~N
DFS(css)


l=[(1,i)for i in range(N+1)if 1<v[i]]
d=[0]*-~N
for i in range(N+1):
    if 1<v[i]:d[i]=1
for c,n in l:
    for e in edges[n]:
        if d[e]<1:
            d[e]=c+1
            l+=(c+1,e),
print(*[i-1 for i in d[1:]])