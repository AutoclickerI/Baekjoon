from itertools import*
print(max(i*j*(str(i*j)in'123456789')or-1for i,j in combinations(map(int,[*open(0)][1].split()),2)))