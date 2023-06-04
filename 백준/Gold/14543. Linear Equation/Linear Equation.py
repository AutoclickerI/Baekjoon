from math import*
from decimal import*
getcontext().prec=999
for i in range(int(input())):
    print('Equation',i+1)
    s=input()
    a=int(s[:s.index('x')])
    b=int(s[s.index('+')+1:s.index('=')])
    c=int(s[s.index('=')+1:])
    if a!=0:print(f'x = {(c-b)/Decimal(a):.99f}'[:-93]+'\n')
    elif b==c:print('More than one solution.\n')
    else:print('No solution.\n')