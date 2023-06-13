n,b,c,*l=map(int,open(0).read().split())
c=min(b,c)
p=q=C=0
for v in l:X=min(p,v);Y=min(q+X,v);v-=Y;C+=c*Y+b*v;p=v;q=X
print(C)