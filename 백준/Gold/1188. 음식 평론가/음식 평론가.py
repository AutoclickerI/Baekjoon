n,m=map(int,input().split())
t=m
while m:n,m=m,n%m
print(t-n)