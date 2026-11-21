a,b=map(int,input().split())
x=max(2,-~a//2)
y=b//2or 1
print(x-y*~y-x*x)