from decimal import*
getcontext().prec=999
a,b=map(Decimal,input().split())
print(a/b)