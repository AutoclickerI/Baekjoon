import re
for s in[*open(0)][1:]:print(re.match('(100+1+|01)+$',s)and'YES'or'NO')