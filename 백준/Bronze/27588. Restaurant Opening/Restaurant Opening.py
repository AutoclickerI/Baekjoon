N,M=map(int,input().split())
l=[[*map(int,input().split())]for _ in[0]*N]
print(min(sum(l[k][n]*(abs(k-i)+abs(n-j))for k in range(N)for n in range(M))for i in range(N)for j in range(M)))