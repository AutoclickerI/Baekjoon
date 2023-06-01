a,b,c=list(map(int,input().split()))
def f(a,b):
    if b==0:
        return 1
    x=f(a,b//2)
    if b%2==0:
        return x**2%c
    return x**2*a%c
print(f((a-c),b)%c)