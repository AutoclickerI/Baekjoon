for i in range(int(input())):
    a,b=list(map(int,input().split()))
    n=(a%10)**(4+b%4)%10
    print(10 if n==0 else n)