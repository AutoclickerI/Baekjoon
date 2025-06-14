n,s=open(0)
from itertools import*
exec("s=''.join(str(len([*w]))+v for v,w in groupby(s.strip()));"*int(n))
print(s)