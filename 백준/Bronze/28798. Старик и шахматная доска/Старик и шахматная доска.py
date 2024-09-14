n,m=map(int,input().split())
print(int(min(n+m,2*min(n,m)+1)**.5))