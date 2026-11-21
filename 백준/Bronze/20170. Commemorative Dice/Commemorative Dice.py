l=open(0).read().split()
from fractions import*
print(Fraction(sum(int(x)>int(y)for x in l[:6]for y in l[6:]),36))