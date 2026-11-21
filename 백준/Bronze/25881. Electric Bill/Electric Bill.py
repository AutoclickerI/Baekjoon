p,q,r,*s=map(int,open(0).read().split())
for i in s:print(i,min(1000,i)*p+max(i-1000,0)*q)