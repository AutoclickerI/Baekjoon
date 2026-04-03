for _ in[0]*int(input()):
    n,K=map(int,input().split())
    l=sorted(map(int,input().split()))
    diff=float('inf')
    s=0
    e=n-1
    while s<e:
        d=abs(l[e]+l[s]-K)
        if d<diff:
            diff=d
            c=0
        c+=diff==d
        if abs(l[e]+l[s+1]-K)<abs(l[e-1]+l[s]-K):
            s+=1
        else:
            e-=1
    print(c)