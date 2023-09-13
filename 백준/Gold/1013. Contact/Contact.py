import re
for _ in[0]*int(input()):print('YNEOS'[not re.fullmatch('(100+1+|01)+', input())::2])