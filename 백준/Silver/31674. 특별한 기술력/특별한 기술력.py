for H in sorted(map(int,[*open(a:=0)][c:=1].split())):a+=H*c;c*=2
print(a%(10**9+7))