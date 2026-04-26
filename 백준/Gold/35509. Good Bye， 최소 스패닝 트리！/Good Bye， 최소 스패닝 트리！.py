[N,M],*l=[[*map(int,i.split())]for i in open(0)]

edges=sorted((w,i+1,u,v)for i,(u,v,w)in enumerate(l))

*p,=range(N+1)

def find(n):
    if n!=p[n]:
        p[n]=find(p[n])
    return p[n]

def union(s,e):
    s,e=sorted([find(s),find(e)])
    p[e]=s

mw=0
sm=0
for w,i,u,v in edges:
    if find(u)!=find(v):
        union(u,v)
        mw=max(mw,w)
        sm+=w

*p,=range(N+1)
r=[]
sm2=0
for w,i,u,v in edges[::-1]:
    if w<=mw and find(u)!=find(v):
        union(u,v)
        sm2+=w
        mw=max(mw,w)
        r+=i,

print('NO')
if sm==sm2:
    print('NO')
else:
    print('YES')
    for i in r:print(i)