from decimal import*
getcontext().prec=99
I,S,D=input,sorted,Decimal
R=D(1e6)
G=lambda x:round(x,20)
def F(e=R,s=-R):
 while e-s>1e-20:(s:=p)if f(p:=s/2+e/2)*f(s)>0else(e:=p)
 return s
for i in range(int(I())):A,B,C,d=map(D,I().split());f=lambda x:A*x**3+B*x*x+C*x+d;L=-3*A;Z=B*B+L*C;z,y=S([Q:=(B+Z**D('0.5'))/L,2*B/L-Q]);print(*[F()]if Z<0else[F()]if G((P:=f(z))*(Q:=f(y)))>0else[F(z),F(y,z),F(R,y)]if G(P)*G(Q)else[F(z),y]if G(P)else[z,F(R,y)]if P-Q else[z])