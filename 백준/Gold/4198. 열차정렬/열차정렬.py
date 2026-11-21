from bisect import*

N,*l=map(int,open(0).read().split())

m=0

for i in range(N):
    f=[l[i]]
    b=[-l[i]]
    for v in l[i+1:]:
        if f[-1]<v:
            f+=v,
        elif f[0]<v:
            f[bisect(f,v)]=v
        v*=-1
        if b[-1]<v:
            b+=v,
        elif b[0]<v:
            b[bisect(b,v)]=v
    m=max(len(f)+len(b)-1,m)
print(m)