from itertools import product
a = input().split()
for i in product(list(map(str, range(1, int(a[0]) + 1))), repeat = int(a[1])):
    print(' '.join(i))