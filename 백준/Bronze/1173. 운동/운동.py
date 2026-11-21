N,m,M,T,R=map(int,input().split())
n=t=0
X=m
if X+T>M:
    print(-1)
    exit()
while n<N:
    if X+T<=M:
        X+=T
        n+=1
    else:
        X=max(m,X-R)
    t+=1
print(t)