N,M,K=map(int,input().split())
print(max(N:=N-M*K,0),N+M-1)