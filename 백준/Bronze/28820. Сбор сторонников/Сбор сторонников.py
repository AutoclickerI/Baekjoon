import math
_,s,*l=map(int,open(0).read().split())
print((s-1+math.lcm(*l))%7+1)