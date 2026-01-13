from itertools import*
s=*input(),
print(*next(filter(s.__lt__,permutations(sorted(s))),'0'),sep='')