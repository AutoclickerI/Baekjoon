a,b,c,d,e,f=map(int,open(0).read().split())
x,y=a+2*b+3*c,d+2*e+3*f
print((x>y)+2*(x<y))