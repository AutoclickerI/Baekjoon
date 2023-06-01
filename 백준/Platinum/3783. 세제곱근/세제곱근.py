import math
from decimal import*
getcontext().prec = 1000
for i in range(int(input())):
    n=input()
    p=Decimal(n)**(Decimal(1)/Decimal(3))
    p=Decimal('{:.500f}'.format(p)[:-490])
    if p*p*p>Decimal(n):
        p-=Decimal(str(10**-10))
    elif p*p*p>Decimal(n):
        p-=Decimal(str(10**-10))
    print('{:.500f}'.format(p)[:-490])