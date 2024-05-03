from itertools import*
print(*min(z for z in permutations(input().split())if'0'<z[0]),sep='')