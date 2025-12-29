from itertools import*
import math
s=input()
c=1
for i in{*s}:c*=math.factorial(s.count(i))
print(sum(all(map(str.__ne__,i,i[1:]))for i in permutations(s))//c)