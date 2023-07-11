mod=10**9+7
N,a=map(int,input().split())
print(((N-1)*(pow(N,a+1,mod)-pow(N-1,a+1,mod))+pow(N-1,a,mod))%mod)