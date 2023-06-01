p=10**9+7
f=lambda n:1 if n<1 else 2 if n==1 else f(n//2)**2%p if n%2==0 else f(n//2)**2*2%p
print(f(int(input())-1))