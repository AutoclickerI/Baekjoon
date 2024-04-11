for i in range(int(input())):
    L,N=map(int, input().split())
    a=p=0
    d='C'
    for _ in range(N):
        D,C=input().split()
        c,p=divmod(p*((C==d)*2-1)+int(D),L)
        if c!=-1:d=C
        a+=c
    print(f"Case #{i+1}: {a}")