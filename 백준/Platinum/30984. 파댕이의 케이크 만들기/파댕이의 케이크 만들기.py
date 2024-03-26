mod=10**9+7
N,K=map(int,input().split())
fact=[1]
for i in range(1,N*K+1):
    fact+=fact[-1]*i%mod,
ans=fact[N*K]
for i in range(N):
    ans*=fact[i]*pow(fact[K+i],-1,mod)
    ans%=mod
def comb_inv(n,k):
    return fact[k]*fact[n-k]*pow(fact[n],-1,mod)%mod
t=N*K
while t:
    ans*=comb_inv(t,K)
    t-=K
    ans%=mod
print(ans)