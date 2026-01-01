A,B,N,M=map(int,input().split())
v=[0]*100001
l=[(0,N)]
for c,n in l:
    if n==M:
        print(c)
        break
    for e in n-1,n+1,n-A,n+A,n-B,n+B,n*A,n*B:
        if 0<=e<100001 and v[e]<1:
            v[e]=1
            l+=(c+1,e),