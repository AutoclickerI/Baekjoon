N,*P=map(int,open(0).read().split())

v=[float('inf')]*-~N

v[0]=0
for c in range(1,N+1):
    for i in range(N-c+1):
        v[i+c]=min(v[i+c],v[i]+P[c-1])
print(v[-1])