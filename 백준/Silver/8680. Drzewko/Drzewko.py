n,h=map(int,input().split())
a=0
while h:h-=1;a+=~n%2<<h;n-=n//2
print(a)