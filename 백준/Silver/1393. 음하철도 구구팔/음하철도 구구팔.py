import math
a,b,c,d,e,f=map(int,open(0).read().split())
g=math.gcd(e,f);e//=g;f//=g
print(*min([((c+t*e-a)**2+(d+t*f-b)**2,(c+t*e,d+t*f))for t in range(500)])[1])