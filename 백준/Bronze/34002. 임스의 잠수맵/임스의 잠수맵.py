a,b,c,s,v,l=map(int,open(0).read().split())
x=(250-l)*100
t=0
for m,n in(c,v),(b,s):d=min(x,m*30*n);t-=-d//m;x-=d
print(t*(x<1)or t-x//-a)