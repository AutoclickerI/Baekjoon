n,m=map(int,input().split())
c=0
while m:c+=n//m;n,m=m,n%m
print(c)