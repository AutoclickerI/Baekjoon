N,_=map(int,input().split())
*Q,=map(int,input().split())
v=set()
h=set()
vcnt=hcnt=0
cnt=0
f=0
ans=[]
for i in Q:
    # in v
    if cnt+hcnt-(N-hcnt)==i:
        cnt=cnt+hcnt-(N-hcnt)
        ans+=('R',vcnt),
        vcnt-=1
        if vcnt<0:
            f=1
    # in v'
    elif cnt+(N-hcnt)-hcnt==i:
        cnt=cnt+(N-hcnt)-hcnt
        vcnt+=1
        ans+=('R',vcnt),
        if vcnt>N:
            f=1
    # in h
    elif cnt+vcnt-(N-vcnt)==i:
        cnt=cnt+vcnt-(N-vcnt)
        ans+=('C',hcnt),
        hcnt-=1
        if hcnt<0:
            f=1
    # in h'
    elif cnt+(N-vcnt)-vcnt==i:
        cnt=cnt+(N-vcnt)-vcnt
        hcnt+=1
        ans+=('C',hcnt),
        if hcnt>N:
            f=1
    else:
        f=1
if f:
    print(-1)
else:
    for i in ans:
        print(*i)