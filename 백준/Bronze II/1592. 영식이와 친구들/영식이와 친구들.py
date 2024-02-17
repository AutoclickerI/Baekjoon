import math
n,m,l=map(int,input().split())
print(n*~-m//math.gcd(n,l))