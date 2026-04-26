[N,M],*l=[map(int,i.split())for i in open(0)]

edges=[[]for _ in[0]*-~N]

for i,(u,v)in enumerate(l,1):
    edges[u-1]+=(v-1,i),

bl=N.bit_length()
C=1<<bl
R=2*bl
P=[1<<i for i in range(R+1)]

def chk(k):
    b=k-bl
    dp=[float('inf')]*N
    dp[0]=0
    
    for u in range(N):
        d=dp[u]
        if d==float('inf'):
            continue
        
        for v,i in edges[u]:
            if i<b:
                w=-C
            else:
                t=i-b
                w=float('inf')if R<t else P[t]-C
            
            nd=d+w
            if nd<dp[v]:
                dp[v]=nd
    return dp[-1]<0

s=1
e=M+1

while 1<e-s:
    m=s+e>>1
    if chk(m):
        e=m
    else:
        s=m

print(s)