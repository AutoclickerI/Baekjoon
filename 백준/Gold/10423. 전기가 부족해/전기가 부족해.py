[K,M,N],d,*l=[[*map(int,i.split())][::-1]for i in open(0)]
*p,=range(N+1)
for i in d:p[i]=0
def find(n):
    if p[n]!=n:
        p[n]=find(p[n])
    return p[n]
r=0
for c,*x in sorted(l):
    s,e=sorted(map(find,x))
    if s-e:
        r+=c
        p[e]=s
print(r)