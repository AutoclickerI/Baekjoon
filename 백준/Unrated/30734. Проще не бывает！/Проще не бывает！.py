import math
x=math.isqrt(n:=int(input())-1)
print(x-abs(n+x*~x)+1)