N,M,K=map(int,input().split())
if N<M+K-1 or M*K<N:
    print(-1)
else:
    *r,=range(K,0,-1)
    #K+1 ~ N
    cnt=N-K
    if cnt:
        v=cnt//(M-1)
        lo=cnt-v*(M-1)
        s=K+1
        for _ in[0]*(M-1):
            r+=range(s+v+(0<lo)-1,s-1,-1)
            s+=v+(0<lo)
            lo-=1
    print(*r)