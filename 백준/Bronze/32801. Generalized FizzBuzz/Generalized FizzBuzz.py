import math
n,a,b=map(int,input().split())
g=n//math.lcm(a,b)
print(n//a-g,n//b-g,g)