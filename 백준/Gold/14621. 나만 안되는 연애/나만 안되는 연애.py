import sys
sys.setrecursionlimit(2*10**5)
input=sys.stdin.readline

N,M=map(int,input().split())
t=input().split()

edges=[]

for _ in[0]*M:
    u,v,d=map(int,input().split())
    if t[u-1]!=t[v-1]:
        edges+=(d,u-1,v-1),

*p,=range(N)

def find(n):
    if p[n]!=n:
        p[n]=find(p[n])
    return p[n]
def union(s,e):
    s,e=sorted([find(s),find(e)])
    p[e]=s

cnt=0
r=0
for d,u,v in sorted(edges):
    if find(u)!=find(v):
        union(u,v)
        r+=d
        cnt+=1

if cnt==N-1:
    print(r)
else:
    print(-1)