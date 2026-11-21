N,M,K=map(int,input().split())
d=N+M-1>K
print('YNEOS'[d::2])
exec(-~-d*'print(*range(d:=d+1,d+M));'*N)