import math
f=lambda i:math.isqrt(z:=int(i))**2!=z
for i in[*open(0)][1:]:print('YNEOS'[f(i)|f(i[::-1])::2])