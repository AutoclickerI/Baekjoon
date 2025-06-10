l=[0]+[1e9]*1100
C,_,*z=map(int,open(0).read().split())
while z:c,v,*z=z;i=0;exec('l[i]=min(l[i-v]+c,l[i]);i+=1;'*1100)
print(min(l[C:]))