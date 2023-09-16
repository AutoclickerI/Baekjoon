for i in open(0).read().split()[1:]:
    print(i:=int(i)-1)
    n=9999
    for _ in[0]*i:
        print(-1,n:=n-1)