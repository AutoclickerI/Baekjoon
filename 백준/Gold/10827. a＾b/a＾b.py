from decimal import*
getcontext().prec=9999
a,b=map(Decimal,input().split())
print(f'{a**b:f}')