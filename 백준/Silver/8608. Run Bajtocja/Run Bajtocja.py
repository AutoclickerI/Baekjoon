import math
_,*l=map(int,open(0))
N=math.lcm(*l)
for i in l:print(N//i)