import sys
sys.setrecursionlimit(9**9)

[N,Q],*l=[map(int,i.split())for i in open(0)]
*p,=range(N+1)
def find(n):
    if p[n]!=n:
        p[n]=find(p[n])
    return p[n]
d=[0,1]
for i in l[:N-1]:
    d+=i
r=[]
for q,i,*j in l[N-1:][::-1]:
    if q:
        r+='YNEOS'[find(i)!=find(*j)::2],
    else:
        s,e=sorted([find(i),find(d[i])])
        p[e]=s
for i in r[::-1]:print(i)