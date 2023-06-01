from decimal import*
getcontext().prec=99
D=Decimal
R=D(1e6)
def F(e,s=-R):
 while e-s>1e-20:(s:=p)if f(p:=(s+e)/2)*f(s)>0else(e:=p)
 return s
for i in[*open(0)][1:]:A,B,C,d=map(D,i.split());f=lambda x:((A*x+B)*x+C)*x+d;L=-3*A;Z=B*B+L*C;z,y=sorted([Q:=(B+Z.sqrt())/L,2*B/L-Q]);print(*[F(R)]if(P:=round(f(z),20))*(Q:=round(f(y),20))>0else[F(z),F(y,z),F(R,y)]if P*Q else[F(z),y]if P else[z]+[F(R,y)]*(P!=Q))