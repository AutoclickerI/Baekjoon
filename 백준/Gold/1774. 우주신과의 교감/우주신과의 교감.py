N,M=map(int,input().split())
c=[[*map(int,input().split())]for _ in[0]*N]

*p,=range(N+1)

def find(n):
    if n!=p[n]:
        p[n]=find(p[n])
    return p[n]
def union(a,b):
    a,b=sorted([find(a),find(b)])
    p[b]=a

for _ in[0]*M:
    union(*map(int,input().split()))

d=[]

for i in range(N):
    for j in range(i+1,N):
        y,x=c[i]
        yy,xx=c[j]
        d+=((y-yy)**2+(x-xx)**2,i+1,j+1),

d.sort()

ans=0

for dist,i,j in d:
    if find(i)!=find(j):
        union(i,j)
        ans+=dist**.5
print('%.2f'%ans)