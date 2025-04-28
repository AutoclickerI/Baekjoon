n,k,*a=map(int,open(m:=0).read().split())
for i in range(n):s=0;m=max(m,sum(s<(s:=s+j*(s+j<=k))for j in a[i:]))
print(m)