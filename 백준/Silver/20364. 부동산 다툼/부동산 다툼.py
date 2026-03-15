N,Q,*l=map(int,open(0).read().split())

v=[0]*-~N

for i in l:
    r=0
    k=i
    while i:
        if v[i]:
            r=i
        i>>=1
    v[k]=1
    print(r)