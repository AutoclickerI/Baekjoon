p,q,*l=map(int,open(0).read().split())
for*z,in zip(*[iter(l)]*4):z[0]*=-1;H=sum(i*i for i in z);[print(H%p and-i*pow(H,-1,p))for i in z]