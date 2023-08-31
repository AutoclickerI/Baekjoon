while n:=int(input()):
    a,b,c=map(int,input().split())
    if 2*b==a+c:
        print(n*(2*a+(n-1)*(b-a))//2)
    else:
        print(a*((b//a)**n-1)//(b//a-1))