n,a,b,c=map(int,input().split())
if n==1:print(0,0)
else:
    if a==min(a,b,c):
        a*=n-1
        print(a//100,a%100)
    elif b==min(a,b,c):
        b*=n-1
        print(b//100,b%100)
    else:
        K=min(a,b)
        K+=c*(n-2)
        print(K//100,K%100)