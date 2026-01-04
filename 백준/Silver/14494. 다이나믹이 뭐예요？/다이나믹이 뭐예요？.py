n,m=map(int,input().split())
b=[0]*n
exec('t=[1]\nfor i in range(1,n):t+=t[-1]+b[i]+b[i-1],\nb=t;'*m)
print(b[-1]%(10**9+7))