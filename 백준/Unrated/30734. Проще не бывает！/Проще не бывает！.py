import math
n=int(input())-1
x=math.isqrt(n)
print(x-abs(n-x*x-x)+1)