f=lambda n:n and 2*f(n//2)-n//-2
a,b=map(int,input().split())
print(f(b)-f(a-1))