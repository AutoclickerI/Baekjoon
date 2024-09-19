import math
_,s,*l=map(int,open(0).read().split())
print(7+(s+math.lcm(*l))%-7)