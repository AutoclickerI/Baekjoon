import math
for i in[*open(0)][1:]:n,*l=map(int,i.split());print(sum(math.gcd(l[i],j)for i in range(n)for j in l[i+1:]))