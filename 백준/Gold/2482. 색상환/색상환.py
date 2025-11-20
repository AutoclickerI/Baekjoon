mod=10**9+3
N,K=map(int,open(0))

def getval(N,K):
    if K==0:return 1
    oc=[0]*K
    noc=[0]*K
    for _ in[0]*N:
        oc_t=[0]*K
        noc_t=[0]*K
        for i in range(K):
            noc_t[i]=(oc[i]+noc[i])%mod
            oc_t[i]=noc[i-1]
        oc_t[0]=1
        oc=oc_t
        noc=noc_t
    return noc[-1]+oc[-1]


print((getval(N-3,K-1)+getval(N-1,K))%mod)