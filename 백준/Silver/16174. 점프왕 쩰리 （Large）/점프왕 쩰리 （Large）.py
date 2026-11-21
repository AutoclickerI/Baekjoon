def f(x,y):
 if n<=max(x,y):return 0
 v=a[x*n+y];a[x*n+y]=0
 return-v if v<1else f(x+v,y)|f(x,y+v)
n,*a=map(int,open(0).read().split())
print('HaruHaru'*f(0,0)or'Hing')