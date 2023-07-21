for _ in[0]*int(input()):
    p,q=map(int,input().split())
    r,s=map(int,input().split())
    n=.5/(13-p)
    ans=0
    while(q,p)!=(s,r):
        ans+=n
        p+=1
        if p==13:
            q+=1
            p-=12
            n=1/12
    print(f'{ans+0.0000000001:.4f}')