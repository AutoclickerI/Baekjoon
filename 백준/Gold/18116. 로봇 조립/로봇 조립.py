N=10**6+1
*p,=range(N)
c=[1]*N

def find(n):
    if n!=p[n]:
        p[n]=find(p[n])
        c[n]=0
    return p[n]

def merge(a,b):
    a,b=sorted(map(find,[a,b]))
    if a!=b:
        c[a]+=c[b]
        c[b]=0
        p[b]=a

for i in[*open(0)][1:]:
    q,s,*e=i.split()
    if q=='Q':
        n=find(int(s))
        print(c[n])
    else:
        s,e=map(int,[s]+e)
        merge(s,e)