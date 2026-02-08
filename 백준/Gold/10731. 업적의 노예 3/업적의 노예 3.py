N,K,M=map(int,input().split())
for r in range(N):print(2*pow((K-2*N)*~K,M,m:=10**9+7)*-~min(r,K)%m)