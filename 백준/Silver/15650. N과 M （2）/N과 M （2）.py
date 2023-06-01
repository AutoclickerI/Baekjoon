from itertools import combinations
a = input().split()
for i in combinations(list(map(str, range(1, int(a[0]) + 1))), int(a[1])):
    print(' '.join(i))