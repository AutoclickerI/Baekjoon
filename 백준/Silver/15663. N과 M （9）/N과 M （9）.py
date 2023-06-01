from itertools import permutations
a = input().split()[1]
b = sorted(list(map(int,input().split())))
for i in sorted(set(permutations(b, int(a)))):
    print(*i)