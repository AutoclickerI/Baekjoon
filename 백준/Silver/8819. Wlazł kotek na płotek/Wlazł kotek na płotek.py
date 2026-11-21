import math
for _ in[0]*int(input()):n=int(input());print(*[i for i in range(1,n+1)if math.gcd(i,n)==1])