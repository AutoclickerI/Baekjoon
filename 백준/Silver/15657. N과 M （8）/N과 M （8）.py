from itertools import combinations_with_replacement
a = input().split()[1]
b = sorted(list(map(int,input().split())))
for i in combinations_with_replacement(b, int(a)):
    print(*i)