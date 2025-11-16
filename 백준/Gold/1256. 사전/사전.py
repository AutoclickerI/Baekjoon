import math
N,M,K=map(int,input().split())
v=math.comb(N+M,M)
if v<K:
    print(-1)
else:
    s=''
    while N+M:
        if math.comb(N+M-1,M)<K:
            K-=math.comb(N+M-1,M)
            s+='z'
            M-=1
        else:
            s+='a'
            N-=1
    print(s)