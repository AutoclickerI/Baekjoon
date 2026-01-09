n,*s=map(int,open(0).read().split())
r=v=0
for i in s:f=i&1;r+=f;v+=r-r*f
print(min(v,(n-r)*r-v))