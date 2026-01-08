s='0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
N=int(input())
b=[input()for _ in[0]*N]
*p,=range(N)
def find(n):
    if p[n]!=n:
        p[n]=find(p[n])
    return p[n]
r=0
edges=[]
for y in range(N):
    for x in range(N):
        edges+=(s.find(b[y][x]),y,x),
edges.sort()
for c,y,x in edges:
    y,x=sorted([find(y),find(x)])
    r+=c
    if y-x and c:
        p[x]=y
        r-=c
s={find(i)for i in range(N)}
if len(s)<2:
    print(r)
else:
    print(-1)