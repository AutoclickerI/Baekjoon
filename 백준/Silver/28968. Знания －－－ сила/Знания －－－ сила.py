n,k=map(int,input().split())
a,b=0,n
m=10**9+7
exec("a,b=(2*a+b)%m,(a+b)%m;"*-~k)
print(b)