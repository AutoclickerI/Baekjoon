n,s=open(0)
r=v=0
for i in s.split():f=int(i)&1;r+=f;v+=r-r*f
n=int(n)-r
print(min(v,n*r-v))