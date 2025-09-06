for i in[*open(0)][1:]:
    k,n=i.split()
    k=int(k)
    if len(n)-k==1 and'0'in n:
        print(0)
    else:
        z=2
        r=''
        for c in n[::-1]:
            if z<1:
                if k:
                    k-=1
                else:
                    r+=c
            elif c=='0':
                r+=c
                z-=1
            else:
                k-=1
        if k or z:
            print(-1)
        else:
            print(r[::-1]if'1'<=r[::-1]else-1)