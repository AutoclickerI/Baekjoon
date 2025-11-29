[N],*b=[[*map(int,i.split())]for i in open(0)]
l=[]
for i in range(N):
    for j in range(i,N):
        l+=(b[i][j],i,j),

l.sort()

*p,=range(N)

def find(n):
    if p[n]!=n:
        p[n]=find(p[n])
    return p[n]
r=0
for c,*v in l:
    s,e=sorted(map(find,v))
    if s!=e:
        r+=c
        p[e]=s
print(r)