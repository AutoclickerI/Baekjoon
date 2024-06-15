def get_prime(n):
    for i in range(2,n):
        if n%i<1:
            return i
for _ in[0]*int(input()):
    n,e=map(int,input().split())
    p=get_prime(n);q=n//p
    print(pow(e,-1,(p-1)*(q-1)))