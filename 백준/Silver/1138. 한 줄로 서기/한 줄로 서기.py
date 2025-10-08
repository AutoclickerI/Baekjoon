N,*l=map(int,open(0).read().split())

v=[1]*N
c=[0]*N
for i in range(N):
    m=max(j for j in range(N)if sum(v[:j])==l[i])
    c[m]=i+1
    v[m]=0
print(*c)