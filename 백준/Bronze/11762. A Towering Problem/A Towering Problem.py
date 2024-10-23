from itertools import*
*a,b,c=map(int,input().split())
for p in permutations(sorted(a)[::-1]):sum(p[:3])==b!=c==sum(p[3:])<exit(print(*p))