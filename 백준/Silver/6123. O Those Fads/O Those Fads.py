_,L,K,*l=map(int,open(a:=0).read().split())
for i in sorted(l):f=i<=L;a+=f;L+=K*f
print(a)