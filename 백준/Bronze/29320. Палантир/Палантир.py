n,m,x,y,r,a,b,t=map(int,open(0).read().split())
f=lambda p,v,l:(q:=[p,l-p][0<v])<=(d:=abs(v)*t)and(d-q)//l+1
print(f(x-r,a,n-2*r)+f(y-r,b,m-2*r))