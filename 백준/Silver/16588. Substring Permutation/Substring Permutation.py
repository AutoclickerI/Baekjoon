from collections import*
a,b=map(Counter,open(0))
print('YNEOS'[any(a[i]<b[i]for i in b)::2])