from decimal import*
getcontext().prec=9999
a,b=map(Decimal,input().split())
print(format(a**b.normalize(),'f'))