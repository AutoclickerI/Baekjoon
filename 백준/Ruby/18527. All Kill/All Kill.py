n,t,*L=map(int,open(s:=0).read().split())
r=b=t-sum(L)+1
while~-n:s+=L[-n];n-=1;r=r*(s+b+n)%998244353
print(r)