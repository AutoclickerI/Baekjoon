*l,=map(int,open(0).read().split())
import math
g=math.gcd(x:=sum(x>y for x in l[:6]for y in l[6:]),36)
print('%d/%d'%(x//g,36//g))