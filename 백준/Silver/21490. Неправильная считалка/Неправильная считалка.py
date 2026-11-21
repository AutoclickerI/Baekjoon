import math
n,k=map(int,input().split())
print(n-n//math.gcd(n,k))