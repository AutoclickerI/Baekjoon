from itertools import combinations
a = input().split()[1]
b = sorted(list(map(int,input().split())))
for i in sorted(set(combinations(b, int(a)))):
    print(*i)