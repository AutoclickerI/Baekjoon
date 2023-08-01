import math
p,q,r=map(int,input().split())
print('yneos'[math.lcm(p,q)>r::2])