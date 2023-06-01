for _ in[0]*int(input()):
    n=int(input())
    for i in range(int(n**.5),-1,-1):
        if i+i*i<=n:break
    print(i)