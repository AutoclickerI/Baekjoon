N,M,*A=map(int,open(s:=0).read().split())
e=2<<50
while-~s<e:s,e=[s,m:=s+e>>1,m,e][sum(m//i for i in A)<M::2]
print(e)