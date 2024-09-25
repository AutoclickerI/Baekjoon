N,D,p,*l=map(int,open(0).read().split())
t=x=0
for i in l:i=max(i-t,0);c=i//-D;x-=c;t=(i+c*D)*-p//100
print(x)