for T in range(int(input())):
    p,*l=map(int,input().split())
    if p-1:
        q,r=l
        depth=0
        width=0
        while q!=r:
            if q>r:
                q-=r
                width+=1<<depth
            else:
                r-=q
            depth+=1
        print(f'Case #{T+1}:',2**depth+width)
    else:
        p,=l
        n=p.bit_length()-1
        q=r=1
        while n:
            if p%2**n>=1<<n-1:
                q+=r
            else:
                r+=q
            n-=1
        print(f'Case #{T+1}:',q,r)