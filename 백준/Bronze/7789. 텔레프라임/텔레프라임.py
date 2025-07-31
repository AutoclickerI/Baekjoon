f=lambda n:any(n%i<1for i in range(2,n))
a,b=input().split()
print('YNeos'[f(int(a))|f(int(b+a))::2])