from itertools import*
print('yneos'[any((x-y)%z for x,y,z in permutations(map(int,[*open(0)][1].split()),3))::2])