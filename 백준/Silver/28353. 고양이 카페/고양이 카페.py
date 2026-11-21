N,K,*l=map(int,open(0).read().split())
l.sort()
r=0
s=0
e=N-1
while s<e:
    while s<e and K<l[s]+l[e]:
        e-=1
    if s<e:
        s+=1
        e-=1
        r+=1
print(r)