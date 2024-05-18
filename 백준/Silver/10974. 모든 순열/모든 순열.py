from itertools import*
N=int(input())
for l in permutations(range(1,1+N),N):print(*l)