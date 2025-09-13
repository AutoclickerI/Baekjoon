n,l,*z,v=map(int,open(0).read().split())
t=p=0
for i,j in zip(z,z[n:]):t=max(i*v,t+i-p)+j*v;p=i
print('YNEOS'[l*v<t+l-p::2])