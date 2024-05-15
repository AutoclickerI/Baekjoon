from itertools import*
print(sum(x*y==z for x,y,z in combinations(map(int,[*open(0)][1].split()),3)))