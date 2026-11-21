d,p,q=map(int,input().split())
r,i=2e9,0
while((x:=(i-d)//q)<1)*p*q>i:r=min(r,i-q*x);i+=p
print(r)