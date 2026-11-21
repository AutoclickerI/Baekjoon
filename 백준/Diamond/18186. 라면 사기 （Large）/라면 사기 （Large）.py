n,b,c,*l=map(int,open(0).read().split())
p=q=C=0
for v in l:Y=min(q+(q:=min(p,v)),v);p=v=v-Y;C+=min(b,c)*Y+b*v
print(C)