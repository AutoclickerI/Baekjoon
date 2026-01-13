from itertools import*
s=input()
print(next(filter(s.__lt__,map(''.join,permutations(sorted(s)))),0))