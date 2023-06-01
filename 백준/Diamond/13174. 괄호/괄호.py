m=10**9+7
F=[1]
N,K=map(int,input().split())
Po=[1]
for i in range(1,N):F+=[F[-1]*i%m];Po+=[Po[-1]*K%m]
l=[1]
for i in range(N):
 if i%2:l+=[(K+1)*l[-1]%m]
 else:l+=[(K+1)*l[-1]-Po[i//2]*F[i]*pow(F[i//2]**2*(i//2+1),-1,m)]
print(l[-1]%m)