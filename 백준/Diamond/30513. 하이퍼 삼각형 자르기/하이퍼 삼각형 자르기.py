import math
M,N=map(int,input().split())
print(sum(math.comb(N-M*t,M+(t<0))for t in range(-1,N//M))%(10**9+7))