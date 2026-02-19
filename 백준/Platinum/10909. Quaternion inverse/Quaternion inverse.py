p,q,*l=map(int,open(0).read().split())
for a,b,c,d in zip(*[iter(l)]*4):H=a*a+b*b+c*c+d*d;[print(H%p and-i*pow(H,-1,p))for i in[-a,b,c,d]]