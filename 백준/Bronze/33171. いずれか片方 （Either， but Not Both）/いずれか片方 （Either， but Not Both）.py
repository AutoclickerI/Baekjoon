import math
n,a,b=map(int,open(0))
print(n//a+n//b-n//math.lcm(a,b)*2)