import math
for i in[*open(0)][1:]:a,b=map(int,i.split());g=math.gcd(a,b);print(a//g,b//g)