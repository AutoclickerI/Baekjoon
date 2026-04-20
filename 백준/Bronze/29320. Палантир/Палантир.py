n,m,x,y,r,a,b,t=map(int,open(0).read().split())
f=lambda p,v,l:(abs(v)*t-[p,l-p][0<v]+l)//l
print(f(x-r,a,n-2*r)+f(y-r,b,m-2*r))