U,u,D,d,P,p,H=map(int,open(t:=0).read().split())
while 0<H:H-=(t%U<1)*u+(t%D<1)*d+(t%P<1)*p;t+=1
print(t-1)