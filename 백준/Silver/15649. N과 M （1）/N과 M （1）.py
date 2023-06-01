from itertools import permutations
a = input().split()
for i in permutations(list(map(str, range(1, int(a[0]) + 1))), int(a[1])):
    print(' '.join(i))