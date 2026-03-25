[N,M,t],*l=[[*map(int,i.split())]for i in open(0)]

r=0

*p,=range(N+1)

def find(n):
    if n!=p[n]:
        p[n]=find(p[n])
    return p[n]

def merge(a,b):
    a,b=sorted([find(a),find(b)])
    p[b]=a

for s,e,c in sorted(l,key=lambda i:i[2]):
    if find(s)!=find(e):
        r+=c
        merge(s,e)

print(r+t*(N-2)*(N-1)//2)