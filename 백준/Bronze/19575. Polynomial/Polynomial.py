_,x,*l=map(int,open(v:=0).read().split())
for p in l[::2]:v=(v*x+p)%(10**9+7)
print(v)