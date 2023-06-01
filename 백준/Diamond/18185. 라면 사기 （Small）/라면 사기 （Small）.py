n,*l=map(int,open(0).read().split())
p=q=r=C=0
for v in l:X=min(p,v);v-=X;C+=2*X;Y=min(q,v);v-=Y;C+=2*Y;p=Z=v;C+=3*Z;q,r=X,Y
print(C)