for _ in[0]*int(input()):
    c=0
    n,m=map(int,input().split())
    for a in range(1,n):
        for b in range(a+1,n):
            c+=((a*a+b*b+m)%(a*b)==0)
    print(c)