n,b,c,*l=map(int,open(0).read().split())
c=min(b,c)
p=q=r=C=0
for v in l:X=min(p,v);v-=X;C+=c*X;Y=min(q,v);v-=Y;C+=c*Y;p=Z=v;C+=b*Z;q,r=X,Y
print(C)