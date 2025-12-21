N,K,*l=map(int,open(0).read().split())
s=0
e=0
c=0
m=float('inf')
while s<N:
    if c<K and e<N:
        c+=l[e]<2
        e+=1
    else:
        c-=l[s]<2
        s+=1
    if c==K:
        m=min(m,e-s)
print(-(m==float('inf'))or m)