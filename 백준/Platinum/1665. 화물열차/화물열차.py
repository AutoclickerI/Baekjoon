p,*r=map(int,open(0).read().split())
q=r.pop(p*2)
l=[]
for I in range(p*q):i=I//q*2;x,X,y,Y=3*r[i],3*r[i+1],3*r[(k:=2*p+I%q*2)],3*r[k+1];l+=[x+y-4,x+Y-3,X+y-3,X+Y+2]
g=v=p=V=P=0
for i in sorted(l):
 v+=g*(i//3-p);g+=i%3-1;p=i//3
 if V<v:V,P=v,i//3
print(P)