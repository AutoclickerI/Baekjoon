t,*a=map(int,[*open(0)][r:=1].split())
for i in a:r+=t+i&1;t=i
print(r)