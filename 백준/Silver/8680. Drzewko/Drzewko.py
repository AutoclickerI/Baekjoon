n,h=map(int,input().split())
a=0
while h:
    a+=~n%2*pow(2,h-1)
    n-=n//2
    h-=1
print(a)