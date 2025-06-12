N,P=map(int,input().split())
a=1
if P<N*2:
    for i in range(N+1,P):a*=i;a%=P
    a=pow(-a,-1,P)
else:
    for i in range(1,N+1):a*=i;a%=P
print(a)