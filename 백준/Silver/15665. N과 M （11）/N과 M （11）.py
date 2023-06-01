from itertools import product
a = input().split()[1]
b = sorted(list(map(int,input().split())))
for i in sorted(set(product(b, repeat=int(a)))):
    print(*i)