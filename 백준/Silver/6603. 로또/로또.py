from itertools import combinations
n=input().split()
while n!=['0']:
    z=list(combinations(n[1:], 6))
    for h in z:
        print(*h)
    print()
    n=input().split()