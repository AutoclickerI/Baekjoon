[N,M],*l=[map(int,i.split())for i in open(0)]

*p,=range(N+1)

def find(n):
    if p[n]!=n:
        p[n]=find(p[n])
    return p[n]

c=0
for u,v in l:
    u,v=sorted([find(u),find(v)])
    if u-v:
        c+=1
        p[v]=u
print(M+N-1-2*c)