for i in[*open(0)][1:]:
    *l,k=map(int,i.split())
    a,b=sorted(l)
    ans=-1
    if a<100>b:
        for i in range(a):
            if b-i==(a-i)*k:ans=i;break
    elif a>99:
        if k==1:ans=0
        else:
            for i in range(99):
                if 99+min(0,b-a-i)==(99-i)*k:ans=a-99+i;break
    else:
        for i in range(a):
            if min(99,b-i)==(a-i)*k:ans=i;break 
    print(ans)