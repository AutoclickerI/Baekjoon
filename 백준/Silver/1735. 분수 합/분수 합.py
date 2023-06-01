import math
p,q,r,s=map(int,open(0).read().split())
g=math.gcd(d:=q*s,q:=q*r+p*s)
print(q//g,d//g)