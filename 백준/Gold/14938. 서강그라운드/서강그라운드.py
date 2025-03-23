N,M,R=map(int,input().split())

*l,=map(int,input().split())

b=[[9**9*(i!=j)for i in range(N)]for j in range(N)]

for _ in[0]*R:
    s,e,c=map(int,input().split())
    s-=1
    e-=1
    b[s][e]=min(b[s][e],c)
    b[e][s]=min(b[e][s],c)

for m in range(N):
    for s in range(N):
        for e in range(N):
            b[s][e]=min(b[s][e],b[s][m]+b[m][e])
m=0
for i in b:
    v=0
    for c,r in zip(i,l):
        v+=r*(c<=M)
    m=max(m,v)
print(m)