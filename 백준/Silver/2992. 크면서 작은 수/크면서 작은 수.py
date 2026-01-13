from itertools import*
s=*input(),
print(min([''.join(i)for i in permutations(s)if s<i]or[0]))