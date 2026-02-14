N,M,*A=map(int,open(s:=0).read().split())
e=2<<50
while-~s<e:m=s+e>>1;s,e=[s,m,m,e][sum(m//i for i in A)<M::2]
print(e)