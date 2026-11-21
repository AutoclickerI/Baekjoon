N,K=map(int,input().split())
d=[0]*-~K
for _ in[0]*N:
    n=int(input())
    if n<=K:d[n]+=1
    for i in range(n+1,K+1):d[i]=d[i]+d[i-n]
print(d[K])