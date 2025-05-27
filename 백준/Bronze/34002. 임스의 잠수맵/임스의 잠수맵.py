a,b,c,s,v,l=map(int,open(t:=0).read().split())
x=(250-l)*100
for m,n in(c,v),(b,s):d=min(x,m*30*n);t-=-d//m;x-=d
print(t-(0<x)*x//-a)