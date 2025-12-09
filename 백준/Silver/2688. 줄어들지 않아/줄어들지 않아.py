import math
print(*[math.comb(i+9,i)for i in map(int,open(0))][1:])