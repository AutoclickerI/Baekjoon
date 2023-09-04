while~(n:=int(input())):
    a=0
    for _ in[s:=0]*n:
        p,q=map(int,input().split())
        a+=p*(q-s)
        s=q
    print(a,'miles')