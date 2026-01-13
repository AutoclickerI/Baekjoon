[M,N],*l=[[*map(int,i.split())][::-1]for i in open(0)]
l.sort()
def find(n):
    if p[n]!=n:
        p[n]=find(p[n])
    return p[n]

*p,=range(N+1)

v=0
for c,*x in l:
    s,e=sorted(map(find,x))
    if s-e:
        p[e]=s
        v+=1-c

v2=0
*p,=range(N+1)
for c,*x in l[::-1]:
    s,e=sorted(map(find,x))
    if s-e:
        p[e]=s
        v2+=1-c
print(v*v-v2**2)