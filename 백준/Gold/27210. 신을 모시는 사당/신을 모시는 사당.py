N,*l=map(int,open(0).read().split())
v,*l=[i*2-3 for i in l]
m=v
nm=nv=v
for i in l:
    v=max(v,0)+i
    nv=min(nv,0)+i
    m=max(v,m)
    nm=min(nv,nm)
print(max(m,-nm))