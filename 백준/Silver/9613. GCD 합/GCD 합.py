import math
for i in[*open(0)][1:]:_,*l=map(int,i.split());print(-sum([-math.gcd(i,j)for i in l for j in l]+l)//2)