import math
l=[[*map(int,i.split())]for i in[*open(0)][1:]]
print(sum(sorted(math.dist(i,j)for i,j in zip(l,(l*2)[1:]))[:-1]))