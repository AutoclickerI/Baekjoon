N,M=map(int,input().split())
a=[input().split()for _ in[0]*N]
b=[input().split()for _ in[0]*N]
[print(*p)for p in[[int(a[j][i])+int(b[j][i])for i in range(M)]for j in range(N)]]