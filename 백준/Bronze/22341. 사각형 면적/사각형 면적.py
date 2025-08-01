n,c,*l=map(int,open(0).read().split())
x=y=n
while l:
 a,b,*l=l
 if a<y>0<b<x:y,x=[(a,x),(y,b)][x*a<y*b]
print(y*x)