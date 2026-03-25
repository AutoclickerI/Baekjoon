mod=10**9+7
N,M=map(int,input().split())
if 2 in[N,M]:exit(print(2))
f=[1]
for i in range(1,N+M):f+=f[-1]*i%mod,

def comb(n,r):
    return f[n]*pow(f[r]*f[n-r],-1,mod)%mod

print(2*(comb(N+M-4,M-2)**2-comb(N+M-4,M-1)*comb(N+M-4,N-1))%mod)