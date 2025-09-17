n,*l,q=map(int,open(s:=0).read().split())
e=max(l)+1
while-~s<e:s,e=[m:=s+e>>1,s,e,m][q<sum(map(min,l,[m]*n))::2]
print(s)