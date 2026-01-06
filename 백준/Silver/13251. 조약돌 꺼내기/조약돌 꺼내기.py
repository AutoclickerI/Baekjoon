M,*c,K=map(int,open(0).read().split())
import math
r=0
for i in c:r+=math.comb(i,K)
print(r/math.comb(sum(c),K))