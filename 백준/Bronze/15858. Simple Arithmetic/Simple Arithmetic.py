from decimal import*
getcontext().prec=9999
a,b,c=map(Decimal,input().split())
print(f'{a*b/c:.10f}')