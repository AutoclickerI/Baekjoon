[N,Q],*l=[[*map(int,i.split())]for i in open(0)]

q=0
v=[]
for x1,x2,y in l[:N]:
    v+=(x1,x2,q:=q+1),
v.sort()

*p,=range(N+1)

def find(n):
    if p[n]!=n:
        p[n]=find(p[n])
    return p[n]

def merge(a,b):
    a,b=sorted([find(a),find(b)])
    p[b]=a

m=0
for(x1,x2,i1),(p1,p2,i2)in zip(v,v[1:]):
    m=max(m,x2)
    if p1<=m:
        merge(i1,i2)

for a,b in l[N:]:
    print(+(find(a)==find(b)))