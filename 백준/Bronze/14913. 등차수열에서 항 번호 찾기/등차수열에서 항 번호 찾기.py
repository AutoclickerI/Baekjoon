p,q,r=map(int,input().split())
p=r-p
print([p//q+1,'X'][p%q!=0 or p//q<0])