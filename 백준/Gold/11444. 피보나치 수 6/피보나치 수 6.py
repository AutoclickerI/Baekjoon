n=int(input())
b=(1<<n%3)+1
a=b%2
m=n%2000000016
while 2<m:a,b=b,(a+4*b)%(10**9+7);m-=3
print(a)