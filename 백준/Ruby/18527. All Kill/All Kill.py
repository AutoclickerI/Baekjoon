m=998244353
N,T,*l=map(int,open(0).read().split())
T+=1
a=1
for i in range(N)[::-1]:T-=l[i]-1;a=a*T%m
print(a*(T-N)*pow(T,-1,m)%m)