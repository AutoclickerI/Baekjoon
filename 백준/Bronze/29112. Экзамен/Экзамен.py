import math
l,r=map(int,input().split())

def isdouble(n):
    return n==math.isqrt(n)**2

ans=0
s=0
while s**3//6<=r:
    if s**3%6<1 and l<=s**3//6:
        ans+=isdouble(s**3//6*10)
    s+=1
print(ans)