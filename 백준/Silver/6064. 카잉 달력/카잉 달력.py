import math
for _ in[0]*int(input()):
    M,N,x,y=map(int,input().split())
    ans=y-1
    while ans<2*M*N and ans%M!=x-1:ans+=N
    if x==y==1:
        print(1)
    elif ans%M==x-1 and ans%N==y-1:
        print(ans+1)
    else:print(-1)