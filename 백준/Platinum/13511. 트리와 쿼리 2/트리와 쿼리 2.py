import sys
input=sys.stdin.readline

N=int(input())
dl=N.bit_length()
p=[dl*[0]for _ in[0]*-~N]
w=[dl*[0]for _ in[0]*-~N]
d=[0]*-~N

edges=[[]for _ in[0]*-~N]
for _ in[0]*~-N:
    u,v,c=map(int,input().split())
    edges[u]+=(v,c),
    edges[v]+=(u,c),

l=[(1,1)]
v=[0]*-~N
v[1]=1
for n,dd in l:
    d[n]=dd
    for e,c in edges[n]:
        if v[e]<1:
            v[e]=1
            p[e][0]=n
            w[e][0]=c
            l+=(e,dd+1),

for j in range(dl-1):
    for i in range(N+1):
        p[i][j+1]=p[p[i][j]][j]
        w[i][j+1]=w[i][j]+w[p[i][j]][j]

def up(n,k):
    r=0
    while k:
        bl=k.bit_length()-1
        r+=w[n][bl]
        n=p[n][bl]
        k-=1<<bl
    return n,r

def LCA(u,v):
    if d[u]<d[v]:
        u,v=v,u
    u,r=up(u,d[u]-d[v])
    if u==v:
        return u,r
    for k in range((d[u]-1).bit_length())[::-1]:
        uk=1<<k
        if up(u,uk)[0]!=up(v,uk)[0]:
            u,dr=up(u,uk)
            r+=dr
            v,dr=up(v,uk)
            r+=dr
    u,dr=up(u,1)
    r+=dr
    v,dr=up(v,1)
    r+=dr
    return u,r

for _ in[0]*int(input()):
    q,u,v,*k=map(int,input().split())
    if q<2:
        print(LCA(u,v)[1])
    else:
        [k]=k
        lca,_=LCA(u,v)
        if k<=d[u]-d[lca]:
            print(up(u,k-1)[0])
        else:
            tot=d[u]+d[v]-2*d[lca]
            print(up(v,tot-k+1)[0])