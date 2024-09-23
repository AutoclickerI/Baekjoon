import math
print(sum(max(0,int(10.5-math.hypot(*map(int,i.split()))/20))for i in[*open(0)][1:]))