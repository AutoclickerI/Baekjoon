import math
c=math.comb
n=int(input())
print(sum((-1)**k*c(13,1+k)*c(48-4*k,52-n)for k in range(13))%10007)