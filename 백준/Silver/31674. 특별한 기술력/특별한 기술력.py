a,c,m=0,1,10**9+7
for H in sorted(map(int,[*open(0)][1].split())):a=(a+H*c)%m;c=c*2%m
print(a)