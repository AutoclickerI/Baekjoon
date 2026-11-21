for i in range(int(input())):
    p,q,r=map(int,input().split())
    l=p*p
    while p:
        p*=q
        l+=p*p
        p//=r
        l+=p*p
    print(f'Case #{i+1}:',l*3.141592653)