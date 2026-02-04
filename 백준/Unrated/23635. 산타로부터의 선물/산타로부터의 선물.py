K,N,*A=map(int,open(0).read().split())
P=[0]
for i in A:P+=P[-1]+i,
S=P[N]
b=[1e9]*6**9
for i in range(N+1):b[P[i]]=i
for x in range(S)[::-1]:b[x]=min(b[x:x+2])
r=1e9
for m in range(1,S+1):
    p=0
    f=1
    for _ in[0]*K:
        t=P[p]+m
        p=b[t]
        if 1e9<=p:
            f=0
            break
    if f:r=min(P[p]-K*m,r)
print(r)