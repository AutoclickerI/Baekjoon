[M,N],*l=[[*map(int,i.split())][::-1]for i in open(0)]
*p,=range(N+1)
v=r=0

def find(n):
    if n-p[n]:
        p[n]=find(p[n])
    return p[n]
for c,s,e in sorted(l):
    s,e=sorted([find(s),find(e)])
    if s-e:
        p[e]=s
        v+=1
    else:
        r+=c
if v!=N-1:
    print(-1)
else:
    print(r)