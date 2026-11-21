f=lambda x,y:n>max(x,y)and(-v if(v:=b[x*n+y])<1else exec('b[x*n+y]=0')or f(x+v,y)or f(x,y+v))
n,*b=map(int,open(0).read().split())
print('HaruHaru'*f(0,0)or'Hing')