f=lambda x,y:n>max(x,y)and(-v if(v:=b[x*n+y])<1else f(x+v,y)|f(x,y+v))
n,*b=map(int,open(0).read().split())
print(['Hing','HaruHaru'][f(0,0)])