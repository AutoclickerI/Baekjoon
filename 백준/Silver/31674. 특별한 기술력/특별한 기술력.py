m=10**9+7
for H in sorted(map(int,[*open(a:=0)][c:=1].split())):a+=H*c;c=c*2%m
print(a%m)