for i in range(int(input())):
    n=2*int(input())
    l=[]
    while len(l)<n:
        l+=map(int,input().split())
    a=b=0
    while l:
        p,q,*l=l
        if p>q:
            if q==p-1:
                a+=(p+q)*(1+(q==1))
            else:
                b+=p
        if p<q:
            if p==q-1:
                b+=(p+q)*(1+(p==1))
            else:
                a+=q
    print(f'Game {i+1}: Tessa {b} Danny {a}')