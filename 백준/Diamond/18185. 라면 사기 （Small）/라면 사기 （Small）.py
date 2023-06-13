n,*l=map(int,open(0).read().split())
p=q=C=0
for v in l:X=min(p,v);Y=min(q+X,v);v-=Y;C+=2*Y+3*v;p,q=v,X
print(C)