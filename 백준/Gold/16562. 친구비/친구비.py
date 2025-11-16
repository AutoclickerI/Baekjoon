[N,M,k],A,*l=[[*map(int,i.split())]for i in open(0)]

*p,=range(N+1)

def find(n):
    if p[n]!=n:
        p[n]=find(p[n])
    return p[n]

for i in l:
    s,e=sorted(map(find,i))
    p[e]=s
d={}
for i in range(N):
    v=find(i+1)
    d[v]=min(d.get(v,float('inf')),A[i])
mv=sum(d.values())
print('Oh no'*(k<mv)or mv)