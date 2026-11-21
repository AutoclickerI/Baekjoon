for i in[*open(0)][1:]:
    print("Data set:",i[:-1])
    p,q,r=map(int,i.split())
    p,q=sorted([p,q])
    while r:
        r-=1
        if p>q:p//=2
        else:q//=2
    print(*sorted([p,q])[::-1])
    print()