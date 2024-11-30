import math
n,a,b=map(int,input().split())
p,q,r=n//a,n//b,n//math.lcm(a,b)
print(p-r,q-r,r)