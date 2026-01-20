N=int(input())
M=int(input())
*p,=range(N+1)
edges=[[]for _ in[0]*-~N]
def find(n):
    if p[n]!=n:
        p[n]=find(p[n])
    return p[n]

for _ in[0]*M:
    s,e=map(int,input().split())
    edges[s]+=e,
    edges[e]+=s,
    s,e=sorted(map(find,[s,e]))
    p[e]=s

def BFS(n):
    v=[0]*-~N
    l=[n,*edges[n]]
    for i in l:
        v[i]=1
    for n in l:
        for e in edges[n]:
            if v[e]<1:
                v[e]=v[n]+1
                l+=e,
    return max(i-1 for i in v if i)

d={}
for i in range(1,N+1):
    n=find(i)
    d[n]=d.get(n,[])
    d[n]+=i,
print(len(d))
for v in sorted(min(d[i],key=BFS)for i in d):
    print(v)