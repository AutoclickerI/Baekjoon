from itertools import combinations_with_replacement
a = input().split()
for i in combinations_with_replacement(list(map(str, range(1, int(a[0]) + 1))), int(a[1])):
    print(' '.join(i))