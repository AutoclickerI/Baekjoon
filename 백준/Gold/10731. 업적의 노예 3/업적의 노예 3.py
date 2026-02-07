N,K,M=map(int,input().split())
for r in range(N):print(2*pow(2*N-K,M,m:=10**9+7)*[1,-~r*pow(K+1,M,m)][r<K]%m)