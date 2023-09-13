import re
for s in[*open(0)][1:]:print('YNEOS'[not re.match('(100+1+|01)+$',s)::2])