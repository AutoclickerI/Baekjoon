T=int(input())
for i in range(T):
    n=int(input())
    s,t=map(int,input().split())
    ans=0
    while n:
        if n%2:
            ans+=s
            n-=1
        else:
            n//=2
            if n*s>t:
                ans+=t
            else:
                ans+=n*s
    print(ans) 