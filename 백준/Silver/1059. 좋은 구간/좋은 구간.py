_,*l,N=map(int,open(0).read().split())
l+=0,
rm=min(i for i in l if N<=i)-N
lm=N-max(i for i in l if i<=N)
print(max(rm*lm-1,0))