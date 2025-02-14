p,q,r=map(int,input().split())
v=max(p,q,r)
if p+q+r&1:
    print(-1)
elif p+q+r==v*2:
    print(0)
else:
    if p+q+r<v*2:
        print([0,p,q,r].index(v))
        print(v-(p+q+r)//2,(p+q+r)//2)
    else:
        print([0,p,q,r].index(z:=p+q+r-min(p,q,r)-v))
        print((p+q+r)//2-min(p,q,r),(p+q+r)//2-max(p,q,r))