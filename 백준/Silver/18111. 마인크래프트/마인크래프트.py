_,_,b,*a=map(int,open(0).read().split())
p=9e9
for h in range(257):
 f=r=0
 for x in a:G=max(g:=x-h,0);r+=G;f-=g-G
 if(t:=2*r+f)-p<1>f-r-b:p,q=t,h
print(p,q)