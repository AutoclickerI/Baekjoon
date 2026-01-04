n,m=map(int,input().split())
b=[0]*n
exec('i=0;t=[1]\nwhile~i+n:t+=t[-1]+b[i]+b[i:=i+1],\nb=t;'*m)
print(b[-1]%(10**9+7))