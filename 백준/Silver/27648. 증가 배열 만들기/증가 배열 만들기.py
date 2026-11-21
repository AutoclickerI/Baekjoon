N,M,K=map(int,input().split())
d=N+M-1>K
print('YNEOS'[d::2])
i=0;exec((1-d)*'print(*range(i:=i+1,i+M));'*N)