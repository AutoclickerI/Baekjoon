_,*l=[[*map(int,i.split())]for i in open(0)]
m=1e9
for i,j in l:
    t=0
    for k,p in l:
        t+=((i-k)**2+(j-p)**2)**.5
    m=min(t,m)
print(m/~-len(l))